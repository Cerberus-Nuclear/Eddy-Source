
""" To run: just call python -m pytest while in this directory
or add a configuration in pycharm
"""

import pytest
from argparse import Namespace
from eddymc import eddy


@pytest.fixture
def f2_file(tmpdir):
    with open('mcnp_examples/F2.out', 'r') as f:
        file = f.readlines()
    return file


@pytest.fixture
def scale_file(tmpdir):
    with open('scale_examples/cylinder.out', 'r') as f:
        file = f.readlines()
    return file


@pytest.fixture
def text_file(tmpdir):
    with open('mcnp_examples/not_an_mcnp_file.txt', 'r') as f:
        file = f.readlines()
    return file


def test_crit_checker_positive():
    # arrange
    text = ["cat", "kcode", "badger"]
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


def test_get_filename_from_tkinter(mocker):
    # arrange
    mocker.patch("eddymc.eddy.askopenfilename", return_value="mcnp_examples/F2.out")
    # act
    file = eddy.get_filename()
    # assert
    assert file == 'mcnp_examples/F2.out'


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


def test_get_scaling_factor_from_tkinter(mocker):
    # arrange
    mocker.patch("eddymc.eddy.simpledialog.askfloat", return_value=3.141592)
    # act
    scaling_factor = eddy.get_scaling_factor()
    # assert
    assert scaling_factor == 3.141592


def test_get_scaling_factor_with_invalid_arg_passed():
    # arrange
    sf = 'parrot'
    # act, assert
    with pytest.raises(ValueError):
        eddy.get_scaling_factor(sf)


def test_get_args_with_cli_args(mocker, f2_file):
    # arrange
    data = f2_file
    mocker.patch(
        'eddymc.eddy.argparse.ArgumentParser.parse_args',
        return_value=Namespace(file='mcnp_examples/F2.out', scaling_factor=3.141592)
    )
    # act
    name, output_data, sf, crit = eddy.get_args()
    # assert
    assert name == 'mcnp_examples/F2.out'
    assert output_data == data
    assert sf == 3.141592
    assert crit is False


def test_get_args_with_invalid_cli_scaling_factor(mocker):
    # arrange
    mocker.patch(
        'eddymc.eddy.argparse.ArgumentParser.parse_args',
        return_value=Namespace(file='mcnp_examples/F2.out', scaling_factor='parrot')
    )
    # act, assert
    with pytest.raises(ValueError):
        eddy.get_args()


def test_get_args_with_passed_arguments(mocker, f2_file):
    # arrange
    name = 'mcnp_examples/F2.out'
    data = f2_file
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
    name = 'scale_examples/cylinder.out'
    data = scale_file
    sf = 3.141592
    crit = False
    mocker.patch('eddymc.eddy.get_args',
                 return_value=[name, data, sf, crit],
                 )
    mocked_scale_converter = mocker.patch('eddymc.scale.scale_converter.main')
    mocked_mcnp_converter = mocker.patch('eddymc.mcnp.mcnp_converter.main')
    # act
    eddy.main(filename=name, scaling_factor=sf)
    # assert
    mocked_scale_converter.assert_called_with(name, sf)
    mocked_mcnp_converter.assert_not_called()


def test_main_calls_mcnp_converter(mocker, f2_file):
    # arrange
    name = 'mcnp_examples/F2.out'
    data = f2_file
    sf = 3.141592
    crit = False
    mocker.patch('eddymc.eddy.get_args',
                 return_value=[name, data, sf, crit],
                 )
    mocked_scale_converter = mocker.patch('eddymc.scale.scale_converter.main')
    mocked_mcnp_converter = mocker.patch('eddymc.mcnp.mcnp_converter.main')
    # act
    eddy.main(filename=name, scaling_factor=sf)
    # assert
    mocked_mcnp_converter.assert_called_with(name, sf, crit)
    mocked_scale_converter.assert_not_called()


def test_main_with_non_mc_input(mocker, text_file):
    # arrange
    name = 'mcnp_examples/not_an_mcnp_file.txt'
    data = text_file
    sf = 3.141592
    crit = False
    mocker.patch('eddymc.eddy.get_args',
                 return_value=[name, data, sf, crit],
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


def test_main_with_nonexistent_cli_input(mocker):
    # arrange
    mocker.patch(
        'eddymc.eddy.argparse.ArgumentParser.parse_args',
        return_value=Namespace(file='mcnp_examples/nonexistent_file.txt', scaling_factor=None),
    )
    # act, assert
    with pytest.raises(AssertionError):
        eddy.main()
