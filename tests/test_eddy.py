
""" To run: just call python -m pytest while in this directory
or add a configuration in pycharm
"""

import pytest
from argparse import Namespace
from eddymc import eddy
from eddymc.scale import scale_global_variables as sgv
from tests import mcnp_examples, scale_examples
try:
    import importlib.resources as pkg_resources
except ImportError:
    import importlib_resources as pkg_resources


@pytest.fixture
def f2_file(tmpdir):
    f2 = pkg_resources.read_text(mcnp_examples, 'F2.out')
    return f2.split('\n')


@pytest.fixture
def scale_file(tmpdir):
    file = pkg_resources.read_text(scale_examples, 'cylinder_ce.out')
    return file.split('\n')


@pytest.fixture
def text_file(tmpdir):
    file = pkg_resources.read_text(mcnp_examples, 'not_an_mcnp_file.txt')
    return file.split('\n')


@pytest.fixture
def crit_file(tmpdir):
    file = pkg_resources.read_text(mcnp_examples, 'Criticality.out')
    return file.split('\n')


@pytest.fixture
def mcnp_input(tmpdir):
    with open('tests/mcnp_examples/F4.mcnp', 'r') as f:
        file = f.readlines()
    return file


def test_crit_checker_positive(crit_file):
    # arrange
    text = crit_file
    # act
    result = eddy.check_if_crit(text)
    # assert
    assert result is True


def test_crit_checker_negative(f2_file):
    # arrange
    text = f2_file
    # act
    result = eddy.check_if_crit(text)
    # assert
    assert result is False


def test_read_file():
    # arrange
    file = "mcnp_examples/F2.out"
    # act
    data = eddy.read_file(file)
    # assert
    assert data[0].strip() == "Code Name & Version = MCNP_6.20, 6.2.0"
    assert len(data) == 884


def test_get_filename_with_passed_name():
    # arrange
    file = 'mcnp_examples/F2.out'
    # act
    filename = eddy.get_filename(file)
    # assert
    assert filename == file


"""This test is commented out because I can't get github workflows to 
ignore the Tk().withdraw() line, and it errors there because the server 
can't connect to a display.
Solutions tried so far:
    setting the $DISPLAY variable in the workflow (sets the display, but tkinter can't connect)
    patching various combinations of Tk and withdraw
"""

# def test_get_filename_from_tkinter(mocker):
#     # arrange
#     mocker.patch("eddymc.eddy.Tk.withdraw", return_value=None)
#     mocker.patch("eddymc.eddy.askopenfilename", return_value="mcnp_examples/F2.out")
#     # act
#     file = eddy.get_filename()
#     # assert
#     assert file == 'mcnp_examples/F2.out'


def test_get_filename_if_file_missing():
    # arrange
    name = 'mcnp_examples/nonexistent_file.out'
    # act, assert
    with pytest.raises(AssertionError):
        eddy.get_filename(name)


def test_get_scaling_factor_with_value_passed():
    # arrange
    sf = 3.141592
    # act
    scaling_factor = eddy.get_scaling_factor(sf)
    # assert
    assert scaling_factor == sf


def test_get_scaling_factor_with_value_passed_as_string():
    # arrange
    sf = '3.141592'
    # act
    scaling_factor = eddy.get_scaling_factor(sf)
    # assert
    assert scaling_factor == 3.141592


"""This test is commented out because I can't get github workflows to 
ignore the Tk().withdraw() line, and it errors there because the server 
can't connect to a display. See the comment on test_get_filename_from_tkinter()
for more details
"""
# def test_get_scaling_factor_from_tkinter(mocker):
#     # arrange
#     mocker.patch("eddymc.eddy.Tk.withdraw", return_value=None)
#     mocker.patch("eddymc.eddy.simpledialog.askfloat", return_value=3.141592)
#     # act
#     scaling_factor = eddy.get_scaling_factor()
#     # assert
#     assert scaling_factor == 3.141592


def test_get_scaling_factor_with_invalid_arg_passed():
    # arrange
    sf = 'parrot'
    # act, assert
    with pytest.raises(ValueError):
        eddy.get_scaling_factor(sf)


def test_get_args_with_passed_arguments(mocker):
    # arrange
    name = 'mcnp_examples/F2.out'
    with open('mcnp_examples/F2.out', 'r') as file:
        data = file.readlines()
    sf = 3.141592
    mocker.patch(
        'eddymc.eddy.argparse.ArgumentParser.parse_args',
        return_value=Namespace(file=None, scaling_factor=None),
    )
    # act
    name, output_data, sf, crit = eddy.get_args(name, sf)
    # assert
    assert name == 'mcnp_examples/F2.out'
    assert output_data == data
    assert sf == 3.141592
    assert crit is False


def test_get_args_with_bad_passed_sf(mocker):
    # arrange
    name = 'mcnp_examples/F2.out'
    sf = 'parrot'
    mocker.patch(
        'eddymc.eddy.argparse.ArgumentParser.parse_args',
        return_value=Namespace(file=None, scaling_factor=None),
    )
    # act, assert
    with pytest.raises(ValueError):
        eddy.get_args(name, sf)


def test_main_calls_scale_converter(mocker, scale_file):
    # arrange
    name = 'scale_examples/cylinder_ce.out'
    data = scale_file
    sf = 3.141592
    crit = False
    mocker.patch(
        'eddymc.eddy.argparse.ArgumentParser.parse_args',
        return_value=Namespace(file=None, scaling_factor=None),
    )
    mocked_scale_converter = mocker.patch('eddymc.scale.scale_converter.main')
    mocked_eddy_case = mocker.patch('eddymc.mcnp.eddy_case.EddyCase.__init__')
    # act
    eddy.main(filename=name, scaling_factor=sf)
    # assert
    mocked_scale_converter.assert_called_with(name, sf)
    mocked_eddy_case.assert_not_called()


def test_main_calls_eddy_case(mocker, f2_file):
    # arrange
    name = 'mcnp_examples/F2.out'
    data = f2_file
    sf = 3.141592
    crit = False
    mocker.patch(
        'eddymc.eddy.argparse.ArgumentParser.parse_args',
        return_value=Namespace(file=None, scaling_factor=None),
    )
    mocked_scale_converter = mocker.patch('eddymc.scale.scale_converter.main')
    mocked_eddy_case = mocker.patch('eddymc.mcnp.eddy_case.EddyCase.__init__', return_value=None)
    # The html writer is mocked because that's not what we're testing here
    mocked_html_writer = mocker.patch('eddymc.mcnp.mcnp_html_writer.main', return_value=None)
    # act
    eddy.main(filename=name, scaling_factor=sf)
    # assert
    mocked_eddy_case.assert_called()
    mocked_scale_converter.assert_not_called()


def test_main_calls_html_writer(mocker, f2_file):
    # arrange
    name = 'mcnp_examples/F2.out'
    sf = 1234
    mocked_html_writer = mocker.patch('eddymc.mcnp.mcnp_html_writer.main', return_value=None)
    mocker.patch('eddymc.mcnp.eddy_case.EddyCase.__init__', return_value=None)
    # act
    eddy.main(filename=name, scaling_factor=sf)
    # assert
    mocked_html_writer.assert_called()


def test_input_file_doesnt_continue(mocker):
    # arrange
    name = 'mcnp_examples/F4.mcnp'
    mocker.patch(
        'eddymc.eddy.argparse.ArgumentParser.parse_args',
        return_value=Namespace(file=None, scaling_factor=None),
    )
    mocked_scale_converter = mocker.patch('eddymc.scale.scale_converter.main')
    mocked_eddy_case = mocker.patch('eddymc.mcnp.eddy_case.EddyCase.__init__')
    # act
    with pytest.raises(RuntimeError) as expected_failure:
        eddy.main(filename=name, scaling_factor=1)
    # assert
    mocked_eddy_case.assert_not_called()
    mocked_scale_converter.assert_not_called()
    assert expected_failure


def test_main_with_non_mc_input(mocker, text_file):
    # arrange
    name = 'mcnp_examples/not_an_mcnp_file.txt'
    data = text_file
    sf = 3.141592
    crit = False
    mocker.patch(
        'eddymc.eddy.argparse.ArgumentParser.parse_args',
        return_value=Namespace(file=None, scaling_factor=None),
    )
    # act, assert
    with pytest.raises(RuntimeError):
        eddy.main(name, sf)


def test_main_with_nonexistent_input_passed(mocker):
    # arrange
    name = 'mcnp_examples/nonexistent_file.txt'
    mocker.patch(
        'eddymc.eddy.argparse.ArgumentParser.parse_args',
        return_value=Namespace(file=None, scaling_factor=None),
    )
    # act, assert
    with pytest.raises(AssertionError):
        eddy.main(name)


def test_reset_when_looping_scale(scale_file):
    # arrange
    file = "scale_examples/cylinder_ce.out"
    scaling_factor = 1
    # act
    # call eddy.main twice
    eddy.main(file, scaling_factor)
    eddy.main(file, scaling_factor)
    # assert
    assert len(sgv.tally_list) == 2
