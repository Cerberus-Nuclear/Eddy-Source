#!/usr/bin/env python3
# Peter Evans
# Cerberus Nuclear Ltd

"""This module contains all the code relating to SCALE mixtures."""
# import from standard library:
import re


class Mixture:
    """Each mixture in the SCALE case is represented by a Mixture object"""
    def __init__(self, data):
        self.data = data
        self.number = data[0].split()[2]
        self.density = data[0].split()[5]
        try:
            self.temperature = data[0].split()[8] + 'K'
        except IndexError:
            self.temperature = "Not given in output file"
        self.isotopes = {}
        # There seem to be two formats of mixture table; if multigroup energies are used the table has a
        # 'nucmix' column, if continuous energies are used it does not.
        if 'nucmix' in data[1].split():
            try:
                self.isotopes = self.get_isotope_data_multigroup_format()
            except ValueError:
                print(ValueError)
        else:
            try:
                self.isotopes = self.get_isotope_data_continuous_format()
            except ValueError:
                print(ValueError)


    def get_isotope_data_multigroup_format(self):
        """Create a dictionary with the relevant parts of the mixture table
        Args:
            self: The Mixture object
        Returns:
            isotopes (dict): a dictionary where each entry is a name:nuclide pair, where
                            nuclide is a dict containing the relevant data about that nuclide
        """
        isotopes = {}
        headings = self.data[1].split('   ') # need 2 spaces so 'wgt. frac' is not split
        headings = [x.strip() for x in headings if x]  # remove empty strings
        for line in self.data[2:]:
            if line == '\n' or line == '':
                continue
            else:
                nuclide_index = headings.index("nuclide")
                nuclide = int(line.split()[nuclide_index])
                isotopes[nuclide] = {}
                isotopes[nuclide]['nuclide'] = nuclide
                isotopes[nuclide]['atom-density'] = float(line.split()[headings.index('atom-dens.')])
                isotopes[nuclide]['weight fraction'] = float(line.split()[headings.index('wgt. frac.')])
                isotopes[nuclide]['z-number'] = int(line.split()[headings.index('za')])
                isotopes[nuclide]['atomic weight'] = float(line.split()[headings.index('awt')])
                isotopes[nuclide]['title'] = line.split()[headings.index('nuclide title')].capitalize()
                isotopes[nuclide]['temperature'] = float(line.split()[headings.index('temp')])
        return isotopes


    def get_isotope_data_continuous_format(self):
        """Create a dictionary with the relevant parts of the mixture table
        Args:
            self: The Mixture object
        Returns:
            isotopes (dict): a dictionary where each entry is a name:nuclide pair, where
                            nuclide is a dict containing the relevant data about that nuclide
        """
        isotopes = {}
        headings = self.data[1].split('   ') # need 2 spaces so 'wgt. frac' is not split
        headings = [x.strip() for x in headings if x]  # remove empty strings
        for line in self.data[2:]:
            if line == '\n' or line == '':
                continue
            else:
                nuclide_index = headings.index("nuclide")
                nuclide = int(line.split()[nuclide_index])
                isotopes[nuclide] = {}
                isotopes[nuclide]['nuclide'] = nuclide
                isotopes[nuclide]['atom-density'] = float(line.split()[headings.index('atom-dens.')])
                isotopes[nuclide]['weight fraction'] = float(line.split()[headings.index('wgt. frac.')])
                isotopes[nuclide]['z-number'] = int(line.split()[headings.index('za')])
                isotopes[nuclide]['atomic weight'] = float(line.split()[headings.index('awt')])
                isotopes[nuclide]['title'] = line.split()[headings.index('title')].capitalize()
                isotopes[nuclide]['temperature'] = float(line.split()[headings.index('temp')])
        return isotopes


def get_mixture_data(output_data):
    """Get the part of the SCALE output concerning mixtures

    Args:
        output_data (list): The SCALE output data

    Returns:
        The lines from output_data concerning mixtures
    """
    pattern_mix = re.compile(r'^\s*mixing table\s*')
    for n, line in enumerate(output_data):
        if pattern_mix.match(line):
            for m, other_line in enumerate(output_data[n+1:], start=n+1):
                if "Cross section" in other_line or "*****" in other_line:
                    return output_data[n:m+1]


def create_mixtures(mix_data):
    """Create Mixture objects from the SCALE output data

    Args:
        mix_data (list): The lines from output_data concerning mixtures

    Returns:
        None, but creates Mixture objects
    """
    for n, line in enumerate(mix_data):
        if "mixture = " in line:
            for m, other_line in enumerate(mix_data[n+1:], start=n+1):
                if "mixture" in other_line or "Cross section" in other_line or "*****" in other_line:
                    mix = mix_data[n:m]
                    Mixture(mix)
                    break

