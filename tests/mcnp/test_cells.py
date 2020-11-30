
""" To run: just call python -m pytest while in this directory
or add a configuration in pycharm
"""

import pytest
from eddymc.mcnp import cells
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
def f2_cell_section(tmpdir):
    return ["1cells                                                                                                  print table 60",
            "",
            "                               atom        gram                                            neutron    photon     photon wt             ",
            "              cell      mat   density     density     volume       mass            pieces importance importance generation             ",
            "",
            "        1        1        1  8.83440E-02 7.81000E+00 4.18879E+00 3.27145E+01           1  1.0000E+00 1.0000E+00 -1.000E+00             ",
            "        2        2        2  5.02980E-05 1.20500E-03 4.06019E+03 4.89253E+00           1  1.0000E+00 1.0000E+00 -1.000E+00             ",
            "        3        3        2  5.02980E-05 1.20500E-03 1.24411E+02 1.49916E-01           1  1.0000E+00 1.0000E+00 -1.000E+00             ",
            "        4        4        2  5.02980E-05 1.20500E-03 1.38649E+03 1.67072E+00           1  1.0000E+00 1.0000E+00 -1.000E+00             ",
            "        5        5        0  0.00000E+00 0.00000E+00 0.00000E+00 0.00000E+00           0  0.0000E+00 0.0000E+00 -1.000E+00             ",
            "",
            " total                                               5.57528E+03 3.94276E+01",
            ]


def test_find_cells(f2_file):
    # arrange
    # act
    cell_section = cells.find_cells(f2_file)
    # assert
    assert len(cell_section) == 12


def test_create_cell_objects_calls_init(mocker, f2_cell_section):
    # arrange
    cell_init = mocker.patch('eddymc.mcnp.cells.Cell.__init__', return_value=None)
    # act
    cells.create_cell_objects(f2_cell_section)
    # assert
    assert cell_init.call_count == 5
