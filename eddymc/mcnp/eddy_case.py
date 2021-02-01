#!/usr/bin/env python3
# Peter Evans
# Cerberus Nuclear Ltd

"""This module contains the EddyCase class, which holds all the data relevant to a particular run.

"""

import re


class EddyCase:
    def __init__(self, filepath, scaling_factor, file, crit_case=False):
        self.filepath = filepath
        self.name = filepath.replace('\\', '/').split('/')[-1]
        self.scaling_factor = scaling_factor
        self.file = file
        self.crit_case = crit_case

        # start parsing output:
        self.rundate, self.runtime = self.get_date_time()
        self.ctme, self.nps = self.get_runtime()
        self.mcnp_input = self.get_input()
        self.parameters = self.get_parameters()
        self.lost_particles = self.check_lost_particles()

    def __repr__(self):
        return (f"This Eddy case considers file {self.name}\n"
                f"from {self.filename}\n"
                f"The scaling factor is {self.scaling_factor}\n"
                f"Criticality case: {self.crit_case}\n")

    def get_date_time(self):
        """Get the date and time that the mcnp case was run

        Returns:
            date_time (dict): the date and time the case was run
        """
        for line in self.file:
            if line.startswith('1mcnp'):
                time = line.split()[5]
                date = line.split()[4]
                date = date.split('/')
                d = date[1]
                m = date[0]
                y = '20' + date[2]
                date_time = {'date': f"{y}/{m}/{d}", 'time': time}
                rundate = f"{y}/{m}/{d}"
                runtime = time
                return rundate, runtime

    def get_runtime(self):
        """Get the time or number of particles the MCNP case was run for

        Returns:
            ctme (str): The number of minutes the code ran for, or None if not found
            nps (str): the number of particles run, or None if not found
        """
        ctme = None
        nps = None
        pattern_nps = re.compile(r'^\s{6,}\d+-\s{7}(nps|NPS)\s+.+')
        pattern_ctme = re.compile(r'^\s{6,}\d+-\s{7}(ctme|CTME)\s+.+')
        for line in self.file:
            if pattern_ctme.match(line):
                ctme = line.split()[2]
            if pattern_nps.match(line):
                nps = line.split()[2]
        return ctme, nps

    def get_input(self):
        """Extract the MCNP input deck from the MCNP output file

        Returns:
            mcnp_input (list): The MCNP input deck
        """
        pattern_input = re.compile(r'^\s{6,}\d+-\s{7}(.*)')
        mcnp_input = []
        for line in self.file:
            match = pattern_input.match(line)
            if match:
                mcnp_input.append(match.group(1).strip('\n'))
        return mcnp_input

    def get_parameters(self):
        """Get any parameters used in the input file.
        NOTE: This is only useful if MCNP is run using the Cerberus
        package CYCLONE; non-cyclone users can ignore this function.

        Returns:
            variables (dict): All the parameters used by this case
        """
        variables = {}
        for n, line in enumerate(self.mcnp_input):
            if "USING THE FOLLOWING VARIABLES" in line:
                for m, other_line in enumerate(self.mcnp_input[n+1:], start=n+1):
                    if '=' not in other_line:
                        break
                    variable = other_line.split()[1]
                    value = other_line.split()[3]
                    variables[variable] = float(value)
                break
        return variables

    def check_lost_particles(self):
        """Check whether the run was terminated because 10 or more particles got lost

        Returns:
            True if run terminated due to lost particles, otherwise False
        """
        for line in self.file:
            if "run terminated because" in line and "particles got lost" in line:
                return True
        return False
