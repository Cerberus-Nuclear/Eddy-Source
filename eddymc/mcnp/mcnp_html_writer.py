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
from . import global_variables as gv
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
            line = line.replace("<","&lt")
        if ">" in line:
            line = line.replace(">", "&gt")
        san_mcnp_input.append(line)
    return san_mcnp_input


def get_html(filename, inline_css):
    """Get the HTML from the jinja template

    Args:
        filename (str): The mcnp output file path
        inline_css (str): The whole css file as a single string

    Returns:
        html (str): The completed html output
    """
    case_name, extension = os.path.splitext(filename)
    case_name = case_name.replace('\\', '/').split('/')[-1]
    mcnp_input = sanitize_input(gv.mcnp_input)
    #with open("static/MCNP_template.html", "r") as file:
    #    html_template = file.read()
    html_template = pkg_resources.read_text(static, 'MCNP_template.html')
    template = Template(html_template)
    html = template.render(
        filename=filename, # with path
        case_name=case_name,
        #logo=f"{os.getcwd()}/static/logo.png",
        inline_css=inline_css,
        rundate=gv.rundate,
        runtime=gv.runtime,
        date=datetime.datetime.now().strftime("%Y/%m/%d"),
        time=datetime.datetime.now().strftime("%H:%M:%S"),
        scaling_factor=gv.scaling_factor,
        ctme=gv.ctme,
        nps=gv.nps,
        parameters=gv.parameters,
        fatal_errors=gv.fatal_errors,
        k_eff=gv.k_effective,
        tally_list=gv.tally_list,
        tally_types=gv.f_types,
        f2_tallies=gv.F2_tallies,
        f4_tallies=gv.F4_tallies,
        f5_tallies=gv.F5_tallies,
        f6_tallies=gv.F6_tallies,
        warnings=gv.warnings,
        comments=gv.comments,
        duplicate_surfaces=gv.duplicate_surfaces,
        cell_list=gv.cell_list,
        particle_list=gv.particle_list,
        input_deck=mcnp_input,
        cycles=gv.cycles,
        )
    return html


def main(filename):
    """Provide entry point to this module and call other functions to create HTML,
    write that completed html to the output file

    Args:
        filename (str): The file path of the MCNP output file

    Returns:
        None
    """
    css = get_css()
    output = get_html(filename, css)
    output_file, extension = os.path.splitext(filename)
    output_file += '.html'
    with open(output_file, 'w') as f:
        f.write(output)


