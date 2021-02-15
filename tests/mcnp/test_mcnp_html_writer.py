
""" To run: just call python -m pytest while in this directory
or add a configuration in pycharm
"""

from eddymc.mcnp.mcnp_html_writer import get_css, sanitize_list


def test_get_css():
    # arrange
    # act
    actual_css = get_css()
    # assert
    assert type(actual_css) == str
    assert actual_css is not ''


def test_sanitize_list():
    # arrange
    test_text = [
        "This is ordinary text",
        "This has a <h1> </h1> symbol in it",
        "This has a \" symbol in it",
        "This has a & in it.",
        ]
    # act
    sanitized_text = sanitize_list(test_text)
    # assert
    assert sanitized_text[0] == "This is ordinary text"
    assert sanitized_text[1] == "This has a &lt;h1&gt; &lt;/h1&gt; symbol in it"
    assert sanitized_text[2] == "This has a &#34; symbol in it"
    assert sanitized_text[3] == "This has a &amp; in it."
