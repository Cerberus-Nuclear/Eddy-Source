#!/usr/bin/python3
# Peter Evans
# Cerberus Nuclear Ltd

"""
This module holds the code that writes HTML to the html file.
"""


# Imports from standard library
import datetime
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


def get_html(case):
    """Get the HTML from the jinja template

    Args:
        case (EddyMCNPCase): The EddyMCNPCase object for this Eddy run

    Returns:
        html (str): The completed html output
    """
    inline_css = get_css()

    html_template = pkg_resources.read_text(static, 'MCNP_template.html')
    template = Template(html_template)
    html = template.render(
        filename=case.filepath,
        case_name=case.name,
        # logo=f"{os.getcwd()}/static/logo.png",
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
        input_deck=case.mcnp_input,
        cycles=case.cycles,
        )
    return html
