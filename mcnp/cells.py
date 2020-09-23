#!/usr/bin/python3
# Peter Evans
# Cerberus Nuclear Ltd
# November 2019

"""
    This module holds all the code related to cells, including the Cells class,
    and the functions which find the cell data in the mcnp output, extract the cell
    section of that data, and send it to the Cell class to create the Cell objects.

    It also contains the code to find the neutron, photon and electron population data,
    which is assigned to each cell object as they are created.
"""
# imports from standard library
import re
from pathlib import Path
# local imports
from . import global_variables as gv


class Cell:
    """ This class holds the attributes and methods for Cell objects."""
    # pylint: disable=too-many-instance-attributes
    # MCNP cells have a lot of attributes

    def __init__(self, **info):
        self.cell_number = info['cell_number']
        self.material_number = info['material_number']
        self.atom_density = info['atom_density']
        self.gram_density = info['gram_density']
        self.volume = float(info['volume'])
        self.mass = float(info['mass'])
        self.neutron_importance = info['neutron_importance']
        self.photon_importance = info['photon_importance']
        self.electron_importance = info['electron_importance']
        gv.cell_list.append(self)

    def assign_populations(self, neutron_pop=None, photon_pop=None, electron_pop=None):
        """Assign neutron, photon and electron population data to each cell.

        Args:
            neutron_pop (list): The neutron population section of the MCNP output
            photon_pop (list): The photon population section of the MCNP output
            electron_pop (list): The electron population section of the MCNP output

        Returns:
            None. The data is assigned to the cell objects as various new attributes.
        """
        # Assign neutron population data to cell
        if neutron_pop:
            for line in neutron_pop[6:-2]:
                line = line.split()
                num = line[1]
                if num == self.cell_number:
                    self.neutron_tracks_entering = line[2]
                    self.neutron_population = line[3]
                    self.neutron_collisions = line[4]
        # Assign photon population data to cell
        if photon_pop:
            for line in photon_pop[6:-2]:
                line = line.split()
                num = line[1]
                if num == self.cell_number:
                    self.photon_tracks_entering = line[2]
                    self.photon_population = line[3]
                    self.photon_collisions = line[4]
        # Assign electron population data to cell
        if electron_pop:
            for line in electron_pop[6:-2]:
                line = line.split()
                num = line[1]
                if num == self.cell_number:
                    self.electron_tracks_entering = line[2]
                    self.electron_population = line[3]
                    self.electron_collisions = line[4]

    def describe_object(self):
        """Print a description of the cell object to the terminal (for debugging purposes)

        Args:
            self, the cell object

        Returns:
            None
        """
        print(f"Cell number: {self.cell_number}")
        print(f"Cell material: {self.material_number}")
        print(f"Cell density: {self.gram_density} g/cm3")
        print(f"Cell volume: {self.volume} cm3")
        # The following attributes are particle-dependent, and so may or may not exist for any one mcnp case
        # pylint: disable=multiple-statements
        try:
            print(f"Neutron Importance: {self.neutron_importance}")
        except AttributeError:
            pass
        try:
            print(f"Photon Importance: {self.photon_importance}")
        except AttributeError:
            pass
        try:
            print(f"Electron Importance: {self.electron_importance}")
        except AttributeError:
            pass
        print()


############################################################
#  End of Cell class                                       #
############################################################


def find_cells(output_data):
    """Loop through the mcnp output to find the section containing the cell data

    Args:
        output_data (list): the mcnp output

    Returns:
        cell_section (list): The section of the output containing the cell data
    """
    PATTERN_cells_start = re.compile(r'1cells')
    PATTERN_cells_ends = re.compile(r' total')
    cell_section = []
    for line in output_data:
        if PATTERN_cells_start.match(line):
            cell_start_line = output_data.index(line)
            for row in output_data[cell_start_line:]:
                cell_section.append(row.strip('\n'))
                if PATTERN_cells_ends.match(row):
                    break
            break
    return cell_section


def create_cell_objects(data):
    """Take the cell data and create objects of the Cell class

    Args:
        data (list): a list of strings containing the cell part of the mcnp output

    Returns:
        None: creates Cell objects
    """
    header = (data[2].split())
    PATTERN_cell = re.compile(r'\s+\d+\s.+')
    for line in data[1:]:
        if PATTERN_cell.match(line):
            info = line.split()
            neutron_importance = get_particle_importance(header, info, 'neutron')
            photon_importance = get_particle_importance(header, info, 'photon')
            electron_importance = get_particle_importance(header, info, 'electron')
            Cell(
                cell_number=info[1],
                material_number=info[2],
                atom_density=info[3],
                gram_density=info[4],
                volume=info[5],
                mass=info[6],
                neutron_importance=neutron_importance,
                photon_importance=photon_importance,
                electron_importance=electron_importance
                )


def get_particle_importance(header, data, particle):
    """For a particular particle type, determine the importance of that particle.
    This function is called for each cell as part of its creation.

    Args:
        header (list): the particle population table header
        data (list): the section of the mcnp output with the cell data
        particle (str): either 'neutron', 'photon' or 'electron'

    Returns:
         particle_importance (str): the particle importance, or 0.
    """
    if particle in header:
        particle_importance = data[header.index(particle) + 6]
    else:
        particle_importance = '0'
    return particle_importance


def get_particle_populations(output_data, particle):
    """Find and return the section of the output data concerning populations of a particular particle

    Args:
        output_data (list): the mcnp output
        particle (str): either 'photon', 'neutron' or 'electron'

    Returns:
        particle_populations (list): the lines from the output file concerning populations of that particle
    """
    PATTERN_run_terminated = re.compile(r'^\+\s+\d\d/\d\d/\d\d(.+)')
    PATTERN_particle_populations = re.compile(fr'^1{particle}\s+activity\sin\seach\scell.+')
    PATTERN_end_populations = re.compile(r'\s+total.+')
    particle_populations = None
    for n, line in enumerate(output_data):
        if PATTERN_run_terminated.match(line):
            terminated = n
            for m, new_line in enumerate(output_data[terminated:], start=terminated):
                if PATTERN_particle_populations.match(new_line):
                    for p in range(m, len(output_data)):
                        if PATTERN_end_populations.match(output_data[p]):
                            particle_populations = output_data[m:p + 1]
                            return particle_populations
    return None
