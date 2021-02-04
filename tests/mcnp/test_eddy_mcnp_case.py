""" To run: just call python -m pytest while in this directory
or add a configuration in pycharm
"""

import pytest
from eddymc.mcnp.eddy_mcnp_case import EddyMCNPCase
from tests import mcnp_examples

try:
    import importlib.resources as pkg_resources
except ImportError:
    import importlib_resources as pkg_resources


class MockEddyMCNPCase(EddyMCNPCase):
    def __init__(self, filepath, scaling_factor, file, crit_case=False):
        self.filepath = filepath
        self.name = filepath.replace('\\', '/').split('/')[-1]
        self.scaling_factor = scaling_factor
        self.file = file
        self.crit_case = crit_case


@pytest.fixture
def simple_case(f2_file, tmpdir):
    return MockEddyMCNPCase(
        filepath="mcnp_examples/F2.out",
        scaling_factor=1234,
        file=f2_file,
        crit_case=False)


@pytest.fixture
def crit_case(crit_file, tmpdir):
    return MockEddyMCNPCase(
        filepath="mcnp_examples/Criticality.out",
        file=crit_file,
        scaling_factor=1,
        crit_case=True
    )


@pytest.fixture
def f2_file(tmpdir):
    f2 = pkg_resources.read_text(mcnp_examples, 'F2.out')
    return f2.split('\n')


@pytest.fixture
def f4_file(tmpdir):
    # noinspection PyTypeChecker
    f4 = pkg_resources.read_text(mcnp_examples, 'F4.out')
    return f4.split('\n')


@pytest.fixture
def f5_file(tmpdir):
    # noinspection PyTypeChecker
    f5 = pkg_resources.read_text(mcnp_examples, 'F5.out')
    return f5.split('\n')


@pytest.fixture
def f4_f5_file(tmpdir):
    # noinspection PyTypeChecker
    f4_f5 = pkg_resources.read_text(mcnp_examples, 'F4_F5_param.out')
    return f4_f5.split('\n')


@pytest.fixture
def f6_file(tmpdir):
    # noinspection PyTypeChecker
    f6 = pkg_resources.read_text(mcnp_examples, 'F6.out')
    return f6.split('\n')


@pytest.fixture
def lost_particle_file(tmpdir):
    file = pkg_resources.read_text(mcnp_examples, 'lost_particles.out')
    return file.split('\n')


@pytest.fixture
def failed_case(tmpdir):
    file = pkg_resources.read_text(mcnp_examples, 'fatal_error.out')
    return file.split('\n')


@pytest.fixture
def dumps_file(tmpdir):
    file = pkg_resources.read_text(mcnp_examples, 'Dumps.out')
    return file.split('\n')


@pytest.fixture
def crit_file(tmpdir):
    file = pkg_resources.read_text(mcnp_examples, 'Criticality.out')
    return file.split('\n')


def test_object_created(f2_file):
    # arrange
    path = "mcnp_examples/F2.out"
    sf = 1234
    # act
    case = EddyMCNPCase(filepath=path, scaling_factor=sf, file=f2_file, crit_case=False)
    # assert
    assert case


def test_get_date_time(simple_case):
    # act
    rundate, runtime = simple_case.get_date_time()
    # assert
    assert type(rundate) == str
    assert type(runtime) == str


def test_get_runtime(simple_case):
    # arrange
    # act
    ctme, nps = simple_case.get_runtime()
    # assert
    # This case (F2.out) has ctme but to nps card
    assert type(ctme) == str
    assert nps is None


def test_get_input(simple_case):
    # arrange
    # act
    actual_input = simple_case.get_input()
    # assert
    assert actual_input[0] == 'Test MCNP example'
    assert actual_input[-6] == 'RAND SEED=7048155456235'
    assert actual_input[-1] == ''
    assert len(actual_input) == 191


def test_get_parameters_positive(simple_case):
    # arrange
    parameter_input = [r"Test MCNP example",
                       r"c",
                       r"c ==============================================================================",
                       r"c",
                       r"c",
                       r"c                 _______     _______ _      ____  _   _ ______",
                       r"c                / ____\ \   / / ____| |    / __ \| \ | |  ____|",
                       r"c               | |     \ \_/ / |    | |   | |  | |  \| | |__",
                       r"c               | |      \   /| |    | |   | |  | | . ` |  __|",
                       r"c               | |____   | | | |____| |___| |__| | |\  | |____",
                       r"c                \_____|  |_|  \_____|______\____/|_| \_|______|",
                       r"c",
                       r"c",
                       r"c",
                       r"c                                Version 0.19.2",
                       r"c",
                       r"c ######################### Cerberus Nuclear 2020 ############################",
                       r"c",
                       r"c",
                       r"c",
                       r"c",
                       r"c     USING THE FOLLOWING VARIABLES:",
                       r"c               width     =   10.00000",
                       r"c",
                       r"c",
                       r"c =============================== START TITLE ==================================",
                       r"c ==============================================================================",
                       r"c   MCNP example Case - concentric spheres",
                       r"c",
                       r"c",
                       r"c <width=10>",
                       r"c",
                       r"c ==============================================================================",
                       r"c ============================= START CELL SECTION =============================",
                       r"c ==============================================================================",
                       ]
    case = simple_case
    case.mcnp_input = parameter_input
    # act
    variables = simple_case.get_parameters()
    # assert
    assert variables['width'] == 10


def test_get_parameters_negative(simple_case):
    # arrange
    no_parameter_input = [r"Test MCNP example",
                          r"c",
                          r"c ==============================================================================",
                          r"c",
                          r"c",
                          r"c                 _______     _______ _      ____  _   _ ______",
                          r"c                / ____\ \   / / ____| |    / __ \| \ | |  ____|",
                          r"c               | |     \ \_/ / |    | |   | |  | |  \| | |__",
                          r"c               | |      \   /| |    | |   | |  | | . ` |  __|",
                          r"c               | |____   | | | |____| |___| |__| | |\  | |____",
                          r"c                \_____|  |_|  \_____|______\____/|_| \_|______|",
                          r"c",
                          r"c",
                          r"c",
                          r"c                                Version 0.19.2",
                          r"c",
                          r"c ######################### Cerberus Nuclear 2020 ############################",
                          r"c",
                          r"c",
                          r"c",
                          r"c",
                          r"c     USING THE FOLLOWING VARIABLES:",
                          r"c",
                          r"c",
                          r"c =============================== START TITLE ==================================",
                          r"c ==============================================================================",
                          r"c   MCNP example Case - concentric spheres",
                          r"c",
                          r"c",
                          r"c <width=10>",
                          r"c",
                          r"c ==============================================================================",
                          r"c ============================= START CELL SECTION =============================",
                          r"c ==============================================================================", ]
    case = simple_case
    case.mcnp_input = no_parameter_input
    # act
    variables = simple_case.get_parameters()
    # assert
    # should be an empty dict
    assert not variables


def test_check_lost_particles_positive(lost_particle_file):
    # arrange
    case = MockEddyMCNPCase(
        filepath="mcnp_examples/lost_particles.out",
        scaling_factor=1234,
        file=lost_particle_file,
        crit_case=False,
    )
    # act
    lost_particles = case.check_lost_particles()
    # assert
    assert lost_particles is True


def test_check_lost_particles_negative(simple_case):
    # arrange
    # act
    lost_particles = simple_case.check_lost_particles()
    # assert
    assert lost_particles is False


def test_get_fatal_errors_present(failed_case):
    # arrange
    case = MockEddyMCNPCase(
        filepath="mcnp_examples/fatal_error.out",
        scaling_factor=1234,
        file=failed_case,
        crit_case=False,
    )
    # act
    fatal_errors = case.get_fatal_errors()
    # assert
    assert len(fatal_errors) == 3
    assert fatal_errors[0] == "Surface       -16 not found for cell         4 card."
    assert fatal_errors[1] == "Surface      -16 of cell        4 is not defined."
    assert fatal_errors[2] == "1 tally volumes or areas were not input nor calculated."


def test_get_fatal_errors_not_present(simple_case):
    # arrange
    # act
    fatal_errors = simple_case.get_fatal_errors()
    # assert
    assert fatal_errors == []   # empty list


def test_get_warnings(simple_case):
    # arrange
    # act
    warnings = simple_case.get_warnings()
    # assert
    assert len(warnings) == 4
    assert warnings[0] == "1 materials had unnormalized fractions. print table 40."
    assert warnings[1] == "8017.80c lacks gamma-ray production cross sections."
    assert warnings[2] == "Material        1 has been set to a conductor."
    assert warnings[3] == "2 photons from neutron collisions were created below a local photon energy cutoff and were not followed."


def test_get_comments(simple_case):
    # arrange
    # act
    comments = simple_case.get_comments()
    # assert
    assert len(comments) == 7
    assert comments[0] == "Physics models disabled."
    assert comments[6] == "Setting up hash-based fast table search for xsec tables"


def test_get_duplicate_surfaces(dumps_file):
    # arrange
    case = MockEddyMCNPCase(
        filepath="mcnp_examples/Dumps.out",
        scaling_factor=1234,
        file=dumps_file,
        crit_case=False,
    )
    # act
    duplicate_surfaces = case.get_duplicate_surfaces()
    # assert
    assert len(duplicate_surfaces) == 8
    assert duplicate_surfaces[0] == "Surface       34   and surface      501   are the same.      501   will be deleted."


def test_get_keff(crit_file, crit_case):
    # arrange
    # act
    k_eff = crit_case.get_k_eff()
    # assert
    assert k_eff['first half k_eff'] == 0.78280
    assert k_eff['first half stdev'] == 0.00061
    assert k_eff['second half k_eff'] == 0.78235
    assert k_eff['second half stdev'] == 0.00067
    assert k_eff['final k_eff'] == 0.78257
    assert k_eff['final stdev'] == 0.00045


def test_get_active_cycles(crit_file, crit_case):
    # arrange
    # act
    cycles = crit_case.get_active_cycles()
    # assert
    assert cycles["inactive"] == 16
    assert cycles["active"] == 184


def test_get_cell_data(simple_case):
    # arrange
    # act
    cell_section = simple_case.get_cell_data()
    # assert
    assert len(cell_section) == 12


def test_create_cells_calls_cell_init(simple_case, mocker):
    # arrange
    c = simple_case
    c.cell_data = [
        "1cells                                                                                                  print table 60",
        "",
        "                               atom        gram                                            neutron    photon     photon wt             ",
        "              cell      mat   density     density     volume       mass            pieces importance importance generation             ",
        "",
        "        1        1        1  8.83440E-02 7.81000E+00 4.18879E+00 3.27145E+01           1  1.0000E+00 1.0000E+00 -1.000E+00             ",
        "        2        2        2  5.02980E-05 1.20500E-03 4.06019E+03 4.89253E+00           1  1.0000E+00 1.0000E+00 -1.000E+00             ",
        "        3        3        2  5.02980E-05 1.20500E-03 1.24411E+02 1.49916E-01           1  1.0000E+00 1.0000E+00 -1.000E+00             ",
        "        4        4        2  5.02980E-05 1.20500E-03 1.38649E+03 1.67072E+00           1  1.0000E+00 1.0000E+00 -1.000E+00             ",
        "        5        5        0  0.00000E+00 0.00000E+00 0.00000E+00 0.00000E+00           0  0.0000E+00 0.0000E+00 -1.000E+00             ",
        "",
        " total                                               5.57528E+03 3.94276E+01",
        ]
    mocker.patch('eddymc.mcnp.eddy_mcnp_case.EddyMCNPCase.get_particle_importance', return_value=1)
    mock_cell_init = mocker.patch('eddymc.mcnp.cells.Cell.__init__', return_value=None)
    # act
    c.create_cells()
    # assert
    assert mock_cell_init.call_count == 5


def test_get_tallies_f2(simple_case):
    # arrange
    c = simple_case
    # act
    c.tally_list, c.f_types, c.F2_tallies, c.F4_tallies, c.F5_tallies, c.F6_tallies = c.get_tallies()
    # assert
    assert len(c.tally_list) == 3
    assert c.f_types == ['F2']
    assert len(c.F2_tallies['neutrons']) == 2
    assert len(c.F2_tallies['photons']) == 1
    assert len(c.F2_tallies['electrons']) == 0


def test_get_tallies_f4(f4_file):
    # arrange
    c = MockEddyMCNPCase(
        filepath="mcnp_examples/F4.out",
        scaling_factor=1234,
        file=f4_file,
        crit_case=False)
    # act
    c.tally_list, c.f_types, c.F2_tallies, c.F4_tallies, c.F5_tallies, c.F6_tallies = c.get_tallies()
    # assert
    assert len(c.tally_list) == 3
    assert c.f_types == ['F4']
    assert len(c.F4_tallies['neutrons']) == 1
    assert len(c.F4_tallies['photons']) == 2
    assert len(c.F4_tallies['electrons']) == 0


def test_get_tallies_f5(f5_file):
    # arrange
    c = MockEddyMCNPCase(
        filepath="mcnp_examples/F5.out",
        scaling_factor=1234,
        file=f5_file,
        crit_case=False)
    # act
    c.tally_list, c.f_types, c.F2_tallies, c.F4_tallies, c.F5_tallies, c.F6_tallies = c.get_tallies()
    # assert
    assert len(c.tally_list) == 3
    assert c.f_types == ['F5']
    assert len(c.F5_tallies['neutrons']) == 1
    assert len(c.F5_tallies['photons']) == 2
    assert len(c.F5_tallies['electrons']) == 0


def test_get_tallies_f6(f6_file):
    # arrange
    c = MockEddyMCNPCase(
        filepath="mcnp_examples/F6.out",
        scaling_factor=1234,
        file=f6_file,
        crit_case=False)
    # act
    c.tally_list, c.f_types, c.F2_tallies, c.F4_tallies, c.F5_tallies, c.F6_tallies = c.get_tallies()
    # assert
    assert len(c.tally_list) == 6
    assert c.f_types == ['F6', 'F6+']
    assert len(c.F6_tallies['neutrons']) == 2
    assert len(c.F6_tallies['photons']) == 2
    assert len(c.F6_tallies['electrons']) == 0
    assert len(c.F6_tallies['Collision Heating']) == 2


def test_get_tallies_adds_f2_to_types_list(simple_case):
    # arrange
    c = simple_case
    # act
    c.tally_list, c.f_types, c.F2_tallies, c.F4_tallies, c.F5_tallies, c.F6_tallies = c.get_tallies()
    # assert
    assert "F2" in c.f_types
    assert "F4" not in c.f_types
    assert "F5" not in c.f_types
    assert "F6" not in c.f_types
    assert "F6+" not in c.f_types


def test_get_tallies_adds_f4_to_types_list(f4_file):
    # arrange
    c = MockEddyMCNPCase(
        filepath="mcnp_examples/F4.out",
        scaling_factor=1,
        file=f4_file,
        crit_case=False
    )
    # act
    c.tally_list, c.f_types, c.F2_tallies, c.F4_tallies, c.F5_tallies, c.F6_tallies = c.get_tallies()
    # assert
    assert "F2" not in c.f_types
    assert "F4" in c.f_types
    assert "F5" not in c.f_types
    assert "F6" not in c.f_types
    assert "F6+" not in c.f_types


def test_get_tallies_adds_f5_to_types_list(f5_file):
    # arrange
    c = MockEddyMCNPCase(
        filepath="mcnp_examples/F5.out",
        scaling_factor=1,
        file=f5_file,
        crit_case=False
    )
    # act
    c.tally_list, c.f_types, c.F2_tallies, c.F4_tallies, c.F5_tallies, c.F6_tallies = c.get_tallies()
    # assert
    assert "F2" not in c.f_types
    assert "F4" not in c.f_types
    assert "F5" in c.f_types
    assert "F6" not in c.f_types
    assert "F6+" not in c.f_types


def test_get_tallies_adds_f6_to_types_list(f6_file):
    # arrange
    c = MockEddyMCNPCase(
        filepath="mcnp_examples/F6.out",
        scaling_factor=1,
        file=f6_file,
        crit_case=False
    )
    # act
    c.tally_list, c.f_types, c.F2_tallies, c.F4_tallies, c.F5_tallies, c.F6_tallies = c.get_tallies()
    # assert
    assert "F2" not in c.f_types
    assert "F4" not in c.f_types
    assert "F5" not in c.f_types
    assert "F6" in c.f_types
    assert "F6+" in c.f_types
