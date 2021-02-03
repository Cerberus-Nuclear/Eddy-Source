#!/usr/bin/env python3
# Peter Evans
# Cerberus Nuclear Ltd

"""This module contains the EddyMCNPCase class, which holds all the data relevant to a particular MCNP run.

"""

import re
from .cells import Cell
from .particles import Particle
from .tallies import F2Tally, F4Tally, F5Tally, F6Tally


class EddyMCNPCase:
    """ An EddyCase object holds all the essential data for a single Eddy run,
    and its __init__ method is responsible for calling the other classes that
    Eddy uses.
    """
    def __init__(self, filepath, scaling_factor, file, crit_case=False):
        """ Most of the work done by eddy is handled within the __init__ function;
        it calls all the instance methods that get information from the mcnp output file,
        and puts them into attributes of the EddyCase object.

        Args:
            filepath (str): The path to the mcnp output file
            scaling_factor (float): A number to multiply the tally results by
            file (list): The contents of the mcnp output file
            crit_case (bool): True if crit case, otherwise false
        """

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
        self.fatal_errors = self.get_fatal_errors()
        self.warnings = self.get_warnings()
        self.comments = self.get_comments()
        self.duplicate_surfaces = self.get_duplicate_surfaces()
        if self.crit_case is True:
            self.k_effective = self.get_k_eff()
            self.cycles = self.get_active_cycles()
        else:
            self.k_effective = None
            self.cycles = None

        # Cells
        self.cell_data = self.get_cell_data()
        self.neutron_populations = self.get_particle_populations('neutron')
        self.photon_populations = self.get_particle_populations('photon')
        self.electron_populations = self.get_particle_populations('electron')
        self.cell_list = self.create_cells()
        for cell in self.cell_list:
            cell.assign_populations(
                self.neutron_populations,
                self.photon_populations,
                self.electron_populations,
            )

        # Particles
        self.particle_list = []
        for particle_type in ['neutron', 'photon', 'electron']:
            particle_data = self.find_mcnp_particle_data(particle_type)
            if particle_data:
                particle = self.create_particle(particle_type, particle_data)
                self.particle_list.append(particle)

        # Tallies
        # initialise empty variables
        self.tally_list = []   # list of all tallies
        self.f_types = []
        self.F2_tallies = {'neutrons': [], 'photons': [], 'electrons': []}
        self.F4_tallies = {'neutrons': [], 'photons': [], 'electrons': []}
        self.F5_tallies = {'neutrons': [], 'photons': [], 'electrons': []}
        self.F6_tallies = {'neutrons': [], 'photons': [], 'electrons': [], 'Collision Heating': []}
        # get tallies
        if self.crit_case is False:
            # TODO: sort this monstrosity of a function call out
            self.tally_list, self.f_types, self.F2_tallies, self.F4_tallies, self.F5_tallies, self.F6_tallies = self.get_tallies()
        # apply scaling factor
            if self.scaling_factor != 1:
                for tally in self.tally_list:
                    tally.scale_result(self.scaling_factor)

    def __repr__(self):
        return (f"This Eddy MCNP case considers file {self.name}\n"
                f"from {self.filepath}\n"
                f"The scaling factor is {self.scaling_factor}\n"
                f"Criticality case: {self.crit_case}\n")

    def get_date_time(self):
        """Get the date and time that the mcnp case was run

        Returns:
            tuple: The rundate and runtime, as a tuple of 2 strings
        """
        for line in self.file:
            if line.startswith('1mcnp'):
                time = line.split()[5]
                date = line.split()[4]
                date = date.split('/')
                d = date[1]
                m = date[0]
                y = '20' + date[2]
                # date_time = {'date': f"{y}/{m}/{d}", 'time': time}
                rundate = f"{y}/{m}/{d}"
                runtime = time
                return rundate, runtime

    def get_runtime(self):
        """Get the time or number of particles the MCNP case was run for

        Returns:
            tuple:
                str:
                    The number of minutes the code ran for, or None if not found.
                str:
                    nps The number of particles run, or None if not found.

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
            list: The MCNP input deck, as a list of strings
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
            dict: A dictionary containing all the parameters used by this case,
                    and their values
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
            bool: True if run terminated due to lost particles, otherwise False

        """
        for line in self.file:
            if "run terminated because" in line and "particles got lost" in line:
                return True
        return False

    def get_fatal_errors(self):
        """Find the warnings in the MCNP output data

        Returns:
            list: A list of the fatal error messages
        """
        fatal_errors = []
        for line in self.file:
            if "fatal error." in line:
                message = line[14:].strip().capitalize()
                fatal_errors.append(message)
        return fatal_errors

    def get_warnings(self):
        """Find the warnings in the MCNP output data

        Returns:
            list: A list of the warning messages
        """
        warnings = []
        PATTERN_warnings = re.compile(r'warning')
        for line in self.file:
            if PATTERN_warnings.search(line):
                if "warning message so far" not in line and "warning messages so far" not in line:
                    warning = line[10:].strip().capitalize()
                    if warning not in warnings:
                        warnings.append(warning)
        return warnings

    def get_comments(self):
        """Find the comments in the MCNP output file.

        Returns:
            list: A list of the comments
        """
        PATTERN_comments = re.compile(r'comment\.\s+[A-Za-z0-9].+')    # Ignores blank comment lines
        comments = []
        for line in self.file:
            if PATTERN_comments.search(line):
                comment = line[10:].strip().capitalize()
                comments.append(comment)
        return comments

    def get_duplicate_surfaces(self):
        """Find all the duplicate surface messages in the mcnp output

        Returns:
            list: A list of the duplicate surfaces
        """
        duplicate_surfaces = []
        PATTERN_duplicates = re.compile(r'\ssurface\s+\d+.+and surface.+are the same.+')
        for line in self.file:
            if PATTERN_duplicates.match(line):
                if line.strip().capitalize() not in duplicate_surfaces:
                    duplicate_surfaces.append(line.strip().capitalize())
        return duplicate_surfaces

    def get_k_eff(self):
        """Search the output data for the section concerning k-effective, and create a single dictionary holding the data

        Returns:
            dict: A dictionary with the k-effective values for the first half, second half and total run
        """
        PATTERN_k_eff = re.compile(r'^\s*problem\s+keff.+')
        k_eff = {}
        for num, line in enumerate(self.file):
            if PATTERN_k_eff.match(line):
                first_half = re.split(r'\s{2,}', self.file[num+2].strip())
                k_eff['first half k_eff'] = float(first_half[1])
                k_eff['first half stdev'] = float(first_half[2])

                second_half = re.split(r'\s{2,}', self.file[num+3].strip())
                k_eff['second half k_eff'] = float(second_half[1])
                k_eff['second half stdev'] = float(second_half[2])

                final_result = re.split(r'\s{2,}', self.file[num+4].strip())
                k_eff['final k_eff'] = float(final_result[1])
                k_eff['final stdev'] = float(final_result[2])
        return k_eff

    def get_active_cycles(self):
        """For a crit case, find the number of active and inactive cycles

        Returns:
            dict: A dictionary with entries for active and inactive cycles
        """
        cycles = {}
        for line in self.file:
            if "the minimum estimated standard deviation for the col/abs/tl keff estimator occurs with" in line:
                cycles["inactive"] = int(line.split()[12])
                cycles["active"] = int(line.split()[16])
        return cycles

    def get_cell_data(self):
        """Loop through the mcnp output to find the section containing the cell data

        Returns:
            list: The section of the output containing the cell data
        """
        PATTERN_cells_start = re.compile(r'1cells')
        PATTERN_cells_ends = re.compile(r' total')
        cell_section = []
        for line in self.file:
            if PATTERN_cells_start.match(line):
                cell_start_line = self.file.index(line)
                for row in self.file[cell_start_line:]:
                    cell_section.append(row.strip('\n'))
                    if PATTERN_cells_ends.match(row):
                        break
                break
        return cell_section

    def get_particle_populations(self, particle):
        """Find and return the section of the output data concerning populations of a particular particle.
        This function is in the EddyCase class rather than the Cell class as this data is in a separate part
        of the MCNP output from the rest of the cell data.

        Args:
            particle (str): either 'photon', 'neutron' or 'electron'

        Returns:
            list: the lines from the output file concerning populations of that particle,
                    or None if no particle information is found
        """
        PATTERN_run_terminated = re.compile(r'^\+\s+\d\d/\d\d/\d\d(.+)')
        PATTERN_particle_populations = re.compile(fr'^1{particle}\s+activity\sin\seach\scell.+')
        PATTERN_end_populations = re.compile(r'\s+total.+')
        for n, line in enumerate(self.file):
            if PATTERN_run_terminated.match(line):
                terminated = n
                for m, new_line in enumerate(self.file[terminated:], start=terminated):
                    if PATTERN_particle_populations.match(new_line):
                        for p in range(m, len(self.file)):
                            if PATTERN_end_populations.match(self.file[p]):
                                particle_populations = self.file[m:p + 1]
                                return particle_populations
        return None

    def create_cells(self):
        """Take the cell data and create objects of the Cell class

        Returns:
            list: a list of all the Cell objects

        """
        cell_list = []
        header = (self.cell_data[2].split())
        PATTERN_cell = re.compile(r'\s+\d+\s.+')
        for line in self.cell_data[1:]:
            if PATTERN_cell.match(line):
                info = line.split()
                neutron_importance = self.get_particle_importance(header, info, 'neutron')
                photon_importance = self.get_particle_importance(header, info, 'photon')
                electron_importance = self.get_particle_importance(header, info, 'electron')
                cell_list.append(Cell(
                    cell_number=info[1],
                    material_number=info[2],
                    atom_density=info[3],
                    gram_density=info[4],
                    volume=info[5],
                    mass=info[6],
                    neutron_importance=neutron_importance,
                    photon_importance=photon_importance,
                    electron_importance=electron_importance,
                    )
                )
        return cell_list

    def find_mcnp_particle_data(self, particle):
        """Find the particle data in the mcnp output.

        Args:
            particle (str): either neutron, photon or electron

        Returns:
            list: The part of the MCNP output with the particle data
        """
        particle_data = None  # ensure we return None if data is not found
        PATTERN_run_terminated = re.compile(r'^\+\s+\d\d/\d\d/\d\d(.+)')
        PATTERN_particle = {
            'neutron': re.compile(r'\sneutron\screation\s+tracks.+'),
            'photon': re.compile(r'\sphoton\screation\s+tracks.+'),
            'electron': re.compile(r'\selectron\screation\s+tracks.+')
        }
        # The particle data tables are different lengths for the different particle types
        particle_data_lines = {'neutron': 28, 'photon': 33, 'electron': 24}
        # Find the particle data and save to a list
        for n, line in enumerate(self.file):
            if PATTERN_run_terminated.match(line):
                terminated = n
                for m, new_line in enumerate(self.file[terminated:], start=terminated):
                    if PATTERN_particle[particle].match(new_line):
                        particle_data = self.file[m:m + particle_data_lines[particle]]
                        break
        return particle_data

    def create_particle(self, particle, particle_data):
        """Get the relevant information from the particle data (by calling another method), then create a Particle object

        Args:
            particle (str): Either 'neutron', 'photon' or 'electron'
            particle_data (list): The part of the MCNP output with the particle data for this particle

        Returns:
            Particle: The new particle object
        """
        creation_data, loss_data, total_data = self.sort_mcnp_particle_data(particle, particle_data)
        return Particle(
            particle_type=particle,
            creation_data=creation_data,
            loss_data=loss_data,
            total_data=total_data,
        )

    def get_tallies(self):
        """Find the tally sections in the MCNP output.

        Returns:
            tuple: the tally_list, f_types, F2_tallies, F4_tallies, F5_tallies, F6_tallies variables
        """
        tally_list = []   # list of all tallies
        f_types = []
        F2_tallies = {'neutrons': [], 'photons': [], 'electrons': []}
        F4_tallies = {'neutrons': [], 'photons': [], 'electrons': []}
        F5_tallies = {'neutrons': [], 'photons': [], 'electrons': []}
        F6_tallies = {'neutrons': [], 'photons': [], 'electrons': [], 'Collision Heating': []}

        PATTERN_run_terminated = re.compile(r'^\+\s+\d\d/\d\d/\d\d(.+)')
        PATTERN_tally_start = re.compile(r'^\s*1tally\s+\d+\s+nps.+')
        PATTERN_tally_end = re.compile(r'(^\s*(1tally|1status).+)')
        for n, line in enumerate(self.file):
            if PATTERN_run_terminated.match(line):
                terminated = n
                for m, new_line in enumerate(self.file[terminated:], start=terminated):
                    if PATTERN_tally_start.match(new_line):
                        tally_start = m
                        for o, other_line in enumerate(self.file[tally_start + 1:], start=tally_start + 1):
                            if PATTERN_tally_end.match(other_line):
                                tally_end = o
                                break
                        try:
                            tally_data = self.file[tally_start:tally_end]
                        except NameError:
                            print("Eddy did not find the end of one of the tally data sections.")
                            raise
                        tally_type = tally_data[1].split()[2]
                        # Create tally object
                        if tally_type == "2":
                            new_tally = F2Tally(tally_data)
                            F2_tallies[new_tally.particles].append(new_tally)
                        elif tally_type == "4":
                            new_tally = F4Tally(tally_data)
                            F4_tallies[new_tally.particles].append(new_tally)
                        elif tally_type == "5":
                            new_tally = F5Tally(tally_data)
                            F5_tallies[new_tally.particles].append(new_tally)
                        elif tally_type == "6" or tally_type == "6+":
                            new_tally = F6Tally(tally_data)
                            F6_tallies[new_tally.particles].append(new_tally)
                        else:
                            raise Exception("This tally type is not recognised")
                        assert new_tally, "EddyCase.get_tallies failed to create a recognised tally"
                        tally_list.append(new_tally)
                        if new_tally.f_type not in f_types:
                            f_types.append(new_tally.f_type)
                break
        return tally_list, f_types, F2_tallies, F4_tallies, F5_tallies, F6_tallies

    @staticmethod
    def sort_mcnp_particle_data(particle, data):
        """Separate out the photon data into creation, loss, and total data,
        then split each by indices and put into a dictionary

        Args:
            data (list): The part of the MCNP output with the particle data for this particle
            particle (str): either neutron, photon or electron

        Returns:
            a tuple containing
                creation_dict: The particle creation data,
                loss_dict: The particle loss data,
                total_dict: The particle neutron data,
        """
        # TODO: Make this whole method clearer

        indices = [0, 18, 27, 41, 55]
        particle_data_table_range = {
            'photon': range(3, 27),
            'neutron': range(3, 22),
            'electron': range(3, 18),
        }
        particle_summary_range = {
            'photon': range(28, 32),
            'neutron': range(23, 27),
            'electron': range(19, 23),
        }
        creation_dict = {}
        loss_dict = {}

        # get particle numbers from table in mcnp output
        for line_num in particle_data_table_range[particle]:
            # Separate creation data
            creation = data[line_num][:55]
            # split the line into 4 columns
            creation = [creation[indices[i]:indices[i + 1]].strip() for i in range(len(indices) - 1)]
            creation_dict[creation[0]] = {'tracks': int(creation[1]),
                                          'weight': float(creation[2]),
                                          'energy': float(creation[3]),
                                          }
            # Separate loss data
            loss_line = data[line_num][64:]
            # for photons there are fewer loss values than creation values, so we check if the line has contents
            if loss_line.isspace() is False:
                # split the line into 4 columns
                loss = [loss_line[indices[i]:indices[i + 1]].strip() for i in range(len(indices) - 1)]
                loss_dict[loss[0]] = {'tracks': int(loss[1]),
                                      'weight': float(loss[2]),
                                      'energy': float(loss[3]),
                                      }

        # get summary data for particle
        total_dict = {}
        for line_num in particle_summary_range[particle]:
            total = data[line_num][:42].strip(), data[line_num][42:53].strip()
            total_dict[total[0]] = total[1]

        return creation_dict, loss_dict, total_dict

    @staticmethod
    def get_particle_importance(header, data, particle):
        """For a particular particle type, determine the importance of that particle.
        This function is called for each cell as part of its creation.

        Args:
            header (list): The particle population table header.
            data (list): The section of the mcnp output with the cell data.
            particle (str): Either 'neutron', 'photon' or 'electron'.

        Returns:
            str: The particle importance, or 0.

        """
        if particle in header:
            particle_importance = data[header.index(particle) + 6]
        else:
            particle_importance = '0'
        return particle_importance
