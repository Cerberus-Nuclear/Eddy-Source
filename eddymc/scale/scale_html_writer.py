#!/usr/bin/env python3
# Peter Evans
# Cerberus Nuclear Ltd

""" This module creates the HTML output for the SCALE data """

# Standard library imports
import datetime
try:
    import importlib.resources as pkg_resources
except ImportError:
    import importlib_resources as pkg_resources
# Third party imports
from jinja2 import Template
# local imports
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


def get_html(case):
    """Get the html output from the jinja template

    Args:
        case (EddySCALECase): The EddySCALECase object for this Eddy run

    Returns:
        html (str): the html output as a single string
    """
    inline_css = get_css()
    html_template = pkg_resources.read_text(static, 'SCALE_template.html')
    template = Template(html_template)
    # render template as a unicode string
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
        tally_list=case.tally_list,
        mixture_list=case.mixture_list,
        input_deck=case.scale_input,
        )
    return html
