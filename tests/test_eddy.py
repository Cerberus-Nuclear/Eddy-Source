
""" To run: just call python -m pytest while in this directory
or add a configuration in pycharm
"""

import pytest
from argparse import Namespace

from eddymc import eddy


def test_crit_checker_positive():
    # arrange
    text = ["cat", "kcode", "badger"]
    # act
    result = eddy.check_if_crit(text)
    # assert
    assert result is True


def test_crit_checker_negative():
    # arrange
    text = ["cat", "dog", "badger"]
    # act
    result = eddy.check_if_crit(text)
    # assert
    assert result is False


def test_get_scaling_factor_with_cli_args():
    # arrange
    args = Namespace(file=None, scaling_factor=1.6)
    # act
    sf = eddy.get_scaling_factor(args)
    # assert
    assert sf == 1.6


def test_get_scaling_factor_with_invalid_cli_arg():
    # arrange
    args = Namespace(file=None, scaling_factor='parrot')
    # act
    with pytest.raises(ValueError):
        sf = eddy.get_scaling_factor(args)
    # assert

