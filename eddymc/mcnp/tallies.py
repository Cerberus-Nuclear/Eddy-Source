#!/usr/bin/env python3
# Peter Evans
# Cerberus Nuclear Ltd

"""
    This module holds all the code relating to tallies.
"""

# standard library imports
import re
# local imports:


class Tally:
    """Each mcnp tally is represented by a Tally object containing all the available data about that tally.
    All tallies should be members of one of the subclass of this Tally class.
    """

    def __init__(self, data):
        # for item in data: print(item)
        self.data = data    # can be removed once this method is complete
        self.tally_number = data[0].split()[1]
        self.nps = data[0].split()[4]
        self.f_type = 'F' + data[1].split()[2]
        self.tally_type = data[1].split()[3:]
        self.tally_type = ' '.join(self.tally_type)
        self.particles = data[2].split()[1]
        self.dose_functions = self.get_dose_functions()
        self.results = self.get_results()
        self.statistical_checks = self.get_statistical_checks()
        self.passes = self.get_passes()

    def get_dose_functions(self):
        """Gets the dose function, if any, that the results of this tally are multiplied by

        Returns:
            Either a tuple of the DE and DF functions, if they exist, otherwise a string
            stating that this tally is not multiplied by a dose function.

        """
        if "this tally is modified by dose function" in self.data[3]:
            return self.data[3].split()[7], self.data[3].split()[9][:-1]
        else:
            return "This tally is not modified by any dose function"

    def get_results(self):
        """This is a placeholder method; each subclass of Tally should have its own 'get_results' method"""
        raise NotImplementedError(f"The {self.__class__} subclass should have its own get_results() method")

    def get_statistical_checks(self):
        """Get the statistical check results from the mcnp output file

        Returns:
            statistical_checks, a dictionary with the results of the statistical checks for this tally.
        """
        start_PATTERN = re.compile(r"\s+results of 10 statistical checks.+")
        value = None
        pass_fail = None
        for n, line in enumerate(self.data):
            if start_PATTERN.match(line):
                value = self.data[n+6].split()
                pass_fail = self.data[n+7].split()
                break
        if value:       # if statistical checks have been found
            statistical_checks = {
                'mean_behaviour'    : {'value': value[1], 'pass': pass_fail[1]},
                'rel_err_value'     : {'value': value[2], 'pass': pass_fail[2]},
                'rel_err_decrease'  : {'value': value[3], 'pass': pass_fail[3]},
                'rel_err_dec_rate'  : {'value': value[4], 'pass': pass_fail[4]},
                'VoV_value'         : {'value': value[5], 'pass': pass_fail[5]},
                'VoV_decrease'      : {'value': value[6], 'pass': pass_fail[6]},
                'VoV_dec_rate'      : {'value': value[7], 'pass': pass_fail[7]},
                'FoM_value'         : {'value': value[8], 'pass': pass_fail[8]},
                'FoM_behaviour'     : {'value': value[9], 'pass': pass_fail[9]},
                'pdf_slope'         : {'value': value[10], 'pass': pass_fail[10]},
                }
        else:
            # print(f"Tally {self.tally_number} does not have statistical checks")
            statistical_checks = {
                'mean_behaviour'    : {'value': r"none", 'pass': "no"},
                'rel_err_value'     : {'value': r"none", 'pass': "no"},
                'rel_err_decrease'  : {'value': r"none", 'pass': "no"},
                'rel_err_dec_rate'  : {'value': r"none", 'pass': "no"},
                'VoV_value'         : {'value': r"none", 'pass': "no"},
                'VoV_decrease'      : {'value': r"none", 'pass': "no"},
                'VoV_dec_rate'      : {'value': r"none", 'pass': "no"},
                'FoM_value'         : {'value': r"none", 'pass': "no"},
                'FoM_behaviour'     : {'value': r"none", 'pass': "no"},
                'pdf_slope'         : {'value': r"none", 'pass': "no"},
            }
        return statistical_checks

    def get_passes(self):
        """Determine how many statistical checks were passed

        Returns:
            Passes (int): the number of checks passed (out of ten)
        """
        passes = 0
        if self.statistical_checks:
            for check in self.statistical_checks:
                if self.statistical_checks[check]['pass'] == 'yes':
                    passes += 1
        return passes

    def scale_result(self, scaling_factor):
        """Each subclass of Tally should have its own normalise_data method"""
        print("This Tally class appears not to have its own 'normalise_data() method.")
        raise NotImplementedError(f"The {self.__class__} subclass should have its own normalise_data method")

    def describe_object(self):
        """ Print a description of the Tally object to the terminal."""
        print()
        print(f"Tally {self.tally_number}")
        print(f"Tally type: {self.f_type}, {self.tally_type}")
        print(f"Particles: {self.particles}")
        print(f"Number of particles: {self.nps}")
        print(f"This tally is modified by dose functions {self.dose_functions[0]} and {self.dose_functions[1]}")
        print(f"Tally Results: ")
        for region in self.results:
            print(f"    {region['region']}:     Tally Result = {region['result']}      Variance = {region['variance']}")
        print()
        if 'statistical_checks' in dir(self):
            print("Statistical Check      Value      Pass?")
            for check in self.statistical_checks:
                print(f"{check + ':' : <21}  {self.statistical_checks[check]['value'] : <11} {self.statistical_checks[check]['pass'] : <3}")
            print(f"{self.passes} out of 10 statistical checks passed.")
            print()
        else:
            print("This tally does not have statistical checks.")


class F2Tally(Tally):
    def __init__(self, data):
        super().__init__(data)

    def get_results(self):
        """
            Gets the tally results from the mcnp output file
            Args: self: the object, data: the mcnp output tally section
            Returns: regions: a dictionary holding the results for that tally
        """
        data = self.data
        results = []
        for num, line in enumerate(data):
            if "surface " in line:
                results.append({
                    "surface": line.strip().capitalize(),
                    "result": float(data[num+1].split()[0]),
                    "variance": float(data[num+1].split()[1])
                })
        return results

    def scale_result(self, scaling_factor):
        """Applies scaling factor to results
            Args:
                scaling_factor (float): a number by which the region results are multiplied
            Returns: none, but modifies self.results
        """
        for surface in self.results:
            surface['result'] *= scaling_factor


class F4Tally(Tally):
    def __init__(self, data):
        super().__init__(data)

    def get_results(self):
        """Get the tally results from the mcnp output file

        Returns:
            list: A list of dictionaries, each corresponding to a cell
                            in this tally, with entries for region, result and variance.
        """
        data = self.data
        results = []
        for num, line in enumerate(data):
            if (" cell " in line) or (" surface  " in line):
                results.append({
                    "region": line.strip().capitalize(),
                    "result": float(data[num+1].split()[0]),
                    "variance": float(data[num+1].split()[1])
                })
        return results

    def scale_result(self, scaling_factor):
        """Applies scaling factor to results
            Args:
                scaling_factor (float): a number by which the region results are multiplied
            Returns: none, but modifies self.results
        """
        for region in self.results:
            region['result'] *= scaling_factor


class F5Tally(Tally):
    def __init__(self, data):
        super().__init__(data)

    def get_results(self):
        """
            Gets the tally results from the mcnp output file
            Args: self: the object, data: the mcnp output tally section
            Returns: regions: a dictionary holding the results for that tally
        """
        data = self.data
        results = {}
        for num, line in enumerate(data):
            if "detector located at" in line:
                results["x"] = float(line[28:40])
                results["y"] = float(line[40:52])
                results["z"] = float(line[52:64])
                results["result"] = float(data[num+1].split()[0])
                results["variance"] = float(data[num+1].split()[1])
                break
        return results

    def describe_object(self):
        """ Prints a description of the Tally object to the terminal."""
        print()
        print(f"Tally {self.tally_number}")
        print(f"Tally type: {self.f_type}, {self.tally_type}")
        print(f"Particles: {self.particles}")
        print(f"Number of particles: {self.nps}")
        print(f"This tally is modified by dose functions {self.dose_functions[0]} and {self.dose_functions[1]}")
        print(f"Tally Results: ")
        print(f"   Position: {self.results['x']},{self.results['y']},{self.results['z']}   Tally Result = {self.results['result']}      Variance = {self.results['variance']}")
        print()
        if 'statistical_checks' in dir(self):
            print("Statistical Check      Value      Pass?")
            for check in self.statistical_checks:
                print(f"{check + ':' : <21}  {self.statistical_checks[check]['value'] : <11} {self.statistical_checks[check]['pass'] : <3}")
            print(f"{self.passes} out of 10 statistical checks passed.")
            print()
        else:
            print("This tally does not have statistical checks.")

    def scale_result(self, scaling_factor):
        """Applies scaling factor to results
            Args:
                scaling_factor (float): a number by which the region results are multiplied
            Returns: none, but modifies self.results
        """
        self.results["result"] *= scaling_factor


class F6Tally(Tally):
    def __init__(self, data):
        super().__init__(data)
        if self.f_type == "F6+":
            self.particles = "Collision Heating"

    def get_results(self):
        data = self.data
        """Get the tally results from the MCNP output file
        Args:
            data (list): the section of the MCNP output file for this tally
        Returns:
            results (dict): A dictionary of dictionaries of dictionaries, each corresponding to a cell
                            in this tally, with entries for region, mass, result 
                            and variance.
        """
        results = {}
        for num, line in enumerate(data):
            if 'masses' in line:
                masses_start = num
                break
        for num, line in enumerate(data[masses_start:], start=masses_start):
            if 'cell  ' in line:
                masses_end = num-1
                break
        mass_data = data[masses_start:masses_end]
        for num, line in enumerate(mass_data):
            if "cell" in line:
                for n, mass in enumerate(mass_data[num+1].split()):
                    cell_no = mass_data[num].split()[n+1]
                    results[cell_no] = {'region': f"Cell {cell_no}", 'mass': float(mass)}


        PATTERN_f6_cell = re.compile(r'^\s+cell\s+\d+')
        for num, line in enumerate(data):
            if 'cell ' in line:
            #if PATTERN_f6_cell.match(line):
                cell_no = line.split()[1]
                results[cell_no]["result"] = float(data[num+1].split()[0])
                results[cell_no]["variance"] = float(data[num+1].split()[1])

        return results

    def scale_result(self, scaling_factor):
        """Applies scaling factor to results
            Args:
                scaling_factor (float): a number by which the region results are multiplied
            Returns: none, but modifies self.results
        """
        for region in self.results:
            self.results[region]['result'] *= scaling_factor


############################################################
#  End of Tally class                                      #
############################################################
