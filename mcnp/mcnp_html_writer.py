#!/usr/bin/python3
# Peter Evans
# Cerberus Nuclear Ltd

"""
This module holds the code that writes HTML to the html file.
"""


# Imports from standard library
import datetime
import os
# Third party imports:
from jinja2 import Template
# local imports
from . import global_variables as gv


def get_css():
    """Read in css from static css file

    Returns:
        inline_css (str): the whole static css file
    """
    with open(r"static/style.css") as file:
        inline_css = file.read()
    return inline_css


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
    with open("static/MCNP_template.html", "r") as file:
        template = Template(file.read())
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
        parameters=gv.parameters,
        k_eff=gv.k_effective,
        tally_list=gv.tally_list,
        tally_types=gv.f_types,
        f2_tallies=gv.F2_tallies,
        f4_tallies=gv.F4_tallies,
        f5_tallies=gv.F5_tallies,
        warnings=gv.warnings,
        comments=gv.comments,
        duplicate_surfaces=gv.duplicate_surfaces,
        cell_list=gv.cell_list,
        particle_list=gv.particle_list,
        input_deck=gv.mcnp_input,
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
