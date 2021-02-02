#!/usr/bin/env python3
# Peter Evans
# Cerberus Nuclear Ltd

"""This module contains the EddySCALECase class, which holds all the data relevant to a particular SCALE run.

"""

import re
from .scale_tallies import Tally
from .mixtures import Mixture


class EddySCALECase:
    def __init__(self, filepath, file, scaling_factor=1):
        self.filepath = filepath
        self.name = filepath.replace('\\', '/').split('/')[-1]
        self.file = file
        self.scaling_factor = scaling_factor

        # parse output
        self.scale_input = self.get_input()
        self.rundate, self.runtime = self.get_runtime()

        # Tallies
        self.tally_data = self.get_tally_data()
        self.tally_list = self.create_tallies()
        self.scale_tally_results()

        # Mixtures
        mixture_data = self.get_mixture_data()
        self.mixture_list = self.create_mixtures(mixture_data)

    def __repr__(self):
        return (f"This Eddy SCALE case considers file {self.name}\n"
                f"from {self.filepath}\n"
                f"The scaling factor is {self.scaling_factor}\n")

    def get_input(self):
        """Get the SCALE input deck from the output file

        Returns:
            list: The lines from the output containing the input data
        """
        for n, line in enumerate(self.file):
            if "Input Data:" in line:
                for m, other_line in enumerate(self.file[n + 1:], start=n + 1):
                    if other_line.lower() == 'end\n':
                        input_data = self.file[n + 2:m + 1]
                        return input_data

    def get_runtime(self):
        """Find the date and time that the SCALE case was run

        Returns:
            A tuple containing
                rundate (str): the date the case was run
                runtime (str): the time the case was run
        """
        for line in self.file:
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

    def get_tally_data(self):
        """Find the parts of the SCALE output with the tally data

        Returns:
            list: The lines from the SCALE output containing the tally data
        """
        for n, line in enumerate(self.file):
            if "Final Tally Results Summary" in line:
                for m, other_line in enumerate(self.file[n + 1:], start=n + 1):
                    if "Total Monaco cpu time for this problem" in other_line:
                        tally_data = self.file[n:m]
                        return tally_data
        # If the function has not returned the data, there is a problem
        raise Exception("Tally data incomplete.")

    def create_tallies(self):
        """Create Tally objects using the output data

        Returns:
            list: A list of Tally objects
        """
        tally_list = []
        for n, line in enumerate(self.tally_data):
            if "Region Tally" in line or "Point Detector" in line:
                tally_info = self.tally_data[n:n + 7]
                tally_list.append(Tally(tally_info))
        return tally_list

    def scale_tally_results(self):
        """Scale the results of each tally by the scaling factor"""
        if self.scaling_factor != 1:
            for tally in self.tally_list:
                tally.scale_results(self.scaling_factor)

    def get_mixture_data(self):
        """Get the part of the SCALE output concerning mixtures

        Returns:
            The lines from output_data concerning mixtures
        """
        pattern_mix = re.compile(r'^\s*mixing table\s*')
        for n, line in enumerate(self.file):
            if pattern_mix.match(line):
                for m, other_line in enumerate(self.file[n + 1:], start=n + 1):
                    if "Cross section" in other_line or "*****" in other_line:
                        return self.file[n:m]
        return None

    @staticmethod
    def create_mixtures(mix_data):
        """Create Mixture objects from the SCALE output data

        Args:
            mix_data (list): The lines from output_data concerning mixtures

        Returns:
            list: A list of Mixture objects
        """
        mixture_list = []
        for n, line in enumerate(mix_data):
            if "mixture = " in line:
                for m, other_line in enumerate(mix_data[n+1:], start=n+1):
                    if "mixture" in other_line or "Cross section" in other_line or "*****" in other_line:
                        mix = mix_data[n:m]
                        mixture_list.append(Mixture(mix))
                        break
        return mixture_list
