#!/usr/bin/env python3
# Peter Evans
# Cerberus Nuclear Ltd

""" This module creates the HTML output for the SCALE data """

# Standard library imports
import os
import datetime
try:
    import importlib.resources as pkg_resources
except ImportError:
    import importlib_resources as pkg_resources
# Third party imports
from jinja2 import Template
#local imports
from . import scale_global_variables as gv
try:
    from .. import static
except ValueError:
    import static


def get_css():
    """Get the css to be used in the html output

    Returns:
        inline_css (str): The whole static css file as a single string
    """
    inline_css = pkg_resources.read_text(static, 'style.css')
    return inline_css


def sanitize_input(scale_input):
    """Replaces any < and > characters in the scale output with html codes &lt and &gt to stop
    them from being interpreted as html tags.

    Args: mcnp_input [list]: The mcnp input file
    Returns: san_mcnp_input [list]: The sanitized version of the mcnp input
    """
    san_scale_input = []
    for line in scale_input:
        if "<" in line:
            line = line.replace("<","&lt")
        if ">" in line:
            line = line.replace(">", "&gt")
        san_scale_input.append(line)
    return san_scale_input


def get_html(filename, inline_css):
    """Get the html output from the jinja template

    Args:
        filename (str): The file path of the SCALE output file
        inline_css (str): The css as a single string

    Returns:
        html (str): the html output as a single string
    """
    scale_input = sanitize_input(gv.scale_input)
    html_template = pkg_resources.read_text(static, 'SCALE_template.html')
    template = Template(html_template)
    case_name, extension = os.path.splitext(filename)
    case_name = case_name.replace('\\', '/').split('/')[-1]
    # render template as a unicode string
    html = template.render(
        filename=filename,
        case_name=case_name,
        #logo=f"{os.getcwd()}/static/logo.png",
        inline_css=inline_css,
        rundate=gv.rundate,
        runtime=gv.runtime,
        date=datetime.datetime.now().strftime("%Y/%m/%d"),
        time=datetime.datetime.now().strftime("%H:%M:%S"),
        scaling_factor=gv.scaling_factor,
        tally_list=gv.tally_list,
        mixture_list=gv.mixture_list,
        input_deck=scale_input,
        )
    return html


def main(filename):
    """Provide entry point to this module and call other functions to create HTML,
    write that completed html to the output file

    Args:
        filename (str): The file path of the SCALE output file

    Returns:
        None
    """
    inline_css = get_css()
    output = get_html(filename, inline_css)
    output_file, extension = os.path.splitext(filename)
    output_file += '.html'
    with open(output_file, 'w') as f:
        f.write(output)


