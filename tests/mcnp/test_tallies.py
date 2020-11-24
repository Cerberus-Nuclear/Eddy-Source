
""" To run: just call python -m pytest while in this directory
or add a configuration in pycharm
"""

import pytest
from eddymc.mcnp import tallies
from tests import mcnp_examples
try:
    import importlib.resources as pkg_resources
except ImportError:
    import importlib_resources as pkg_resources


@pytest.fixture
def f2_file(tmpdir):
    f2 = pkg_resources.read_text(mcnp_examples, 'F2.out')
    return f2.split('\n')


@pytest.fixture
def f4_file(tmpdir):
    f4 = pkg_resources.read_text(mcnp_examples, 'F4.out')
    return f4.split('\n')


@pytest.fixture
def f5_file(tmpdir):
    f5 = pkg_resources.read_text(mcnp_examples, 'F5.out')
    return f5.split('\n')


@pytest.fixture
def f4_f5_file(tmpdir):
    f4_f5 = pkg_resources.read_text(mcnp_examples, 'F4_F5_param.out')
    return f4_f5.split('\n')


@pytest.fixture
def f6_file(tmpdir):
    f6 = pkg_resources.read_text(mcnp_examples, 'F6.out')
    return f6.split('\n')


@pytest.fixture
def f2_tally_data(tmpdir):
    tally_data = [
        "1tally        2        nps =     5294245",
        "           tally type 2    particle flux averaged over a surface.                              ",
        "           particle(s): neutrons ",
        "           this tally is modified by dose function DE2 and DF2.",
        "",
        "           areas   ",
        "                surface:       2                                                                                   ",
        "                         1.23163E+03",
        " ",
        " surface  2                                                                                                                            ",
        "                 1.11143E-03 0.0001",
        "",
        "",
        " ===================================================================================================================================",
        "",
        "           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc) bin of tally        2",
        "",
        " tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-",
        " behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope",
        "",
        " desired      random       <0.10      yes      1/sqrt(nps)       <0.10      yes        1/nps           constant    random      >3.00",
        " observed     random        0.00      yes          yes            0.00      yes         yes            constant    random       4.73",
        " passed?        yes          yes      yes          yes             yes      yes         yes               yes        yes         yes",
        "",
        " ===================================================================================================================================",
        "",
        "",
        " this tally meets the statistical criteria used to form confidence intervals: check the tally fluctuation chart to verify.",
        " the results in other bins associated with this tally may not meet these statistical criteria.",
        "",
        " ----- estimated confidence intervals:  -----",
        "",
        " estimated asymmetric confidence interval(1,2,3 sigma): 1.1114E-03 to 1.1114E-03; 1.1114E-03 to 1.1114E-03; 1.1114E-03 to 1.1114E-03",
        " estimated  symmetric confidence interval(1,2,3 sigma): 1.1114E-03 to 1.1114E-03; 1.1114E-03 to 1.1114E-03; 1.1114E-03 to 1.1114E-03",
        "",
        "1analysis of the results in the tally fluctuation chart bin (tfc) for tally 2 with nps = 5294245             print table 160",
        "",
        "",
        " normed average tally per history  = 1.11143E-03          unnormed average tally per history  = 1.36887E+00",
        " estimated tally relative error    = 0.0000               estimated variance of the variance  = 0.0000",
        " relative error from zero tallies  = 0.0000               relative error from nonzero scores  = 0.0000",
        "",
        " number of nonzero history tallies =     5294244          efficiency for the nonzero tallies  = 1.0000",
        " history number of largest  tally  =     2031173          largest  unnormalized history tally = 2.49461E+01",
        " (largest  tally)/(average tally)  = 1.82238E+01          (largest  tally)/(avg nonzero tally)= 1.82238E+01",
        "",
        " (confidence interval shift)/mean  = 0.0000               shifted confidence interval center  = 1.11143E-03",
        "",
        "",
        " if the largest  history score sampled so far were to occur on the next history, the tfc bin quantities would change as follows:",
        "",
        "      estimated quantities           value at nps           value at nps+1           value(nps+1)/value(nps)-1.",
        "",
        "      mean                            1.11143E-03             1.11143E-03                     0.000003",
        "      relative error                  0.00000E+00             0.00000E+00                     0.000000",
        "      variance of the variance        0.00000E+00             0.00000E+00                     0.000000",
        "      shifted center                  1.11143E-03             1.11143E-03                     0.000000",
        "      figure of merit                 1.00000E+30             1.00000E+30                     0.000000",
        "",
        " the estimated inverse power slope of the 200 largest  tallies starting at 3.89990E+00 is 4.7311",
        " the large score tail of the empirical history score probability density function appears to have no unsampled regions.",
        "",
        " relative error is 0! fom and f(x) signal-to-noise ratio are both undefined. histories/minute = 5.169E+06",
        "",
        ]
    return tally_data


@pytest.fixture
def f4_tally_data(tmpdir):
    tally_data = [
        "1tally        4        nps =     8473614",
        "           tally type 4    track length estimate of particle flux.                             ",
        "           particle(s): neutrons ",
        "           this tally is modified by dose function DE4 and DF4.",
        "",
        "           volumes ",
        "                   cell:       3                                                                                   ",
        "                         1.24411E+02",
        " ",
        " cell  3                                                                                                                               ",
        "                 1.10032E-03 0.0001",
        "",
        "",
        " ===================================================================================================================================",
        "",
        "           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc) bin of tally        4",
        "",
        " tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-",
        " behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope",
        "",
        " desired      random       <0.10      yes      1/sqrt(nps)       <0.10      yes        1/nps           constant    random      >3.00",
        " observed     random        0.00      yes          yes            0.00      yes         yes            constant    random       3.30",
        " passed?        yes          yes      yes          yes             yes      yes         yes               yes        yes         yes",
        "",
        " ===================================================================================================================================",
        "",
        "",
        " this tally meets the statistical criteria used to form confidence intervals: check the tally fluctuation chart to verify.",
        " the results in other bins associated with this tally may not meet these statistical criteria.",
        "",
        " ----- estimated confidence intervals:  -----",
        "",
        " estimated asymmetric confidence interval(1,2,3 sigma): 1.1003E-03 to 1.1003E-03; 1.1003E-03 to 1.1003E-03; 1.1003E-03 to 1.1003E-03",
        " estimated  symmetric confidence interval(1,2,3 sigma): 1.1003E-03 to 1.1003E-03; 1.1003E-03 to 1.1003E-03; 1.1003E-03 to 1.1003E-03",
        "",
        "1analysis of the results in the tally fluctuation chart bin (tfc) for tally 4 with nps = 8473614             print table 160",
        "",
        "",
        " normed average tally per history  = 1.10032E-03          unnormed average tally per history  = 1.36893E-01",
        " estimated tally relative error    = 0.0000               estimated variance of the variance  = 0.0000",
        " relative error from zero tallies  = 0.0000               relative error from nonzero scores  = 0.0000",
        "",
        " number of nonzero history tallies =     8473613          efficiency for the nonzero tallies  = 1.0000",
        " history number of largest  tally  =     7039011          largest  unnormalized history tally = 3.55161E+00",
        " (largest  tally)/(average tally)  = 2.59445E+01          (largest  tally)/(avg nonzero tally)= 2.59445E+01",
        "",
        " (confidence interval shift)/mean  = 0.0000               shifted confidence interval center  = 1.10032E-03",
        "",
        "",
        " if the largest  history score sampled so far were to occur on the next history, the tfc bin quantities would change as follows:",
        "",
        "      estimated quantities           value at nps           value at nps+1           value(nps+1)/value(nps)-1.",
        "",
        "      mean                            1.10032E-03             1.10033E-03                     0.000003",
        "      relative error                  0.00000E+00             0.00000E+00                     0.000000",
        "      variance of the variance        0.00000E+00             0.00000E+00                     0.000000",
        "      shifted center                  1.10032E-03             1.10032E-03                     0.000000",
        "      figure of merit                 1.00000E+30             1.00000E+30                     0.000000",
        "",
        " the estimated inverse power slope of the 200 largest  tallies starting at 5.56925E-01 is 3.2972",
        " the large score tail of the empirical history score probability density function appears to have no unsampled regions.",
        "",
        " relative error is 0! fom and f(x) signal-to-noise ratio are both undefined. histories/minute = 8.438E+06",
        "",
        ]
    return tally_data


@pytest.fixture
def f5_tally_data(tmpdir):
    tally_data = [
        "1tally        5        nps =     6767806",
        "           tally type 5    particle flux at a point detector.                                  ",
        "           particle(s): neutrons ",
        "           this tally is modified by dose function DE5 and DF5.",
        " ",
        " detector located at x,y,z = 5.00000E+00 0.00000E+00 0.00000E+00",
        "                 4.38636E-03 0.0003",
        " ",
        " detector located at x,y,z = 5.00000E+00 0.00000E+00 0.00000E+00",
        " uncollided neutron flux",
        "                 3.58745E-03 0.0001",
        " ",
        " detector score diagnostics                  cumulative          tally         cumulative",
        "                                             fraction of         per           fraction of",
        "   times average score     transmissions     transmissions       history       total tally",
        "        1.00000E-01              32209         0.00386        1.52692E-06        0.00048",
        "        1.00000E+00            6311395         0.76076        1.96902E-03        0.61405",
        "        2.00000E+00            1902162         0.98888        1.07467E-03        0.94894",
        "        5.00000E+00              74900         0.99786        1.06067E-04        0.98199",
        "        1.00000E+01              14699         0.99963        4.58831E-05        0.99629",
        "        1.00000E+02               1874         0.99985        1.14282E-05        0.99985",
        "        1.00000E+03                  0         0.99985        0.00000E+00        0.99985",
        "        1.00000E+38                  0         0.99985        0.00000E+00        0.99985",
        " before dd roulette               1250         1.00000        4.87964E-07        1.00000",
        "",
        " average tally per history = 3.20908E-03            largest score = 3.20578E-01",
        " (largest score)/(average tally) = 9.98972E+01      nps of largest score =     2982367",
        "",
        " score contributions by cell",
        "        cell      misses        hits    tally per history    weight per hit",
        "     1     1       14869     8330998       3.20639E-03         2.60476E-03",
        "     2     2         114        6731       2.60671E-06         2.62097E-03",
        "     3     3           5          74       8.55109E-09         7.82056E-04",
        "     4     4          42         686       7.56374E-08         7.46208E-04",
        "       total       15030     8338489       3.20908E-03         2.60460E-03",
        "",
        " score misses",
        "   russian roulette on pd                        0",
        "   psc=0.                                        0",
        "   russian roulette in transmission          15030",
        "   underflow in transmission                     0",
        "   hit a zero-importance cell                    0",
        "   energy cutoff                                 0",
        "",
        "",
        " ===================================================================================================================================",
        "",
        "           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc) bin of tally        5",
        "",
        " tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-",
        " behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope",
        "",
        " desired      random       <0.05      yes      1/sqrt(nps)       <0.10      yes        1/nps           constant    random      >3.00",
        " observed     random        0.00      yes          yes            0.00      yes         yes            constant    random       4.09",
        " passed?        yes          yes      yes          yes             yes      yes         yes               yes        yes         yes",
        "",
        " ===================================================================================================================================",
        "",
        "",
        " this tally meets the statistical criteria used to form confidence intervals: check the tally fluctuation chart to verify.",
        " the results in other bins associated with this tally may not meet these statistical criteria.",
        "",
        " ----- estimated confidence intervals:  -----",
        "",
        " estimated asymmetric confidence interval(1,2,3 sigma): 4.3851E-03 to 4.3876E-03; 4.3838E-03 to 4.3889E-03; 4.3826E-03 to 4.3901E-03",
        " estimated  symmetric confidence interval(1,2,3 sigma): 4.3851E-03 to 4.3876E-03; 4.3838E-03 to 4.3889E-03; 4.3826E-03 to 4.3901E-03",
        "",
        "1analysis of the results in the tally fluctuation chart bin (tfc) for tally 5 with nps = 6767806             print table 160",
        "",
        "",
        " normed average tally per history  = 4.38636E-03          unnormed average tally per history  = 4.38636E-03",
        " estimated tally relative error    = 0.0003               estimated variance of the variance  = 0.0000",
        " relative error from zero tallies  = 0.0000               relative error from nonzero scores  = 0.0003",
        "",
        " number of nonzero history tallies =     6767072          efficiency for the nonzero tallies  = 0.9999",
        " history number of largest  tally  =     2982367          largest  unnormalized history tally = 4.04023E-01",
        " (largest  tally)/(average tally)  = 9.21091E+01          (largest  tally)/(avg nonzero tally)= 9.20991E+01",
        "",
        " (confidence interval shift)/mean  = 0.0000               shifted confidence interval center  = 4.38636E-03",
        "",
        "",
        " if the largest  history score sampled so far were to occur on the next history, the tfc bin quantities would change as follows:",
        "",
        "      estimated quantities           value at nps           value at nps+1           value(nps+1)/value(nps)-1.",
        "",
        "      mean                            4.38636E-03             4.38641E-03                     0.000013",
        "      relative error                  2.87350E-04             2.87661E-04                     0.001083",
        "      variance of the variance        2.77417E-05             3.24159E-05                     0.168490",
        "      shifted center                  4.38636E-03             4.38636E-03                     0.000000",
        "      figure of merit                 1.19954E+07             1.19694E+07                    -0.002163",
        "",
        " the estimated inverse power slope of the 200 largest  tallies starting at 9.05563E-02 is 4.0881",
        " the large score tail of the empirical history score probability density function appears to have no unsampled regions.",
        "",
        " fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (6.703E+06)*( 1.338E+00)**2 = (6.703E+06)*(1.789E+00) = 1.200E+07",
        "",
        ]
    return tally_data


@pytest.fixture
def f6_tally_data(tmpdir):
    tally_data = [
        "1tally      116        nps =   300000000",
        "           tally type 6    track length estimate of heating.            units   mev/gram       ",
        "           particle(s): neutrons ",
        "",
        "           masses  ",
        "                   cell:      23           24                                                                      ",
        "                         2.12237E+04  2.12237E+04",
        " ",
        " cell  23                                                                                                                              ",
        "                 1.98631E-09 0.0069",
        " ",
        " cell  24                                                                                                                              ",
        "                 1.99881E-09 0.0069",
        "",
        "",
        " ===================================================================================================================================",
        "",
        "           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc) bin of tally      116",
        "",
        " tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-",
        " behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope",
        "",
        " desired      random       <0.10      yes      1/sqrt(nps)       <0.10      yes        1/nps           constant    random      >3.00",
        " observed     random        0.01      yes          yes            0.00      yes         yes            constant    random      10.00",
        " passed?        yes          yes      yes          yes             yes      yes         yes               yes        yes         yes",
        "",
        " ===================================================================================================================================",
        "",
        "",
        " this tally meets the statistical criteria used to form confidence intervals: check the tally fluctuation chart to verify.",
        " the results in other bins associated with this tally may not meet these statistical criteria.",
        "",
        " ----- estimated confidence intervals:  -----",
        "",
        " estimated asymmetric confidence interval(1,2,3 sigma): 1.9728E-09 to 2.0000E-09; 1.9591E-09 to 2.0137E-09; 1.9455E-09 to 2.0273E-09",
        " estimated  symmetric confidence interval(1,2,3 sigma): 1.9727E-09 to 1.9999E-09; 1.9590E-09 to 2.0136E-09; 1.9454E-09 to 2.0272E-09",
        "",
        "1analysis of the results in the tally fluctuation chart bin (tfc) for tally 116 with nps = 300000000         print table 160",
        "",
        "",
        " normed average tally per history  = 1.98631E-09          unnormed average tally per history  = 4.21569E-05",
        " estimated tally relative error    = 0.0069               estimated variance of the variance  = 0.0002",
        " relative error from zero tallies  = 0.0025               relative error from nonzero scores  = 0.0064",
        "",
        " number of nonzero history tallies =      166457          efficiency for the nonzero tallies  = 0.0006",
        " history number of largest  tally  =   181112136          largest  unnormalized history tally = 3.99665E+00",
        " (largest  tally)/(average tally)  = 9.48041E+04          (largest  tally)/(avg nonzero tally)= 5.26027E+01",
        "",
        " (confidence interval shift)/mean  = 0.0000               shifted confidence interval center  = 1.98640E-09",
        "",
        "",
        " if the largest  history score sampled so far were to occur on the next history, the tfc bin quantities would change as follows:",
        "",
        "      estimated quantities           value at nps           value at nps+1           value(nps+1)/value(nps)-1.",
        "",
        "      mean                            1.98631E-09             1.98694E-09                     0.000316",
        "      relative error                  6.86482E-03             6.86992E-03                     0.000743",
        "      variance of the variance        2.46172E-04             2.49604E-04                     0.013939",
        "      shifted center                  1.98640E-09             1.98640E-09                     0.000000",
        "      figure of merit                 1.47219E+01             1.47001E+01                    -0.001484",
        "",
        " the estimated slope of the 200 largest  tallies starting at  1.82865E+00 appears to be decreasing at least exponentially.",
        " the large score tail of the empirical history score probability density function appears to have no unsampled regions.",
        "",
        " fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (2.081E+05)*( 8.410E-03)**2 = (2.081E+05)*(7.073E-05) = 1.472E+01",
        "",
        ]
    return tally_data


@pytest.fixture
def f6_plus_tally_data(tmpdir):
    tally_data = [
        "1tally       46        nps =   300000000",
        "           tally type 6+   energy deposition                            units   mev/gram       ",
        "           particle(s): neutrons ",
        "",
        "           masses  ",
        "                   cell:      27           28                                                                      ",
        "                         3.11734E+04  3.11734E+04",
        " ",
        " cell  27                                                                                                                              ",
        "                 4.44113E-09 0.0083",
        " ",
        " cell  28                                                                                                                              ",
        "                 4.46157E-09 0.0082",
        "",
        "",
        " ===================================================================================================================================",
        "",
        "           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc) bin of tally       46",
        "",
        " tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-",
        " behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope",
        "",
        " desired      random       <0.10      yes      1/sqrt(nps)       <0.10      yes        1/nps           constant    random      >3.00",
        " observed     random        0.01      yes          yes            0.00      yes         yes            constant   increase     10.00",
        " passed?        yes          yes      yes          yes             yes      yes         yes               yes         no         yes",
        "",
        " ===================================================================================================================================",
        "",
        "",
        " warning.  the tally in the tally fluctuation chart bin did not pass  1 of the 10 statistical checks.",
        "",
        "1analysis of the results in the tally fluctuation chart bin (tfc) for tally 46 with nps = 300000000          print table 160",
        "",
        "",
        " normed average tally per history  = 4.44113E-09          unnormed average tally per history  = 1.38445E-04",
        " estimated tally relative error    = 0.0083               estimated variance of the variance  = 0.0004",
        " relative error from zero tallies  = 0.0028               relative error from nonzero scores  = 0.0078",
        "",
        " number of nonzero history tallies =      129733          efficiency for the nonzero tallies  = 0.0004",
        " history number of largest  tally  =   151081051          largest  unnormalized history tally = 2.38990E+01",
        " (largest  tally)/(average tally)  = 1.72624E+05          (largest  tally)/(avg nonzero tally)= 7.46502E+01",
        "",
        " (confidence interval shift)/mean  = 0.0001               shifted confidence interval center  = 4.44143E-09",
        "",
        "",
        " if the largest  history score sampled so far were to occur on the next history, the tfc bin quantities would change as follows:",
        "",
        "      estimated quantities           value at nps           value at nps+1           value(nps+1)/value(nps)-1.",
        "",
        "      mean                            4.44113E-09             4.44369E-09                     0.000575",
        "      relative error                  8.30645E-03             8.32157E-03                     0.001820",
        "      variance of the variance        3.95912E-04             4.14948E-04                     0.048080",
        "      shifted center                  4.44143E-09             4.44143E-09                     0.000001",
        "      figure of merit                 1.00552E+01             1.00187E+01                    -0.003630",
        "",
        " the estimated slope of the 200 largest  tallies starting at  8.20349E+00 appears to be decreasing at least exponentially.",
        " the large score tail of the empirical history score probability density function appears to have no unsampled regions.",
        "",
        " fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (2.081E+05)*( 6.951E-03)**2 = (2.081E+05)*(4.831E-05) = 1.006E+01",
        "",
        "1unnormed tally density for tally 46          nonzero tally mean(m) = 3.201E-01   nps = 300000000            print table 161",
        "",
        " abscissa              ordinate   log plot of tally probability density function in tally fluctuation chart bin(d=decade,slope=10.0)",
        "  tally  number num den log den:d-----------d------------d-----------d------------d------------d------------d-----------d-----------",
        " 3.98-08      1 2.27-01  -0.644 ************|************|***********|************|************|************|***********|***********",
        " 6.31-08      0 0.00+00   0.000             |            |           |            |            |            |           |           ",
        " 1.00-07      1 9.03-02  -1.044 ************|************|***********|************|************|************|***********|******     ",
        " 1.58-07      0 0.00+00   0.000             |            |           |            |            |            |           |           ",
        " 2.51-07      1 3.60-02  -1.444 ************|************|***********|************|************|************|***********|*          ",
        " 3.98-07      3 6.81-02  -1.167 ************|************|***********|************|************|************|***********|****       ",
        " 6.31-07      5 7.16-02  -1.145 ************|************|***********|************|************|************|***********|*****      ",
        " 1.00-06      1 9.03-03  -2.044 ************|************|***********|************|************|************|*****      |           ",
        " 1.58-06      5 2.85-02  -1.545 ************|************|***********|************|************|************|***********|           ",
        " 2.51-06      9 3.24-02  -1.490 ************|************|***********|************|************|************|***********|           ",
        " 3.98-06     14 3.18-02  -1.498 ************|************|***********|************|************|************|***********|           ",
        " 6.31-06     16 2.29-02  -1.640 ************|************|***********|************|************|************|********** |           ",
        " 1.00-05     32 2.89-02  -1.539 ************|************|***********|************|************|************|***********|           ",
        " 1.58-05     45 2.56-02  -1.591 ************|************|***********|************|************|************|***********|           ",
        " 2.51-05    114 4.10-02  -1.387 ************|************|***********|************|************|************|***********|**         ",
        " 3.98-05    154 3.49-02  -1.457 ************|************|***********|************|************|************|***********|*          ",
        " 6.31-05    215 3.08-02  -1.512 ************|************|***********|************|************|************|***********|           ",
        " 1.00-04    313 2.83-02  -1.549 ************|************|***********|************|************|************|***********|           ",
        " 1.58-04    526 3.00-02  -1.523 ************|************|***********|************|************|************|***********|           ",
        " 2.51-04    847 3.05-02  -1.516 ************|************|***********|************|************|************|***********|           ",
        " 3.98-04   1282 2.91-02  -1.536 ************|************|***********|************|************|************|***********|           ",
        " 6.31-04   1880 2.69-02  -1.570 ************|************|***********|************|************|************|***********|           ",
        " 1.00-03   2890 2.61-02  -1.583 ************|************|***********|************|************|************|***********|           ",
        " 1.58-03   4140 2.36-02  -1.627 ************|************|***********|************|************|************|********** |           ",
        " 2.51-03   5917 2.13-02  -1.672 ************|************|***********|************|************|************|********** |           ",
        " 3.98-03   8248 1.87-02  -1.728 ************|************|***********|************|************|************|*********  |           ",
        " 6.31-03  10594 1.52-02  -1.819 ************|************|***********|************|************|************|********   |           ",
        " 1.00-02  12501 1.13-02  -1.947 ************|************|***********|************|************|************|******     |           ",
        " 1.58-02  13391 7.63-03  -2.117 ************|************|***********|************|************|************|****       |           ",
        " 2.51-02  13160 4.73-03  -2.325 ************|************|***********|************|************|************|**         |           ",
        " 3.98-02  10892 2.47-03  -2.607 ************|************|***********|************|************|*********** |           |           ",
        " 6.31-02   7103 1.02-03  -2.993 ************|************|***********|************|************|******      |           |           ",
        " 1.00-01   4103 3.71-04  -3.431 ************|************|***********|************|************|            |           |           ",
        " 1.58-01   2667 1.52-04  -3.818 ************|************|***********|************|********    |            |           |           ",
        " 2.51-01   2782 1.00-04  -4.000 ************|************|***********|************|******      |            |           |           ",
        " 3.98-01   3432 7.79-05  -4.109 mmmmmmmmmmmm|mmmmmmmmmmmm|mmmmmmmmmmm|mmmmmmmmmmmm|mmmmm       |            |           |           ",
        " 6.31-01   4218 6.04-05  -4.219 ************|************|***********|************|***         |            |           |           ",
        " 1.00+00   4796 4.33-05  -4.363 ************|************|***********|************|**          |            |           |           ",
        " 1.58+00   5472 3.12-05  -4.506 ************|************|***********|************|            |            |           |           ",
        " 2.51+00   4000 1.44-05  -4.842 ************|************|***********|********    |            |            |           |           ",
        " 3.98+00   2358 5.35-06  -5.272 ************|************|***********|***         |            |            |           |           ",
        " 6.31+00   1118 1.60-06  -5.796 ************|************|********   |            |            |            |           |           ",
        " 1.00+01    399 3.60-07  -6.443 ************|************|           |            |            |            |           |           ",
        " 1.58+01     77 4.39-08  -7.358 ************|*           |           |            |            |            |           |           ",
        " 2.51+01     11 3.96-09  -8.403 *           |            |           |            |            |            |           |           ",
        "  total  129733 4.32-04         d-----------d------------d-----------d------------d------------d------------d-----------d-----------",
        "",
        ]
    return tally_data


def test_get_tallies_f2(mocker, f2_file, f2_tally_data):
    # arrange
    file = f2_file
    tally_data = f2_tally_data
    f2_mock = mocker.patch('eddymc.mcnp.tallies.F2Tally.__init__', return_value=None)
    f4_mock = mocker.patch('eddymc.mcnp.tallies.F4Tally.__init__', return_value=None)
    f5_mock = mocker.patch('eddymc.mcnp.tallies.F5Tally.__init__', return_value=None)
    f6_mock = mocker.patch('eddymc.mcnp.tallies.F6Tally.__init__', return_value=None)
    # act
    tallies.get_tallies(file)
    # assert
    f2_mock.assert_any_call(tally_data)
    f4_mock.assert_not_called()
    f5_mock.assert_not_called()
    f6_mock.assert_not_called()


def test_get_tallies_f4(mocker, f4_file, f4_tally_data):
    file = f4_file
    tally_data = f4_tally_data
    f2_mock = mocker.patch('eddymc.mcnp.tallies.F2Tally.__init__', return_value=None)
    f4_mock = mocker.patch('eddymc.mcnp.tallies.F4Tally.__init__', return_value=None)
    f5_mock = mocker.patch('eddymc.mcnp.tallies.F5Tally.__init__', return_value=None)
    f6_mock = mocker.patch('eddymc.mcnp.tallies.F6Tally.__init__', return_value=None)
    # act
    tallies.get_tallies(file)
    # assert
    f4_mock.assert_any_call(tally_data)
    f2_mock.assert_not_called()
    f5_mock.assert_not_called()
    f6_mock.assert_not_called()


def test_get_tallies_f5(mocker, f5_file, f5_tally_data):
    file = f5_file
    tally_data = f5_tally_data
    f2_mock = mocker.patch('eddymc.mcnp.tallies.F2Tally.__init__', return_value=None)
    f4_mock = mocker.patch('eddymc.mcnp.tallies.F4Tally.__init__', return_value=None)
    f5_mock = mocker.patch('eddymc.mcnp.tallies.F5Tally.__init__', return_value=None)
    f6_mock = mocker.patch('eddymc.mcnp.tallies.F6Tally.__init__', return_value=None)
    # act
    tallies.get_tallies(file)
    # assert
    f5_mock.assert_any_call(tally_data)
    f2_mock.assert_not_called()
    f4_mock.assert_not_called()
    f6_mock.assert_not_called()


def test_get_tallies_f6(mocker, f6_file, f6_tally_data):
    file = f6_file
    tally_data = f6_tally_data
    f2_mock = mocker.patch('eddymc.mcnp.tallies.F2Tally.__init__', return_value=None)
    f4_mock = mocker.patch('eddymc.mcnp.tallies.F4Tally.__init__', return_value=None)
    f5_mock = mocker.patch('eddymc.mcnp.tallies.F5Tally.__init__', return_value=None)
    f6_mock = mocker.patch('eddymc.mcnp.tallies.F6Tally.__init__', return_value=None)
    # act
    tallies.get_tallies(file)
    # assert
    f6_mock.assert_any_call(tally_data)
    f2_mock.assert_not_called()
    f4_mock.assert_not_called()
    f5_mock.assert_not_called()


def test_get_tallies_f6plus(mocker, f6_file, f6_plus_tally_data):
    file = f6_file
    tally_data = f6_plus_tally_data
    f2_mock = mocker.patch('eddymc.mcnp.tallies.F2Tally.__init__', return_value=None)
    f4_mock = mocker.patch('eddymc.mcnp.tallies.F4Tally.__init__', return_value=None)
    f5_mock = mocker.patch('eddymc.mcnp.tallies.F5Tally.__init__', return_value=None)
    f6_mock = mocker.patch('eddymc.mcnp.tallies.F6Tally.__init__', return_value=None)
    # act
    tallies.get_tallies(file)
    # assert
    f6_mock.assert_any_call(tally_data)
    f2_mock.assert_not_called()
    f4_mock.assert_not_called()
    f5_mock.assert_not_called()


def test_f2_init():
    pass
    # this will actually need several tests for different possibilities


def test_f4_init():
    pass
    # this will actually need several tests for different possibilities


def test_f5_init():
    pass
    # this will actually need several tests for different possibilities


def test_f6_init_creates_object():
    # this will actually need several tests for different possibilities
    # arrange
    tally_data = [
        "1tally      396        nps =   300000000",
        "           tally type 6    track length estimate of heating.            units   mev/gram       ",
        "           particle(s): photons  ",
        "",
        "           masses  ",
        "                   cell:      29           30                                                                      ",
        "                         2.12285E+04  2.12285E+04",
        " ",
        " cell  29                                                                                                                              ",
        "                 1.96685E-09 0.0141",
        " ",
        " cell  30                                                                                                                              ",
        "                 1.94392E-09 0.0141",
        "",
        "",
        " ===================================================================================================================================",
        "",
        "           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc) bin of tally      396",
        "",
        " tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-",
        " behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope",
        "",
        " desired      random       <0.10      yes      1/sqrt(nps)       <0.10      yes        1/nps           constant    random      >3.00",
        " observed     random        0.01      yes          yes            0.00      yes         yes            constant    random      10.00",
        " passed?        yes          yes      yes          yes             yes      yes         yes               yes        yes         yes",
        "",
        " ===================================================================================================================================",
        "",
        "",
        " this tally meets the statistical criteria used to form confidence intervals: check the tally fluctuation chart to verify.",
        " the results in other bins associated with this tally may not meet these statistical criteria.",
        "",
        " ----- estimated confidence intervals:  -----",
        "",
        " estimated asymmetric confidence interval(1,2,3 sigma): 1.9395E-09 to 1.9950E-09; 1.9117E-09 to 2.0228E-09; 1.8839E-09 to 2.0506E-09",
        " estimated  symmetric confidence interval(1,2,3 sigma): 1.9391E-09 to 1.9946E-09; 1.9113E-09 to 2.0224E-09; 1.8835E-09 to 2.0502E-09",
        "",
        "1analysis of the results in the tally fluctuation chart bin (tfc) for tally 396 with nps = 300000000         print table 160",
        "",
        "",
        " normed average tally per history  = 1.96685E-09          unnormed average tally per history  = 4.17533E-05",
        " estimated tally relative error    = 0.0141               estimated variance of the variance  = 0.0012",
        " relative error from zero tallies  = 0.0084               relative error from nonzero scores  = 0.0114",
        "",
        " number of nonzero history tallies =       14281          efficiency for the nonzero tallies  = 0.0000",
        " history number of largest  tally  =   170078837          largest  unnormalized history tally = 1.78932E+01",
        " (largest  tally)/(average tally)  = 4.28545E+05          (largest  tally)/(avg nonzero tally)= 2.04002E+01",
        "",
        " (confidence interval shift)/mean  = 0.0002               shifted confidence interval center  = 1.96724E-09",
        "",
        "",
        " if the largest  history score sampled so far were to occur on the next history, the tfc bin quantities would change as follows:",
        "",
        "      estimated quantities           value at nps           value at nps+1           value(nps+1)/value(nps)-1.",
        "",
        "      mean                            1.96685E-09             1.96966E-09                     0.001428",
        "      relative error                  1.41246E-02             1.41764E-02                     0.003667",
        "      variance of the variance        1.21436E-03             1.29241E-03                     0.064266",
        "      shifted center                  1.96724E-09             1.96725E-09                     0.000005",
        "      figure of merit                 3.47754E+00             3.45218E+00                    -0.007295",
        "",
        " the estimated slope of the 200 largest  tallies starting at  5.17418E+00 appears to be decreasing at least exponentially.",
        " the large score tail of the empirical history score probability density function appears to have no unsampled regions.",
        "",
        " fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (2.081E+05)*( 4.088E-03)**2 = (2.081E+05)*(1.671E-05) = 3.478E+00",
        "",
        ]
    # act
    F6_object = tallies.F6Tally(tally_data)
    # assert
    assert type(F6_object) == tallies.F6Tally


def test_f6_init_creates_f6plus_object():
    pass


