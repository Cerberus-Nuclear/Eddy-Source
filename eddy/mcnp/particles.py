#!/usr/bin/env python3
# Peter Evans
# Cerberus Nuclear Ltd

""" This module holds the code related to particle data. """

# Standard library imports
import re
# local imports
from . import global_variables as gv


class Particle:
    """
    This class exists to hold the data on particle populations, creation and loss.
    """

    def __init__(self, creation_data, loss_data, total_data, particle_type):
        gv.particle_list.append(self)
        self.attributes = []
        self.particle_type = particle_type
        for item in creation_data:
            name = ' '.join(item.split()) + ' creation'
            name = name.title()
            self.__dict__[name] = creation_data[item]
            self.attributes.append(name)
        for item in loss_data:
            name = ' '.join(item.split()) + ' loss'
            name = name.title()
            self.__dict__[name] = loss_data[item]
            self.attributes.append(name)
        for item in total_data:
            name = ' '.join(item.split()).title()
            self.__dict__[name] = total_data[item]
            self.attributes.append(name)

    def describe_object(self):
        """ Print the attributes of the particle to the terminal."""
        print()
        print(f"Printing {self.particle_type} Data...".upper())
        for item in self.attributes:
            print(f"{item}: {self.__dict__[item]}")
        print()

# ----------------------------------------------------------------------------------
# NEUTRONS -------------------------------------------------------------------------
# ----------------------------------------------------------------------------------


def get_neutrons(output_data):
    """Find the mcnp neutron data then create a Particle object with that data

    Args:
        output_data (list): The MCNP output

    Returns:
        None
    """
    neutron_data = find_mcnp_neutron_data(output_data)
    if neutron_data:
        creation_data, loss_data, total_data = sort_mcnp_neutron_data(neutron_data)
        Particle(creation_data, loss_data, total_data, 'neutron')


def find_mcnp_neutron_data(output_data):
    """Find the neutron data in the mcnp output.

    Args:
        output_data (list): The MCNP output

    Returns:
        neutron_data (list): The part of the MCNP output with the neutron particle data
    """
    PATTERN_run_terminated = re.compile(r'^\+\s+\d\d/\d\d/\d\d(.+)')
    PATTERN_neutron = re.compile(r'\sneutron\screation\s+tracks.+')
    neutron_data = None
    # Find the neutron data and save to a list
    for n, line in enumerate(output_data):
        if PATTERN_run_terminated.match(line):
            terminated = n
            for m, new_line in enumerate(output_data[terminated:], start=terminated):
                if PATTERN_neutron.match(new_line):
                    neutron_data = output_data[m:m+28]
                    break
    return neutron_data


def sort_mcnp_neutron_data(data):
    """Separate out the neutron data into creation, loss, and total data,
    then split each by indices and put into a dictionary

    Args:
        data (list): The part of the MCNP output with the neutron particle data

    Returns:
        a tuple containing
            creation_dict: The neutron creation data,
            loss_dict: The neutron loss data,
            total_dict: The total neutron data,
    """
    indices = [0, 18, 27, 41, 55]   # These have been put in based on inspection of an example output file
    creation_dict = {}
    loss_dict = {}
    for line_num in range(3, 22):
        # Separate neutron creation data
        creation = data[line_num][:55]
        creation = [creation[indices[i]:indices[i+1]].strip() for i in range(len(indices)-1)]
        creation_dict[creation[0]] = {'tracks': int(creation[1]),
                                      'weight': float(creation[2]),
                                      'energy': float(creation[3]),
                                      }
        # Separate neutron loss data
        loss = data[line_num][64:]
        loss = [loss[indices[i]:indices[i+1]].strip() for i in range(len(indices)-1)]
        loss_dict[loss[0]] = {'tracks': int(loss[1]),
                              'weight': float(loss[2]),
                              'energy': float(loss[3]),
                              }
    total_dict = {}
    for line_num in range(23, 27):
        total = data[line_num][:42].strip(), data[line_num][42:53].strip()
        total_dict[total[0]] = total[1]
    return creation_dict, loss_dict, total_dict


# ----------------------------------------------------------------------------------
# PHOTONS --------------------------------------------------------------------------
# ----------------------------------------------------------------------------------


def get_photons(output_data):
    """Find the mcnp photon data then create a Particle object with that data

    Args:
        output_data (list): The MCNP output

    Returns:
        None
    """
    photon_data = find_mcnp_photon_data(output_data)
    if photon_data:
        creation_data, loss_data, total_data = sort_mcnp_photon_data(photon_data)
        Particle(creation_data, loss_data, total_data, 'photon')


def find_mcnp_photon_data(output_data):
    """Find the photon data in the mcnp output

    Args:
        output_data (list): The MCNP output

    Returns:
        photon_data (list): The part of the MCNP output with the photon particle data
    """
    PATTERN_run_terminated = re.compile(r'^\+\s+\d\d/\d\d/\d\d(.+)')
    PATTERN_photon = re.compile(r'\sphoton\screation\s+tracks.+')
    photon_data = None
    for n, line in enumerate(output_data):
        if PATTERN_run_terminated.match(line):
            terminated = n
            for m, new_line in enumerate(output_data[terminated:], start=terminated):
                if PATTERN_photon.match(new_line):
                    photon_data = output_data[m:m+33]
                    break
    return photon_data


def sort_mcnp_photon_data(photon_data):
    """Separate out the photon data into creation, loss, and total data,
    then split each by indices and put into a dictionary

    Args:
        photon_data (list): The part of the MCNP output with the photon particle data

    Returns:
        a tuple containing
            creation_dict: The photon creation data,
            loss_dict: The photon loss data,
            total_dict: The photon neutron data,
    """
    indices = [0, 18, 27, 41, 55]
    creation_dict = {}
    loss_dict = {}
    for line_num in range(3, 27):
        # Separate photon creation data
        creation = photon_data[line_num][:55]
        creation = [creation[indices[i]:indices[i+1]].strip() for i in range(len(indices)-1)]
        creation_dict[creation[0]] = {'tracks': int(creation[1]),
                                      'weight': float(creation[2]),
                                      'energy': float(creation[3]),
                                      }
        # Separate photon loss data
        loss = photon_data[line_num][64:]
        loss = [loss[indices[i]:indices[i+1]].strip() for i in range(len(indices)-1)]
        try:
            loss_dict[loss[0]] = {'tracks': int(loss[1]), 'weight': float(loss[2]), 'energy': float(loss[3])}
        except ValueError:
            # There are more creation lines than loss lines
            pass

    total_dict = {}
    for line_num in range(28, 32):
        total = photon_data[line_num][:42].strip(), photon_data[line_num][42:53].strip()
        total_dict[total[0]] = total[1]
    # for item in total_dict: print(item, total_dict[item])
    return creation_dict, loss_dict, total_dict

# ----------------------------------------------------------------------------------
# ELECTRONS ------------------------------------------------------------------------
# ----------------------------------------------------------------------------------


def get_electrons(output_data):
    """Find the mcnp electron data then create a Particle object with that data

    Args:
        output_data (list): The MCNP output

    Returns:
        None
    """
    electron_data = find_mcnp_electron_data(output_data)
    if electron_data:
        creation_data, loss_data, total_data = sort_mcnp_electron_data(electron_data)
        Particle(creation_data, loss_data, total_data, 'electron')


def find_mcnp_electron_data(output_data):
    """Find the electron data in the mcnp output

    Args:
        output_data (list): The MCNP output

    Returns:
        electron_data (list): The part of the MCNP output with the electron particle data
    """
    PATTERN_run_terminated = re.compile(r'^\+\s+\d\d/\d\d/\d\d(.+)')
    PATTERN_electron = re.compile(r'\selectron\screation\s+tracks.+')
    electron_data = None
    for n, line in enumerate(output_data):
        if PATTERN_run_terminated.match(line):
            terminated = n
            for m, new_line in enumerate(output_data[terminated:], start=terminated):
                if PATTERN_electron.match(new_line):
                    electron_data = output_data[m:m+24]
                    break
    return electron_data


def sort_mcnp_electron_data(electron_data):
    """Separate out the electron data into creation, loss, and total data,
    then split each by indices and put into a dictionary

    Args:
        electron_data (list): The part of the MCNP output with the electron particle data

    Returns:
        a tuple containing
            creation_dict: The electron creation data,
            loss_dict: The electron loss data,
            total_dict: The electron neutron data,
    """
    indices = [0, 18, 27, 41, 55]
    creation_dict = {}
    loss_dict = {}
    for line_num in range(3, 18):
        # Separate electron creation data
        creation = electron_data[line_num][:55]
        creation = [creation[indices[i]:indices[i+1]].strip() for i in range(len(indices)-1)]
        creation_dict[creation[0]] = {'tracks': int(creation[1]),
                                      'weight': float(creation[2]),
                                      'energy': float(creation[3]),
                                      }
        # Separate electron loss data
        loss = electron_data[line_num][64:]
        loss = [loss[indices[i]:indices[i+1]].strip() for i in range(len(indices)-1)]
        try:
            loss_dict[loss[0]] = {'tracks': int(loss[1]), 'weight': float(loss[2]), 'energy': float(loss[3])}
        except ValueError:
            pass  # ignore single empty entry

    total_dict = {}
    for line_num in range(19, 23):
        total = electron_data[line_num][:42].strip(), electron_data[line_num][42:53].strip()
        total_dict[total[0]] = total[1]
    return creation_dict, loss_dict, total_dict
