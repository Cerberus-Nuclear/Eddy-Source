#!/usr/bin/env python3
# Peter Evans
# Cerberus Nuclear Ltd

""" MCNP HTML Output Writer
Usage: python3 mcnp_reader.py [-o mcnp_filename.out] [-n scaling_factor]

This programme takes an MCNP output file and creates a HTML summary of the results.
If run from the command line, it can take two optional arguments; the
mcnp filename and a normalisation factor. if the mcnp filename is not supplied, a tkinter
window will open to allow a file to be selected. If a normalisation factor is not applied,
it will be assumed to be 1.

"""

# Imports from standard library
import re
# Local imports
from . import particles, mcnp_html_writer, tallies, global_variables as gv, cells


def read_file(filename):
    """Read in the MCNP output file.

    Args:
        filename (str): The name (and location) of the MCNP .out file

    Returns:
        data (list): The lines from the output file
    """
    with open(filename, 'r') as file:
        data = file.readlines()
    return data


def parse_output(output_data):
    """Send the MCNP data to functions in various modules, which extract the relevant data for themselves

    Args:
        output_data (list): The MCNP output data

    Returns:
        None
    """
    gv.date_time = get_date_time(output_data)
    gv.ctme, gv.nps = get_runtime(output_data)
    gv.mcnp_input = get_input(output_data)
    gv.parameters = get_parameters(gv.mcnp_input)
    cell_data = cells.find_cells(output_data)
    neutron_populations = cells.get_particle_populations(output_data, 'neutron')
    photon_populations = cells.get_particle_populations(output_data, 'photon')
    electron_populations = cells.get_particle_populations(output_data, 'electron')
    cells.create_cell_objects(cell_data)
    for cell in gv.cell_list:
        cell.assign_populations(neutron_populations, photon_populations, electron_populations)
    gv.fatal_errors = get_fatal_errors(output_data)
    gv.warnings = get_warnings(output_data)
    gv.comments = get_comments(output_data)
    gv.duplicate_surfaces = get_duplicate_surfaces(output_data)
    particles.get_neutrons(output_data)
    particles.get_photons(output_data)
    particles.get_electrons(output_data)
    if gv.crit_case:
        gv.k_effective = get_k_eff(output_data)
        gv.cycles = get_active_cycles(output_data)
    else:
        tallies.get_tallies(output_data)
        if gv.scaling_factor != 1:
            for tally in gv.tally_list:
                tally.normalise_data()


def get_date_time(output_data):
    """Get the date and time that the mcnp case was run

    Args:
        output_data (list): The MCNP output file

    Returns:
        date_time (dict): the date and time the case was run
    """
    for line in output_data:
        if line.startswith('1mcnp'):
            time = line.split()[5]
            date = line.split()[4]
            date = date.split('/')
            d = date[1]
            m = date[0]
            y = '20' + date[2]
            date_time = {'date': f"{y}/{m}/{d}", 'time': time}
            gv.rundate = f"{y}/{m}/{d}"
            gv.runtime = time
            return date_time


def get_runtime(output_data):
    """Get the time or number of particles the MCNP case was run for

    Args:
        output_data (list): The MCNP output file

    Returns:
        ctme (str): The number of minutes the code ran for, or None if not found
        nps (str): the number of particles run, or None if not found
    """
    ctme = None
    nps = None
    pattern_nps = re.compile(r'^\s{6,}\d+-\s{7}(nps|NPS)\s+.+')
    pattern_ctme = re.compile(r'^\s{6,}\d+-\s{7}(ctme|CTME)\s+.+')
    for line in output_data:
        if pattern_ctme.match(line):
            ctme = line.split()[2]
        if pattern_nps.match(line):
            nps = line.split()[2]
    return ctme, nps


def get_input(output_data):
    """Extract the MCNP input deck from the MCNP output file

    Args:
        output_data (list): The MCNP output data

    Returns:
        mcnp_input (list): The MCNP input deck
    """
    pattern_input = re.compile(r'^\s{6,}\d+-\s{7}(.*)')
    mcnp_input = []
    for line in output_data:
        match = pattern_input.match(line)
        if match:
            mcnp_input.append(match.group(1).strip('\n'))
    return mcnp_input


def get_parameters(input_data):
    """Get any parameters used in the input file.
    NOTE: This is only useful if MCNP is run using the Cerberus
    package CYCLONE; non-cyclone users can ignore this function.

    Args:
        input_data (list): The MCNP input file

    Returns:
        variables (dict): All the parameters used by this case
    """
    variables = {}
    for n, line in enumerate(input_data):
        if "USING THE FOLLOWING VARIABLES" in line:
            for m, other_line in enumerate(input_data[n+1:], start=n+1):
                if '=' not in other_line:
                    break
                variable = other_line.split()[1]
                value = other_line.split()[3]
                variables[variable] = float(value)
            break
    return variables


def get_fatal_errors(output_data):
    """Find the warnings in the MCNP output data

    Args:
        output_data (list): The MCNP output data

    Returns:
        fatal_errors, a list of the fatal error messages
    """
    fatal_errors = []
    for line in output_data:
        if "fatal error." in line:
            message = line[14:].strip().capitalize()
            fatal_errors.append(message)
    return fatal_errors


def get_warnings(output_data):
    """Find the warnings in the MCNP output data

    Args:
        output_data (list): The MCNP output data

    Returns:
        warnings, a list of the warning messages
    """
    warnings = []
    PATTERN_warnings = re.compile(r'warning')
    for line in output_data:
        if PATTERN_warnings.search(line):
            if "warning message so far" not in line and "warning messages so far" not in line:
                warning = line[10:].strip().capitalize()
                if warning not in warnings:
                    warnings.append(warning)
    return warnings


def get_comments(output_data):
    """Find the comments in the MCNP output file.

    Args:
        output_data (list): The mcnp output

    Returns:
        comments, a list of the comments
    """
    PATTERN_comments = re.compile(r'comment\.\s+[A-Za-z0-9].+')    # Ignores blank comment lines
    comments = []
    for line in output_data:
        if PATTERN_comments.search(line):
            comment = line[10:].strip().capitalize()
            comments.append(comment)
    return comments


def get_duplicate_surfaces(output_data):
    """Find all the duplicate surface messages in the mcnp output

    Args:
        output_data (list): The mcnp output

    Returns:
        duplicate_surfaces, a list of the duplicate surfaces
    """
    duplicate_surfaces = []
    PATTERN_duplicates = re.compile(r'\ssurface\s+\d+.+and surface.+are the same.+')
    for line in output_data:
        if PATTERN_duplicates.match(line):
            if line.strip().capitalize() not in duplicate_surfaces:
                duplicate_surfaces.append(line.strip().capitalize())
    return duplicate_surfaces


def get_k_eff(output_data):
    """Search the output data for the section concerning k-effective, and create a single dictionary holding the data

    Args:
        output_data (list): The MCNP output

    Returns:
         k_eff (dict): the k-effective values for the first half, second half and total run
    """
    PATTERN_k_eff = re.compile(r'^\s*problem\s+keff.+')
    k_eff = {}
    for num, line in enumerate(output_data):
        if PATTERN_k_eff.match(line):
            first_half = re.split(r'\s{2,}', output_data[num+2].strip())
            k_eff['first half k_eff'] = float(first_half[1])
            k_eff['first half stdev'] = float(first_half[2])

            second_half = re.split(r'\s{2,}', output_data[num+3].strip())
            k_eff['second half k_eff'] = float(second_half[1])
            k_eff['second half stdev'] = float(second_half[2])

            final_result = re.split(r'\s{2,}', output_data[num+4].strip())
            k_eff['final k_eff'] = float(final_result[1])
            k_eff['final stdev'] = float(final_result[2])
    return k_eff


def get_active_cycles(output_data):
    """For a crit case, find the number of active and inactive cycles

    Args:
        output_data (list): the output file

    Returns:
        None, but writes cycles (dict) to gv.cycles

    """
    cycles = {}
    for line in output_data:
        if "the minimum estimated standard deviation for the col/abs/tl keff estimator occurs with" in line:
            cycles["inactive"] = int(line.split()[12])
            cycles["active"] = int(line.split()[16])
    return cycles


def main(filename, scaling_factor=1, crit_case=False):
    """ Provide entry point to this module and call the other parts of the script

    Args:
        filename (str): the mcnp output file
        scaling_factor (float): A number which all results will be multiplied by
        crit_case (bool): True if criticality case, False (default) for shielding case

    Returns:
        None
    """
    gv.scaling_factor = scaling_factor
    gv.crit_case = crit_case
    output_data = read_file(filename)
    parse_output(output_data)
    mcnp_html_writer.main(filename)
