
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


def test_read_file():
    # arrange
    file = os.path.dirname(mcnp_examples.__file__)
    file += "\\F2.out"
    # act
    data = mcnp_converter.read_file(file)
    # assert
    assert data[0].strip() == "Code Name & Version = MCNP_6.20, 6.2.0"
    assert len(data) == 884


def test_parse_output():
    # This one might need a lot of tests
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
    pass
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
    input_section = [
"Test MCNP example",
"c",
"c ==============================================================================",
"c",
"c",
"c                 _______     _______ _      ____  _   _ ______",
"c                / ____\ \   / / ____| |    / __ \| \ | |  ____|",
"c               | |     \ \_/ / |    | |   | |  | |  \| | |__",
"c               | |      \   /| |    | |   | |  | | . ` |  __|",
"c               | |____   | | | |____| |___| |__| | |\  | |____",
"c                \_____|  |_|  \_____|______\____/|_| \_|______|",
"c",
"c",
"c",
"c                                Version 0.19.2",
"c",
"c ######################### Cerberus Nuclear 2020 ############################",
"c",
"c",
"c",
"c",
"c     USING THE FOLLOWING VARIABLES:",
"c               width     =   10.00000",
"c",
"c",
"c =============================== START TITLE ==================================",
"c ==============================================================================",
"c   MCNP example Case - concentric spheres",
"c",
"c",
"c <width=10>",
"c",
"c ==============================================================================",
"c ============================= START CELL SECTION =============================",
"c ==============================================================================",
]
    # act
    parameters = mcnp_converter.get_parameters(input_section)
    # assert
    assert parameters['width'] == 10.0


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



def test_get_duplicate_surfaces():
    pass
    # arrange
    # act
    # assert


def test_get_keff():
    pass
    # arrange
    # act
    # assert


def test_get_active_cycles():
    pass
    # arrange
    # act
    # assert


def test_main_calls_mcnp_html_writer(mocker):
    # arrange
    file = os.path.dirname(mcnp_examples.__file__)
    file += "\\F2.out"
    sf = 1.0
    mocked_html_writer = mocker.patch('eddymc.mcnp.mcnp_converter.mcnp_html_writer.main')
    # act
    mcnp_converter.main(file, sf)
    # assert
    mocked_html_writer.assert_called_with(file)


def test_main_writes_to_gv(mocker):
    # arrange
    file = os.path.dirname(mcnp_examples.__file__)
    file += "\\F2.out"
    sf = 1.0
    output = mocker.patch('eddymc.mcnp.mcnp_converter.gv')
    # mock the rest of the main() function so it doesn't make actual calls
    mock_read_file = mocker.patch('eddymc.mcnp.mcnp_converter.read_file')
    mock_parse_output = mocker.patch('eddymc.mcnp.mcnp_converter.parse_output')
    mock_html_writer = mocker.patch('eddymc.mcnp.mcnp_converter.mcnp_html_writer.main')
    # act
    mcnp_converter.main(file, sf)
    # assert
    assert output.scaling_factor == 1.0
    assert output.crit_case is False


# TODO: add tests for parse_output (see line 34)
