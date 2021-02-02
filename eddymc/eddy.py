#!/usr/bin/env python3
# Peter Evans
# Cerberus Nuclear Ltd

"""Eddy is a programme to convert the text-based output files from MCNP and SCALE to
a user-friendly HTML format.

Copyright (C) 2020  Cerberus Nuclear Ltd

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.


This module is the entry point for Eddy, the MCNP and SCALE to HTML output converter.
If run as __main__, this script asks for an output file and scaling factor, 
determines whether it is an MCNP or SCALE case, and creates the relevant EddyMCNPCase or EddySCALECase
object, then calls the relevant HTML writer

Alternatively, main() can be called directly by another module and provided with the same two arguments.
"""

# Imports from standard library
import os.path
import argparse
from tkinter import Tk, simpledialog
from tkinter.filedialog import askopenfilename

# Local imports
if __name__ == "__main__":
    from scale import scale_html_writer
    from scale.eddy_scale_case import EddySCALECase
    from mcnp import mcnp_html_writer
    from mcnp.eddy_mcnp_case import EddyMCNPCase
else:
    from .scale import scale_html_writer
    from .scale.eddy_scale_case import EddySCALECase
    from .mcnp import mcnp_html_writer
    from .mcnp.eddy_mcnp_case import EddyMCNPCase


class NotAcceptedFileTypeError(Exception):
    """Raised when the file selected is not recognised as a SCALE or MCNP output"""


def main(filename=None, scaling_factor=None):
    """Entry point to Eddy. Can take filename and scaling factor as arguments.
    Call get_args to find the filename & scaling factor if not provided, and also get the
    output data and determine whether it is a crit case.
    Determine whether it is an MCNP or SCALE case;
    call the relevant converter.

    Args:
        filename (str): the file path (including the name) of the output file
        scaling_factor (float): A number by which the results will be multiplied
    """


    filename, output_data, scaling_factor, crit_case = get_args(filename, scaling_factor)

    if 'SCALE' in output_data[2]:
        case = EddySCALECase(
            filepath=filename,
            file=output_data,
            scaling_factor=scaling_factor,
        )
        html = scale_html_writer.get_html(case)
    elif 'Code Name & Version = MCNP' in output_data[0]:
        case = EddyMCNPCase(
            filepath=filename,
            scaling_factor=scaling_factor,
            file=output_data,
            crit_case=crit_case,
        )
        html = mcnp_html_writer.get_html(case)
    else:
        raise NotAcceptedFileTypeError("This file doesn't seem to be an MCNP or SCALE output?")
    output_file, extension = os.path.splitext(filename)
    output_file += '.html'
    write_output(output_file, html)
    print(f"Eddy run complete, {output_file} created.\n")


def get_args(filename=None, scaling_factor=None):
    """
    Get the args from argparse if they are sent by the command line,
    Call functions to get filename and scaling factor.
    Determine if this is a crit case (for MCNP).
    Read in the output data from the mcnp output file.

    Args:
        filename (optional) (str or None): the file path (including the name) of the output file, may be None
        scaling_factor (optional) (float or None): the scaling factor to multiply results by, may be None

    Returns:
        filename (str): the file path (including the name) of the output file
        output_data (list): The contents of the output file
        scaling_factor (float): the scaling factor to multiply results by
        crit_case (bool): True if kcode case, otherwise False
    """

    filename = get_filename(filename)

    # get contents of file
    output_data = read_file(filename)

    # Check if shielding or crit case
    crit_case = check_if_crit(output_data)

    # get scaling factor
    if crit_case:
        # set scaling factor to 1 for crit cases (this variable will not be used)
        scaling_factor = 1
    else:
        # Ask for scaling factor for shielding cases, and check it is a valid float.
        scaling_factor = get_scaling_factor(scaling_factor)

    print(f"Output file selected: {filename}")
    return filename, output_data, scaling_factor, crit_case


def get_filename(filename=None):
    """ Get the name and path of the MCNP output file
    Args:
        filename(str): The filename including filepath
    Returns:
        filename (str): The filename including filepath
    """
    # open tkinter window for file selection
    if not filename:
        Tk().withdraw()
        filename = askopenfilename(
            title="Select Output File",
            filetypes=(("output files", "*.out"), ("all files", "*.*"))
            )

    # check file exists
    assert os.path.isfile(filename), "That MCNP file does not exist in that location."
    return filename


def read_file(filename):
    """Read in the output file.

    Args:
        filename (str): The name (and location) of the .out file

    Returns:
        data (list): The lines from the output file
    """
    with open(filename, 'r') as file:
        data = file.readlines()
    return data


def check_if_crit(output_data):
    """Read through output data to check if case is crit or shielding

    Args:
        output_data (list): The text of the output file

    Returns:
        True if kcode found or False if not.

    """
    for line in output_data:
        if 'kcode' in line.lower():
            return True
    return False


def get_scaling_factor(scaling_factor=None):
    """ Get the scaling factor to multiply results by for a shielding case
    Args: None
    Returns:
        scaling_factor (float): The scaling factor
    """
    if not scaling_factor:
        # open tkinter window to ask for scaling factor
        Tk().withdraw()
        scaling_factor = simpledialog.askfloat(
            title="Scaling Factor",
            prompt="Please enter a scaling factor to multiply your results by", initialvalue=1,
        )
    # type checking for scaling factor
    if type(scaling_factor) is not float:
        try:
            scaling_factor = float(scaling_factor)
        except ValueError:
            print("The scaling factor should be a floating-point (decimal) number")
            raise
    return scaling_factor


def write_output(file, html):
    """Write the HTML to the desired file

    Args:
        file (str): The filepath of the html file to be written
        html (str): The contents to be written to the html file
    """
    with open(file, 'w') as f:
        f.write(html)


if __name__ == "__main__":
    # Eddy should only take command line args if run as __main__
    parser = argparse.ArgumentParser(description='MCNP or SCALE output to HTML Converter')
    parser.add_argument("-o", "--file", help="MCNP or SCALE output file")
    parser.add_argument("-sf", "--scaling_factor", type=float, help="Scaling Factor")
    # Note: args will be an argparse Namespace object, with the values for args.file and args.scaling_factor
    # set to None if no cli arguments have been passed.
    args = parser.parse_args()
    main(filename=args.file, scaling_factor=args.scaling_factor)
