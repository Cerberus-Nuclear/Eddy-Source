#!/usr/bin/env python3
# Peter Evans
# Cerberus Nuclear Ltd

"""
    This module is the base of the SCALE to HTML converter section of Eddy.
"""

# local imports
from . import scale_tallies, mixtures, scale_global_variables as gv, scale_html_writer


def read_file(filename):
    """Read in the SCALE output file.

    Args:
        filename (str): The file path of the SCALE .out file

    Returns:
        data (list): The lines from the output file
    """
    with open(filename, 'r') as file:
        data = file.readlines()
    return data


def get_runtime(data):
    """Find the date and time that the SCALE case was run

    Args:
        data(list): The SCALE output data

    Returns:
        A tuple containing
            rundate (str): the date the case was run
            runtime (str): the time the case was run
    """
    for line in data:
        if "Job started on" in line:
            rundate = line.split()[6]
            # rearrange date from m/d/y to y/m/d
            y = rundate.split('/')[2]
            m = rundate.split('/')[1]
            d = rundate.split('/')[0]
            rundate = f"{y}/{m}/{d}"
            # time is fine as h/m/s
            runtime = line.split()[7]
            return rundate, runtime


def get_input(data):
    """Get the SCALE input deck from the output file

    Args:
        data (list): The SCALE output data

    Returns:
        input_data (list): The lines from the output containing the input data
    """
    for n, line in enumerate(data):
        if "Input Data:" in line:
            for m, other_line in enumerate(data[n+1:], start=n+1):
                if other_line.lower() == 'end\n':
                    input_data = data[n+2:m+1]
                    return input_data


def parse_output(data):
    """Crete various objects from the output data by calling other modules

    Args:
        data (list): The SCALE output data

    Returns:
        None
    """
    tally_data = scale_tallies.get_tally_data(data)
    gv.rundate, gv.runtime = get_runtime(data)
    scale_tallies.create_tallies(tally_data)
    scale_tallies.Tally.scale_results()
    mixture_data = mixtures.get_mixture_data(data)
    mixtures.create_mixtures(mixture_data)
    gv.scale_input = get_input(data)


def main(filename, scaling_factor=1):
    """Provide an entry to the SCALE converter and call the other functions in this module

    Args:
        filename (str): The SCALE output file path
        scaling_factor (float): The scaling factor to multiply the results by

    Returns:
        None
    """
    gv.filename = filename
    gv.scaling_factor = scaling_factor
    output_data = read_file(filename)
    parse_output(output_data)
    scale_html_writer.main(filename)
