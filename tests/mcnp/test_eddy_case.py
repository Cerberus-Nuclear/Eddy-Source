""" To run: just call python -m pytest while in this directory
or add a configuration in pycharm
"""

import pytest
from eddymc.mcnp.eddy_case import EddyCase
from tests import mcnp_examples

try:
    import importlib.resources as pkg_resources
except ImportError:
    import importlib_resources as pkg_resources


@pytest.fixture
def f2_file(tmpdir):
    f2 = pkg_resources.read_text(mcnp_examples, 'F2.out')
    return f2.split('\n')


@pytest.fixture
def simple_case(f2_file, tmpdir):
    class MockEddyCase(EddyCase):
        def __init__(self, filepath, scaling_factor, file, crit_case=False):
            self.filepath = filepath
            self.name = filepath.replace('\\', '/').split('/')[-1]
            self.scaling_factor = scaling_factor
            self.file = file
            self.crit_case = crit_case
    return MockEddyCase(
        filepath="mcnp_examples/F2.out",
        scaling_factor=1234,
        file=f2_file,
        crit_case=False)


def test_object_created(f2_file):
    # arrange
    path = "mcnp_examples/F2.out"
    sf = 1234
    # act
    case = EddyCase(filepath=path, scaling_factor=sf, file=f2_file, crit_case=False)
    # assert
    assert case


def test_get_date_time(simple_case):
    # act
    rundate, runtime = simple_case.get_date_time()
    # assert
    assert type(rundate) == str
    assert type(runtime) == str


def test_get_runtime(simple_case):
    # arrange
    # act
    ctme, nps = simple_case.get_runtime()
    # assert
    # This case (F2.out) has ctme but to nps card
    assert type(ctme) == str
    assert nps is None


def test_get_input(simple_case):
    # arrange
    # act
    actual_input = simple_case.get_input()
    # assert
    assert actual_input[0] == 'Test MCNP example'
    assert actual_input[-6] == 'RAND SEED=7048155456235'
    assert actual_input[-1] == ''
    assert len(actual_input) == 191


def test_get_parameters_positive(simple_case):
    # arrange
    parameter_input = [r"Test MCNP example",
                       r"c",
                       r"c ==============================================================================",
                       r"c",
                       r"c",
                       r"c                 _______     _______ _      ____  _   _ ______",
                       r"c                / ____\ \   / / ____| |    / __ \| \ | |  ____|",
                       r"c               | |     \ \_/ / |    | |   | |  | |  \| | |__",
                       r"c               | |      \   /| |    | |   | |  | | . ` |  __|",
                       r"c               | |____   | | | |____| |___| |__| | |\  | |____",
                       r"c                \_____|  |_|  \_____|______\____/|_| \_|______|",
                       r"c",
                       r"c",
                       r"c",
                       r"c                                Version 0.19.2",
                       r"c",
                       r"c ######################### Cerberus Nuclear 2020 ############################",
                       r"c",
                       r"c",
                       r"c",
                       r"c",
                       r"c     USING THE FOLLOWING VARIABLES:",
                       r"c               width     =   10.00000",
                       r"c",
                       r"c",
                       r"c =============================== START TITLE ==================================",
                       r"c ==============================================================================",
                       r"c   MCNP example Case - concentric spheres",
                       r"c",
                       r"c",
                       r"c <width=10>",
                       r"c",
                       r"c ==============================================================================",
                       r"c ============================= START CELL SECTION =============================",
                       r"c ==============================================================================",
                       ]
    case = simple_case
    case.mcnp_input = parameter_input
    # act
    variables = simple_case.get_parameters()
    # assert
    assert variables['width'] == 10


def test_get_parameters_negative(simple_case):
    # arrange
    no_parameter_input = [r"Test MCNP example",
                          r"c",
                          r"c ==============================================================================",
                          r"c",
                          r"c",
                          r"c                 _______     _______ _      ____  _   _ ______",
                          r"c                / ____\ \   / / ____| |    / __ \| \ | |  ____|",
                          r"c               | |     \ \_/ / |    | |   | |  | |  \| | |__",
                          r"c               | |      \   /| |    | |   | |  | | . ` |  __|",
                          r"c               | |____   | | | |____| |___| |__| | |\  | |____",
                          r"c                \_____|  |_|  \_____|______\____/|_| \_|______|",
                          r"c",
                          r"c",
                          r"c",
                          r"c                                Version 0.19.2",
                          r"c",
                          r"c ######################### Cerberus Nuclear 2020 ############################",
                          r"c",
                          r"c",
                          r"c",
                          r"c",
                          r"c     USING THE FOLLOWING VARIABLES:",
                          r"c",
                          r"c",
                          r"c =============================== START TITLE ==================================",
                          r"c ==============================================================================",
                          r"c   MCNP example Case - concentric spheres",
                          r"c",
                          r"c",
                          r"c <width=10>",
                          r"c",
                          r"c ==============================================================================",
                          r"c ============================= START CELL SECTION =============================",
                          r"c ==============================================================================", ]
    case = simple_case
    case.mcnp_input = no_parameter_input
    # act
    variables = simple_case.get_parameters()
    # assert
    # should be an empty dict
    assert not variables
