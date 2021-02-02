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
# local imports


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
