
import pytest
from eddymc.scale import mixtures
from tests import scale_examples
try:
    import importlib.resources as pkg_resources
except ImportError:
    import importlib_resources as pkg_resources


@pytest.fixture
def ce_623_file(tmpdir):
    file = pkg_resources.read_text(scale_examples, 'cylinder_ce.out')
    return file.split('\n')


@pytest.fixture
def ce_624_file(tmpdir):
    file = pkg_resources.read_text(scale_examples, 'cylinder_ce_6_2_4.out')
    return file.split('\n')


@pytest.fixture
def multigroup_623_file(tmpdir):
    file = pkg_resources.read_text(scale_examples, 'cylinder_multigroup.out')
    return file.split('\n')


@pytest.fixture
def multigroup_624_file(tmpdir):
    file = pkg_resources.read_text(scale_examples, 'cylinder_multigroup_6_2_4.out')
    return file.split('\n')


@pytest.fixture
def single_mixture_ce_623(tmpdir):
    return [
        " mixture =     1          density(g/cc) =  7.8600              temperature(K) =   293.0",
        "    nuclide   atom-dens.   wgt. frac.      za      awt        title        temp",
        "      24050  7.11730E-04  7.51005E-03     24050    49.9460     cr-50         293.00",
        "      24052  1.37250E-02  1.50607E-01     24052    51.9405     cr-52         293.00",
        "      24053  1.55630E-03  1.74065E-02     24053    52.9407     cr-53         293.00",
        "      24054  3.87397E-04  4.41454E-03     24054    53.9389     cr-54         293.00",
        "      26054  3.66661E-03  4.17829E-02     26054    53.9396     fe-54         293.00",
        "      26056  5.75579E-02  6.80165E-01     26056    55.9349     fe-56         293.00",
        "      26057  1.32926E-03  1.59889E-02     26057    56.9354     fe-57         293.00",
        "      26058  1.76900E-04  2.16513E-03     26058    57.9333     fe-58         293.00",
        "      28058  4.38990E-03  5.37310E-02     28058    57.9353     ni-58         293.00",
        "      28060  1.69098E-03  2.14099E-02     28060    59.9308     ni-60         293.00",
        "      28061  7.35058E-05  9.46209E-04     28061    60.9311     ni-61         293.00",
        "      28062  2.34369E-04  3.06631E-03     28062    61.9283     ni-62         293.00",
        "      28064  5.96868E-05  8.06113E-04     28064    63.9280     ni-64         293.00",
        "",
    ]


@pytest.fixture
def single_mixture_ce_624(tmpdir):
    return [
        " mixture =     1          density(g/cc) =  7.8600              temperature(K) =   293.0",
        "    nuclide   atom-dens.   wgt. frac.      za       awt          temp       title",
        "      24050  7.11730E-04  7.51005E-03     24050    49.9460       293.00     cr-50",
        "      24052  1.37250E-02  1.50607E-01     24052    51.9405       293.00     cr-52",
        "      24053  1.55630E-03  1.74065E-02     24053    52.9407       293.00     cr-53",
        "      24054  3.87397E-04  4.41454E-03     24054    53.9389       293.00     cr-54",
        "      26054  3.66661E-03  4.17829E-02     26054    53.9396       293.00     fe-54",
        "      26056  5.75579E-02  6.80165E-01     26056    55.9349       293.00     fe-56",
        "      26057  1.32926E-03  1.59889E-02     26057    56.9354       293.00     fe-57",
        "      26058  1.76900E-04  2.16513E-03     26058    57.9333       293.00     fe-58",
        "      28058  4.38990E-03  5.37310E-02     28058    57.9353       293.00     ni-58",
        "      28060  1.69098E-03  2.14099E-02     28060    59.9308       293.00     ni-60",
        "      28061  7.35058E-05  9.46209E-04     28061    60.9311       293.00     ni-61",
        "      28062  2.34369E-04  3.06631E-03     28062    61.9283       293.00     ni-62",
        "      28064  5.96868E-05  8.06113E-04     28064    63.9280       293.00     ni-64",
        "",
    ]


@pytest.fixture
def single_mixture_multigroup(tmpdir):
    return [
        " mixture =     1          density(g/cc) =  7.8600              temperature(K) =    293.00",
        "    nuclide    nucmix   atom-dens.   wgt. frac.     za      awt          temp               nuclide title",
        "      24050       1    7.11730E-04  7.51005E-03   24050    49.9460       293.00     cr50 2425 endf/b-7 rel1 rev7 mod5 Mon Jun 16 16:17:53 2014",
        "",
        "      24052       1    1.37250E-02  1.50607E-01   24052    51.9405       293.00     cr52 2431 endf/b-7 rel1 rev7 mod4 Mon Jun 16 16:17:53 2014",
        "",
        "      24053       1    1.55630E-03  1.74065E-02   24053    52.9407       293.00     cr53 2434 endf/b-7 rel1 rev7 mod4 Mon Jun 16 16:17:55 2014",
        "",
        "      24054       1    3.87397E-04  4.41454E-03   24054    53.9389       293.00     cr54 2437 endf/b-7 rel1 rev7 mod5 Mon Jun 16 16:17:55 2014",
        "",
        "      26054       1    3.66661E-03  4.17829E-02   26054    53.9396       293.00     fe54 2625 endf/b-7 rel1 rev7 mod5 Mon Jun 16 16:17:58 2014",
        "",
        "      26056       1    5.75579E-02  6.80165E-01   26056    55.9349       293.00     fe56 2631 endf/b-7 rel1 rev7 mod4 Mon Jun 16 16:17:58 2014",
        "",
        "      26057       1    1.32926E-03  1.59889E-02   26057    56.9354       293.00     fe57 2634 endf/b-7 rel1 rev7 mod4 Mon Jun 16 16:17:58 2014",
        "",
        "      26058       1    1.76900E-04  2.16513E-03   26058    57.9333       293.00     fe58 2637 endf/b-7 rel1 rev7 mod0 Mon Jun 16 16:17:58 2014",
        "",
        "      28058       1    4.38990E-03  5.37310E-02   28058    57.9353       293.00     ni58 2825 endf/b-7 rel1 rev7 mod5 Mon Jun 16 16:18:39 2014",
        "",
        "      28060       1    1.69098E-03  2.14099E-02   28060    59.9308       293.00     ni60 2831 endf/b-7 rel1 rev7 mod4 Mon Jun 16 16:18:39 2014",
        "",
        "      28061       1    7.35058E-05  9.46209E-04   28061    60.9311       293.00     ni61 2834 endf/b-7 rel1 rev7 mod5 Mon Jun 16 16:18:39 2014",
        "",
        "      28062       1    2.34369E-04  3.06631E-03   28062    61.9283       293.00     ni62 2837 endf/b-7 rel1 rev7 mod5 Mon Jun 16 16:18:39 2014",
        "",
        "      28064       1    5.96868E-05  8.06113E-04   28064    63.9280       293.00     ni64 2843 endf/b-7 rel1 rev7 mod4 Mon Jun 16 16:18:39 2014",
        "",
        "",
    ]


#####################################################################
# End of Fixtures --------------------------------------------------#
#####################################################################

def test_get_mixture_data_ce(ce_623_file, ce_624_file):
    # arrange
    scale_623_file = ce_623_file
    scale_624_file = ce_624_file
    # act
    output_623 = mixtures.get_mixture_data(scale_623_file)
    output_624 = mixtures.get_mixture_data(scale_624_file)
    # assert
    assert len(output_623) == 57
    assert len(output_624) == 57
    print(output_624)


def test_get_mixture_data_multigroup(multigroup_623_file, multigroup_624_file):
    # arrange
    scale_623_file = multigroup_623_file
    scale_624_file = multigroup_624_file
    # act
    output_623 = mixtures.get_mixture_data(scale_623_file)
    output_624 = mixtures.get_mixture_data(scale_624_file)
    # assert
    assert len(output_623) == 100
    assert len(output_624) == 100


def test_create_mixtures_ce_623(ce_623_file, single_mixture_ce_623, mocker):
    # arrange
    mixtures_623 = mixtures.get_mixture_data(ce_623_file)
    mocked_Mixture_init = mocker.patch('eddymc.scale.mixtures.Mixture')
    # act
    mixtures.create_mixtures(mixtures_623)
    # assert
    mocked_Mixture_init.assert_called()
    assert mocked_Mixture_init.call_count == 3
    assert mocked_Mixture_init.call_args_list[0][0][0] == single_mixture_ce_623


def test_create_mixtures_ce_624(ce_624_file, single_mixture_ce_624, mocker):
    # arrange
    mixtures_624 = mixtures.get_mixture_data(ce_624_file)
    mocked_Mixture_init = mocker.patch('eddymc.scale.mixtures.Mixture')
    # act
    mixtures.create_mixtures(mixtures_624)
    # assert
    mocked_Mixture_init.assert_called()
    assert mocked_Mixture_init.call_count == 3
    assert mocked_Mixture_init.call_args_list[0][0][0] == single_mixture_ce_624



def test_create_mixtures_multigroup_623(multigroup_623_file, single_mixture_multigroup, mocker):
    # arrange
    mixtures_623 = mixtures.get_mixture_data(multigroup_623_file)
    mocked_Mixture_init = mocker.patch('eddymc.scale.mixtures.Mixture')
    # act
    mixtures.create_mixtures(mixtures_623)
    # assert
    mocked_Mixture_init.assert_called()
    assert mocked_Mixture_init.call_count == 3      # checks correct number of mixtures found
    assert mocked_Mixture_init.call_args_list[0][0][0] == single_mixture_multigroup  #checks first mixture is correct


def test_mixture_init_ce_623(single_mixture_ce_623):
    # arrange
    # act
    mix_1 = mixtures.Mixture(single_mixture_ce_623)
    # assert
    assert mix_1
    assert type(mix_1) == mixtures.Mixture
    assert mix_1.number == '1'
    assert mix_1.density == '7.8600'
    assert len(mix_1.isotopes) == 13
    assert len(mix_1.isotopes) == 13
    assert mix_1.isotopes[24050]["title"] == 'Cr-50'
    assert mix_1.isotopes[28061]["atom-density"] == 7.35058E-05
    assert mix_1.isotopes[26056]["atomic weight"] == 55.9349


def test_mixture_init_ce_624(single_mixture_ce_624):
    # arrange
    # act
    mix_1 = mixtures.Mixture(single_mixture_ce_624)
    # assert
    assert mix_1
    assert type(mix_1) == mixtures.Mixture
    assert mix_1.number == '1'
    assert mix_1.density == '7.8600'
    assert len(mix_1.isotopes) == 13
    assert mix_1.isotopes[24050]["title"] == 'Cr-50'
    assert mix_1.isotopes[28061]["atom-density"] == 7.35058E-05
    assert mix_1.isotopes[26056]["atomic weight"] == 55.9349


def test_mixture_init_multigroup(single_mixture_multigroup):
    # arrange
    # act
    mix_1 = mixtures.Mixture(single_mixture_multigroup)
    # assert
    assert mix_1
    assert type(mix_1) == mixtures.Mixture
    assert mix_1.number == '1'
    assert mix_1.density == '7.8600'
    assert len(mix_1.isotopes) == 13
    assert len(mix_1.isotopes) == 13
    assert mix_1.isotopes[24050]["title"] == 'Cr50'
    assert mix_1.isotopes[28061]["atom-density"] == 7.35058E-05
    assert mix_1.isotopes[26056]["atomic weight"] == 55.9349
