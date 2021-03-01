
""" To run: just call python -m pytest while in this directory
or add a configuration in pycharm
"""

from eddymc.mcnp.mcnp_html_writer import get_css


def test_get_css():
    # arrange
    # act
    actual_css = get_css()
    # assert
    assert type(actual_css) == str
    assert actual_css is not ''
