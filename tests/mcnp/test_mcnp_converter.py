
""" To run: just call python -m pytest while in this directory
or add a configuration in pycharm
"""

import pytest
from eddymc.mcnp import mcnp_converter


@pytest.fixture
def f2_file(tmpdir):
    with open('./mcnp_examples/F2.out', 'r') as f:
        file = f.readlines()
    return file


@pytest.fixture
def f2_nps_file(tmpdir):
    with open('./mcnp_examples/F2_nps.out', 'r') as f:
        file = f.readlines()
    return file


def test_read_file():
    # arrange
    file = "./mcnp_examples/F2.out"
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