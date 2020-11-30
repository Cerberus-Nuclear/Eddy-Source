
""" To run: just call python -m pytest while in this directory
or add a configuration in pycharm
"""

import pytest
from eddymc.mcnp import mcnp_html_writer


def test_get_css():
    # arrange
    # act
    actual_css = mcnp_html_writer.get_css()
    # assert
    assert type(actual_css) == str
    assert actual_css is not ''
