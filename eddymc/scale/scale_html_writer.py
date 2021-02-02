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


def get_html(case):
    """Get the html output from the jinja template

    Args:
        case (EddySCALECase): The EddySCALECase object for this Eddy run

    Returns:
        html (str): the html output as a single string
    """
    inline_css = get_css()
    scale_input = sanitize_input(case.scale_input)
    html_template = pkg_resources.read_text(static, 'SCALE_template.html')
    template = Template(html_template)
    # render template as a unicode string
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
        tally_list=case.tally_list,
        mixture_list=case.mixture_list,
        input_deck=scale_input,
        )
    return html




