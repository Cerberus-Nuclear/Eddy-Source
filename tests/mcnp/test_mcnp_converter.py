
""" To run: just call python -m pytest while in this directory
or add a configuration in pycharm
"""

import pytest
from eddymc.mcnp import mcnp_converter


def test_read_file():
    # arrange
    file = "./mcnp_examples/F2.out"
    # act
    data = mcnp_converter.read_file(file)
    # assert
    assert data[0].strip() == "Code Name & Version = MCNP_6.20, 6.2.0"
    assert len(data) == 884
