
""" To run: just call python -m pytest while in this directory
or add a configuration in pycharm
"""

import os
import pytest
from eddymc.mcnp import mcnp_converter
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
def f2_nps_file(tmpdir):
    f2_nps = pkg_resources.read_text(mcnp_examples, 'F2_nps.out')
    return f2_nps.split('\n')


@pytest.fixture
def parameters_file(tmpdir):
    file = pkg_resources.read_text(mcnp_examples, 'F4_F5_param.out')
    return file.split('\n')


@pytest.fixture
def dumps_file(tmpdir):
    file = pkg_resources.read_text(mcnp_examples, 'Dumps.out')
    return file.split('\n')


@pytest.fixture
def crit_file(tmpdir):
    file = pkg_resources.read_text(mcnp_examples, 'Criticality.out')
    return file.split('\n')


@pytest.fixture
def failed_case(tmpdir):
    file = pkg_resources.read_text(mcnp_examples, 'fatal_error.out')
    return file.split('\n')


def test_read_file():
    # arrange
    file = os.path.dirname(mcnp_examples.__file__)
    file += "//F2.out"
    #file = 'mcnp_examples/F2.out'
    # act
    data = mcnp_converter.read_file(file)
    # assert
    assert data[0].strip() == "Code Name & Version = MCNP_6.20, 6.2.0"
    assert len(data) == 884


def test_parse_output():
    # This one might need a lot of tests
    # although there is almost no actual logic in this function,
    # it is all calls to other functions
    pass


def test_get_date_time(f2_file):
    # arrange
    file = f2_file
    # act
    date_time = mcnp_converter.get_date_time(file)
    # assert
    assert date_time['date'] == '2020/05/06'
    assert date_time['time'] == '14:56:46'


def test_get_runtime_ctme(f2_file):
    # arrange
    file = f2_file
    expected_ctme = '1'
    # act
    actual_ctme = mcnp_converter.get_runtime(file)[0]
    # assert
    assert actual_ctme == expected_ctme


def test_get_runtime_nps(f2_nps_file):
    # arrange
    file = f2_nps_file
    expected_nps = '100000'
    # act
    actual_nps = mcnp_converter.get_runtime(file)[1]
    # assert
    assert actual_nps == expected_nps


def test_get_input(f2_file):
    # arrange
    file = f2_file
    # act
    actual_input = mcnp_converter.get_input(file)
    # assert
    assert actual_input[0] == 'Test MCNP example'
    assert actual_input[-6] == 'RAND SEED=7048155456235'
    assert actual_input[-1] == ''
    assert len(actual_input) == 191


def test_get_parameters_positive():
    # arrange
    parameters_input = [r"Test MCNP example",
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
    # act
    variables = mcnp_converter.get_parameters(parameters_input)
    # assert
    assert variables['width'] == 10


def test_get_parameters_negative():
    # arrange
    parameters_input = [r"Test MCNP example",
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
    # act
    variables = mcnp_converter.get_parameters(parameters_input)
    # assert
    assert not variables


def test_get_fatal_errors_present(failed_case):
    # arrange
    # act
    fatal_errors = mcnp_converter.get_fatal_errors(failed_case)
    # assert
    assert len(fatal_errors) == 3
    assert fatal_errors[0] == "Surface       -16 not found for cell         4 card."
    assert fatal_errors[1] == "Surface      -16 of cell        4 is not defined."
    assert fatal_errors[2] == "1 tally volumes or areas were not input nor calculated."


def test_get_fatal_errors_not_present(f2_file):
    # arrange
    # act
    fatal_errors = mcnp_converter.get_fatal_errors(f2_file)
    # assert
    assert fatal_errors == []   # empty list


def test_get_warnings(f2_file):
    # arrange
    file = f2_file
    # act
    warnings = mcnp_converter.get_warnings(file)
    # assert
    assert len(warnings) == 4
    assert warnings[0] == "1 materials had unnormalized fractions. print table 40."
    assert warnings[1] == "8017.80c lacks gamma-ray production cross sections."
    assert warnings[2] == "Material        1 has been set to a conductor."
    assert warnings[3] == "2 photons from neutron collisions were created below a local photon energy cutoff and were not followed."


def test_get_comments(f2_file):
    # arrange
    file = f2_file
    # act
    comments = mcnp_converter.get_comments(file)
    # assert
    assert len(comments) == 7
    assert comments[0] == "Physics models disabled."
    assert comments[6] == "Setting up hash-based fast table search for xsec tables"


def test_get_duplicate_surfaces(dumps_file):
    pass
    # arrange
    # act
    duplicate_surfaces = mcnp_converter.get_duplicate_surfaces(dumps_file)
    # assert
    assert len(duplicate_surfaces) == 8
    assert duplicate_surfaces[0] == "Surface       34   and surface      501   are the same.      501   will be deleted."


def test_get_keff(crit_file):
    # arrange
    # act
    k_eff = mcnp_converter.get_k_eff(crit_file)
    # assert
    assert k_eff['first half k_eff'] == 0.78280
    assert k_eff['first half stdev'] == 0.00061
    assert k_eff['second half k_eff'] == 0.78235
    assert k_eff['second half stdev'] == 0.00067
    assert k_eff['final k_eff'] == 0.78257
    assert k_eff['final stdev'] == 0.00045


def test_get_active_cycles(crit_file):
    pass
    # arrange
    # act
    cycles = mcnp_converter.get_active_cycles(crit_file)
    # assert
    assert cycles["inactive"] == 16
    assert cycles["active"] == 184


def test_main_calls_mcnp_html_writer(mocker):
    # arrange
    file = os.path.dirname(mcnp_examples.__file__)
    file += "/F2.out"
    sf = 1.0
    mocked_html_writer = mocker.patch('eddymc.mcnp.mcnp_converter.mcnp_html_writer.main')
    # act
    mcnp_converter.main(file, sf)
    # assert
    mocked_html_writer.assert_called_with(file)


def test_main_writes_to_gv(mocker):
    # arrange
    file = os.path.dirname(mcnp_examples.__file__)
    file += "/F2.out"
    sf = 1.0
    output = mocker.patch('eddymc.mcnp.mcnp_converter.gv')
    # mock the rest of the main() function so it doesn't make actual calls
    mocker.patch('eddymc.mcnp.mcnp_converter.read_file')
    mocker.patch('eddymc.mcnp.mcnp_converter.parse_output')
    mocker.patch('eddymc.mcnp.mcnp_converter.mcnp_html_writer.main')
    # act
    mcnp_converter.main(file, sf)
    # assert
    assert output.scaling_factor == 1.0
    assert output.crit_case is False
