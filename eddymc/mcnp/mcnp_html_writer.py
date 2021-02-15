#!/usr/bin/python3
# Peter Evans
# Cerberus Nuclear Ltd

"""
This module holds the code that writes HTML to the html file.
"""


# Imports from standard library
import datetime
import os
try:
    import importlib.resources as pkg_resources
except ImportError:
    import importlib_resources as pkg_resources
# Third party imports:
from jinja2 import Template, escape
# local imports
try:
    from .. import static
except ValueError:
    import static



def get_css():
    """Read in css from static css file

    Returns:
        inline_css (str): the whole static css file
    """
    inline_css = pkg_resources.read_text(static, 'style.css')
    return inline_css


def sanitize_list(text):
    """Replace any html control characters in the mcnp output with the appropriate html codes to stop
    them from being interpreted as html tags.

    Args:
        mcnp_input [list]: The mcnp input file

    Returns:
        list: The sanitized version of the mcnp input
    """
    sanitized_text = []
    for line in text:
        line = str(escape(line))
        sanitized_text.append(line)
    return sanitized_text


def get_html(case):
    """Get the HTML from the jinja template

    Args:
        case (EddyMCNPCase): The EddyMCNPCase object for this Eddy run

    Returns:
        html (str): The completed html output
    """
    inline_css = get_css()

    # The mcnp input needs sanitizing because it can contain partial html tags, e.g. <h1 describing hydrogen
    mcnp_input = sanitize_list(case.mcnp_input)

    """We are also going to sanitize all the sections that are lists of strings.
    I don't think MCNP puts any HTML control characters in these, so this may be excessive.
    There are other cases, i.e. cell names, parameter names, that have not been sanitized
    """
    warnings = sanitize_list(case.warnings)
    comments = sanitize_list(case.comments)
    duplicate_surfaces = sanitize_list(case.duplicate_surfaces)
    fatal_errors = sanitize_list(case.fatal_errors)

    html_template = pkg_resources.read_text(static, 'MCNP_template.html')
    template = Template(html_template)
    html = template.render(
        filename=case.filepath,
        case_name=case.name,
        #logo=f"{os.getcwd()}/static/logo.png",
        inline_css=inline_css,
        rundate=case.rundate,
        runtime=case.runtime,
        date=datetime.datetime.now().strftime("%Y/%m/%d"),
        time=datetime.datetime.now().strftime("%H:%M:%S"),
        scaling_factor=case.scaling_factor,
        ctme=case.ctme,
        nps=case.nps,
        parameters=case.parameters,
        fatal_errors=fatal_errors,
        lost_particles=case.lost_particles,
        k_eff=case.k_effective,
        tally_list=case.tally_list,
        tally_types=case.f_types,
        f2_tallies=case.F2_tallies,
        f4_tallies=case.F4_tallies,
        f5_tallies=case.F5_tallies,
        f6_tallies=case.F6_tallies,
        warnings=warnings,
        comments=comments,
        duplicate_surfaces=duplicate_surfaces,
        cell_list=case.cell_list,
        particle_list=case.particle_list,
        input_deck=mcnp_input,
        cycles=case.cycles,
        )
    return html
