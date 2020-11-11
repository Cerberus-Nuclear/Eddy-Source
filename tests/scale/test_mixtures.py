
import pytest
from eddymc.scale import mixtures


@pytest.fixture
def ce_file(tmpdir):
    with open('./scale_examples/cylinder_ce.out', 'r') as f:
        file = f.readlines()
    return file


@pytest.fixture
def multigroup_file(tmpdir):
    with open('./scale_examples/cylinder_multigroup.out', 'r') as f:
        file = f.readlines()
    return file


@pytest.fixture
def single_mixture_ce(tmpdir):
    return [
        ' mixture =     1          density(g/cc) =  7.8600              temperature(K) =   293.0\n',
        '    nuclide   atom-dens.   wgt. frac.      za      awt        title        temp\n',
        '      24050  7.11730E-04  7.51005E-03     24050    49.9460     cr-50         293.00\n',
        '      24052  1.37250E-02  1.50607E-01     24052    51.9405     cr-52         293.00\n',
        '      24053  1.55630E-03  1.74065E-02     24053    52.9407     cr-53         293.00\n',
        '      24054  3.87397E-04  4.41454E-03     24054    53.9389     cr-54         293.00\n',
        '      26054  3.66661E-03  4.17829E-02     26054    53.9396     fe-54         293.00\n',
        '      26056  5.75579E-02  6.80165E-01     26056    55.9349     fe-56         293.00\n',
        '      26057  1.32926E-03  1.59889E-02     26057    56.9354     fe-57         293.00\n',
        '      26058  1.76900E-04  2.16513E-03     26058    57.9333     fe-58         293.00\n',
        '      28058  4.38990E-03  5.37310E-02     28058    57.9353     ni-58         293.00\n',
        '      28060  1.69098E-03  2.14099E-02     28060    59.9308     ni-60         293.00\n',
        '      28061  7.35058E-05  9.46209E-04     28061    60.9311     ni-61         293.00\n',
        '      28062  2.34369E-04  3.06631E-03     28062    61.9283     ni-62         293.00\n',
        '      28064  5.96868E-05  8.06113E-04     28064    63.9280     ni-64         293.00\n',
    ]


@pytest.fixture
def ce_table(tmpdir):
    return [
        '                                        mixing table\n',
        '\n',
        ' mixture =     1          density(g/cc) =  7.8600              temperature(K) =   293.0\n',
        '    nuclide   atom-dens.   wgt. frac.      za      awt        title        temp\n',
        '      24050  7.11730E-04  7.51005E-03     24050    49.9460     cr-50         293.00\n',
        '      24052  1.37250E-02  1.50607E-01     24052    51.9405     cr-52         293.00\n',
        '      24053  1.55630E-03  1.74065E-02     24053    52.9407     cr-53         293.00\n',
        '      24054  3.87397E-04  4.41454E-03     24054    53.9389     cr-54         293.00\n',
        '      26054  3.66661E-03  4.17829E-02     26054    53.9396     fe-54         293.00\n',
        '      26056  5.75579E-02  6.80165E-01     26056    55.9349     fe-56         293.00\n',
        '      26057  1.32926E-03  1.59889E-02     26057    56.9354     fe-57         293.00\n',
        '      26058  1.76900E-04  2.16513E-03     26058    57.9333     fe-58         293.00\n',
        '      28058  4.38990E-03  5.37310E-02     28058    57.9353     ni-58         293.00\n',
        '      28060  1.69098E-03  2.14099E-02     28060    59.9308     ni-60         293.00\n',
        '      28061  7.35058E-05  9.46209E-04     28061    60.9311     ni-61         293.00\n',
        '      28062  2.34369E-04  3.06631E-03     28062    61.9283     ni-62         293.00\n',
        '      28064  5.96868E-05  8.06113E-04     28064    63.9280     ni-64         293.00\n',
        '\n',
        ' mixture =     2          density(g/cc) = 0.12050E-02          temperature(K) =   293.0\n',
        '    nuclide   atom-dens.   wgt. frac.      za      awt        title        temp\n',
        '       6000  7.49187E-09  1.24000E-04      6000    12.0107     c         293.00\n',
        '       7014  3.89870E-05  7.52324E-01      7014    14.0031     n-14         293.00\n',
        '       7015  1.42431E-07  2.94416E-03      7015    15.0001     n-15         293.00\n',
        '       8016  1.04871E-05  2.31153E-01      8016    15.9949     o-16         293.00\n',
        '       8017  3.99481E-09  9.35803E-05      8017    16.9991     o-17         293.00\n',
        '       8018  2.15509E-08  5.34540E-04      8018    17.9992     o-18         293.00\n',
        '      18036  7.84073E-10  3.88624E-05     18036    35.9675     ar-36         293.00\n',
        '      18038  1.47261E-10  7.70385E-06     18038    37.9627     ar-38         293.00\n',
        '      18040  2.32077E-07  1.27804E-02     18040    39.9624     ar-40         293.00\n',
        '\n',
        ' mixture =     3          density(g/cc) =  1.9895              temperature(K) =   293.0\n',
        '    nuclide   atom-dens.   wgt. frac.      za      awt        title        temp\n',
        '      13027  1.48301E-02  3.33969E-01     13027    26.9815     al-27         293.00\n',
        '      14028  4.09196E-04  9.55494E-03     14028    27.9769     si-28         293.00\n',
        '      14029  2.07875E-05  5.02741E-04     14029    28.9765     si-29         293.00\n',
        '      14030  1.37193E-05  3.43218E-04     14030    29.9738     si-30         293.00\n',
        '      24050  9.45040E-05  3.93956E-03     24050    49.9460     cr-50         293.00\n',
        '      24052  1.82242E-03  7.90042E-02     24052    51.9405     cr-52         293.00\n',
        '      24053  2.06647E-04  9.13094E-03     24053    52.9407     cr-53         293.00\n',
        '      24054  5.14389E-05  2.31574E-03     24054    53.9389     cr-54         293.00\n',
        '      26054  4.86672E-04  2.19099E-02     26054    53.9396     fe-54         293.00\n',
        '      26056  7.63971E-03  3.56662E-01     26056    55.9349     fe-56         293.00\n',
        '      26057  1.76434E-04  8.38419E-03     26057    56.9354     fe-57         293.00\n',
        '      26058  2.34802E-05  1.13534E-03     26058    57.9333     fe-58         293.00\n',
        '      28058  5.82673E-04  2.81751E-02     28058    57.9353     ni-58         293.00\n',
        '      28060  2.24445E-04  1.12268E-02     28060    59.9308     ni-60         293.00\n',
        '      28061  9.75645E-06  4.96166E-04     28061    60.9311     ni-61         293.00\n',
        '      28062  3.11078E-05  1.60789E-03     28062    61.9283     ni-62         293.00\n',
        '      28064  7.92225E-06  4.22703E-04     28064    63.9280     ni-64         293.00\n',
        '      92235  7.51882E-05  1.47501E-02     92235   235.0439     u-235         293.00\n',
        '      92238  5.86203E-04  1.16470E-01     92238   238.0508     u-238         293.00\n',
        '\n',
        '\n',
        '\n',
        '\n',
        '\n',
        ' Cross section preparation time:  5.75 seconds\n',
        ]


@pytest.fixture
def multigroup_table(tmpdir):
    return [
        ' mixture =     1          density(g/cc) = 0.12050E-02          temperature(K) =    293.00',
        '    nuclide    nucmix   atom-dens.   wgt. frac.     za      awt          temp               nuclide title',
        '       6000       1    7.49187E-09  1.23999E-04    6000    12.0107       293.00     c 600 endf/b-7 rel1 rev7 mod0 Mon Jun 16 16:17:50 2014',
        '',
        '       7014       1    3.89870E-05  7.52320E-01    7014    14.0031       293.00     n14 725 endf/b-7 rel1 rev7 mod0 Mon Jun 16 16:18:39 2014',
        '',
        '       7015       1    1.42431E-07  2.94415E-03    7015    15.0001       293.00     n15 728 endf/b-7 rel1 rev7 mod0 Mon Jun 16 16:18:39 2014',
        '',
        '       8016       1    1.04871E-05  2.31152E-01    8016    15.9949       293.00     o16 825 endf/b-7 rel1 rev7 mod4 Mon Jun 16 16:18:40 2014',
        '',
        '       8017       1    3.99481E-09  9.35799E-05    8017    16.9991       293.00     o17 828 endf/b-7 rel1 rev7 mod0 Mon Jun 16 16:18:40 2014',
        '',
        '       8018       1    2.15509E-08  5.39169E-04    8018    18.1551       293.00     Injected O-18 zero cross sections',
        '      18036       1    7.84073E-10  3.88622E-05   18036    35.9675       293.00     ar36 1825 endf/b-7 rel1 rev7 mod0 Mon Jun 16 16:17:47 2014',
        '',
        '      18038       1    1.47261E-10  7.70382E-06   18038    37.9627       293.00     ar38 1831 endf/b-7 rel1 rev7 mod0 Mon Jun 16 16:17:47 2014',
        '',
        '      18040       1    2.32077E-07  1.27804E-02   18040    39.9624       293.00     ar40 1837 endf/b-7 rel1 rev7 mod2 Mon Jun 16 16:17:47 2014',
        ]



def test_get_mixture_data_ce(ce_file):
    # arrange
    file = ce_file
    # act
    output = mixtures.get_mixture_data(file)
    # assert
    assert len(output) == 56


def test_get_mixture_data_multigroup(multigroup_file):
    # arrange
    file = multigroup_file
    # act
    output = mixtures.get_mixture_data(file)
    # assert
    assert len(output) == 181


def test_create_mixtures_ce(ce_table, single_mixture_ce, mocker):
    # arrange
    mixture_table = ce_table
    single_mixture = single_mixture_ce
    mocked_Mixture_init = mocker.patch('eddymc.scale.mixtures.Mixture')
    # act
    mixtures.create_mixtures(mixture_table)
    # assert
    mocked_Mixture_init.assert_called()
    assert mocked_Mixture_init.call_count == 3
    assert mocked_Mixture_init.call_args_list[0].args[0] == single_mixture


def test_create_mixtures_multigroup(multigroup_table, mocker):
    pass


def test_mixture_init_ce_library(single_mixture_ce, mocker):
    pass
    ## arrange
    #mixture_table = single_mixture_ce
    #gv = mocker.patch('eddymc.scale.mixtures.gv')
    #gv.mixture_list = []
    ## act
    #mixtures.Mixture(mixture_table)
    #mixture = gv.mixture_list[0]
    ## assert
    #assert len(gv.mixture_list) == 3
    #assert mixture.number == '1'
    #assert mixture.density == '0.12050E-02'
    #assert len(mixture.isotopes) == 4


def test_mixture_init_multigroup_library(multigroup_table, mocker):
    # arrange
    mixture_table = multigroup_table
    gv = mocker.patch('eddymc.scale.mixtures.gv')
    gv.mixture_list = []
    # act
    mixtures.Mixture(mixture_table)
    mixture = gv.mixture_list[0]
    # assert
    assert len(gv.mixture_list) == 1
    assert mixture.number == '1'
    assert mixture.density == '0.12050E-02'
    assert len(mixture.isotopes) == 9

