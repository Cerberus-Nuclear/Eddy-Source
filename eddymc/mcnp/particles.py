#!/usr/bin/env python3
# Peter Evans
# Cerberus Nuclear Ltd

""" This module holds the code related to particle data. """

# Standard library imports


class Particle:
    """
    This class exists to hold the data on particle populations, creation and loss.
    """

    def __init__(self, creation_data, loss_data, total_data, particle_type):
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

    def __repr__(self):
        """ Print the attributes of the particle to the terminal."""
        print()
        print(f"Printing {self.particle_type} Data...".upper())
        for item in self.attributes:
            print(f"{item}: {self.__dict__[item]}")
        print()

