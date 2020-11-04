
""" To run: just call python -m pytest while in this directory
or add a configuration in pycharm
"""

import pytest

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
