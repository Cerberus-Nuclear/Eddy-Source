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
    returns = simple_case.get_date_time()
    # assert
    assert returns
