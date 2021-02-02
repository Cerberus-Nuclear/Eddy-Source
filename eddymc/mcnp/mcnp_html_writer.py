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
from jinja2 import Template
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


def sanitize_input(mcnp_input):
    """Replaces any < and > characters in the mcnp output with html codes &lt and &gt to stop
    them from being interpreted as html tags.

    Args: mcnp_input [list]: The mcnp input file
    Returns: san_mcnp_input [list]: The sanitized version of the mcnp input
    """
    san_mcnp_input = []
    for line in mcnp_input:
        if "<" in line:
            line = line.replace("<", "&lt")
        if ">" in line:
            line = line.replace(">", "&gt")
        san_mcnp_input.append(line)
    return san_mcnp_input


def get_html(case, inline_css):
    """Get the HTML from the jinja template

    Args:
        case (EddyCase): The EddyCase object for this Eddy run
        inline_css (str): The whole css file as a single string

    Returns:
        html (str): The completed html output
    """
    case_name, extension = os.path.splitext(case.filepath)
    case_name = case_name.replace('\\', '/').split('/')[-1]
    mcnp_input = sanitize_input(case.mcnp_input)
    #with open("static/MCNP_template.html", "r") as file:
    #    html_template = file.read()
    html_template = pkg_resources.read_text(static, 'MCNP_template.html')
    template = Template(html_template)
    html = template.render(
        filename=case.filepath,
        case_name=case_name,
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
        fatal_errors=case.fatal_errors,
        lost_particles=case.lost_particles,
        k_eff=case.k_effective,
        tally_list=case.tally_list,
        tally_types=case.f_types,
        f2_tallies=case.F2_tallies,
        f4_tallies=case.F4_tallies,
        f5_tallies=case.F5_tallies,
        f6_tallies=case.F6_tallies,
        warnings=case.warnings,
        comments=case.comments,
        duplicate_surfaces=case.duplicate_surfaces,
        cell_list=case.cell_list,
        particle_list=case.particle_list,
        input_deck=mcnp_input,
        cycles=case.cycles,
        )
    return html


def main(case):
    """Provide entry point to this module and call other functions to create HTML,
    write that completed html to the output file

    Args:
        case (EddyCase): The EddyCase object for this Eddy run

    Returns:
        None
    """
    css = get_css()
    output = get_html(case, css)
    output_file, extension = os.path.splitext(case.filepath)
    output_file += '.html'
    with open(output_file, 'w') as f:
        f.write(output)


