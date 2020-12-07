
""" This module holds global (project-level) variables for the MCNP output to HTML converter. """

f = None
scaling_factor = 1
date_time = {}
rundate = None
runtime = None
parameters = {}
cell_list = []
tally_list = []
f_types = []
F2_tallies = {'neutrons': [], 'photons': [], 'electrons': []}
F4_tallies = {'neutrons': [], 'photons': [], 'electrons': []}
F5_tallies = {'neutrons': [], 'photons': [], 'electrons': []}
F6_tallies = {'neutrons': [], 'photons': [], 'electrons': [], 'Collision Heating': []}
tally_types = {}
fatal_errors = []
warnings = []
comments = []
duplicate_surfaces = []
particle_list = []
k_effective = {}
ctme = None
nps = None
mcnp_input = None
crit_case = False
cycles = {}
