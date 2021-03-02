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
    # noinspection PyTypeChecker
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
"1tally        6        nps =     3447731",
"           tally type 6    track length estimate of heating.            units   mev/gram       ",
"           particle(s): neutrons ",
"",
"           masses  ",
"                   cell:       3            4                                                                      ",
"                         1.36787E+00  1.67072E+00",
" ",
" cell  3                                                                                                                               ",
"                 2.45307E-05 0.0005",
" ",
" cell  4                                                                                                                               ",
"                 2.00761E-05 0.0005",
"",
"",
" ===================================================================================================================================",
"",
"           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc) bin of tally        6",
"",
" tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-",
" behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope",
"",
" desired      random       <0.10      yes      1/sqrt(nps)       <0.10      yes        1/nps           constant    random      >3.00",
" observed     random        0.00      yes          yes            0.00      yes         yes            increase    random       1.54",
" passed?        yes          yes      yes          yes             yes      yes         yes                no        yes          no",
"",
" ===================================================================================================================================",
"",
"",
" warning.  the tally in the tally fluctuation chart bin did not pass  2 of the 10 statistical checks.",
"",
"1analysis of the results in the tally fluctuation chart bin (tfc) for tally 6 with nps = 3447731             print table 160",
"",
"",
" normed average tally per history  = 2.45307E-05          unnormed average tally per history  = 3.35548E-05",
" estimated tally relative error    = 0.0005               estimated variance of the variance  = 0.0000",
" relative error from zero tallies  = 0.0000               relative error from nonzero scores  = 0.0005",
"",
" number of nonzero history tallies =     3447731          efficiency for the nonzero tallies  = 1.0000",
" history number of largest  tally  =     3397547          largest  unnormalized history tally = 7.55327E-04",
" (largest  tally)/(average tally)  = 2.25103E+01          (largest  tally)/(avg nonzero tally)= 2.25103E+01",
"",
" (confidence interval shift)/mean  = 0.0000               shifted confidence interval center  = 2.45307E-05",
"",
"",
" if the largest  history score sampled so far were to occur on the next history, the tfc bin quantities would change as follows:",
"",
"      estimated quantities           value at nps           value at nps+1           value(nps+1)/value(nps)-1.",
"",
"      mean                            2.45307E-05             2.45308E-05                     0.000006",
"      relative error                  4.74050E-04             4.74088E-04                     0.000080",
"      variance of the variance        8.67834E-07             8.97414E-07                     0.034086",
"      shifted center                  2.45307E-05             2.45307E-05                     0.000000",
"      figure of merit                 4.42686E+06             4.42615E+06                    -0.000160",
"",
" the estimated inverse power slope of the 200 largest  tallies starting at 1.80707E-04 is 1.5437",
" the large score tail of the empirical history score probability density function appears to have no unsampled regions.",
"",
" fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (3.430E+06)*( 1.136E+00)**2 = (3.430E+06)*(1.291E+00) = 4.427E+06",
"",
"1unnormed tally density for tally 6          nonzero tally mean(m) = 3.355E-05   nps = 3447731               print table 161",
"",
" abscissa              ordinate   log plot of tally probability density function in tally fluctuation chart bin(d=decade,slope= 1.5)",
"  tally  number num den log den:d------------d-------------d-------------d--------------d-------------d-------------d-------------d-",
" 3.16-07    630 2.81+03   3.449 *************|*************|*************|**************|*************|*************|             | ",
" 3.98-07   1054 3.73+03   3.572 *************|*************|*************|**************|*************|*************|*            | ",
" 5.01-07   1206 3.39+03   3.531 *************|*************|*************|**************|*************|*************|*            | ",
" 6.31-07   1658 3.71+03   3.569 *************|*************|*************|**************|*************|*************|*            | ",
" 7.94-07   2317 4.11+03   3.614 *************|*************|*************|**************|*************|*************|**           | ",
" 1.00-06   3187 4.49+03   3.653 *************|*************|*************|**************|*************|*************|**           | ",
" 1.26-06   4440 4.97+03   3.697 *************|*************|*************|**************|*************|*************|***          | ",
" 1.58-06   7192 6.40+03   3.806 *************|*************|*************|**************|*************|*************|****         | ",
" 2.00-06   8451 5.97+03   3.776 *************|*************|*************|**************|*************|*************|****         | ",
" 2.51-06  14138 7.94+03   3.900 *************|*************|*************|**************|*************|*************|******       | ",
" 3.16-06  28296 1.26+04   4.101 *************|*************|*************|**************|*************|*************|*********    | ",
" 3.98-06  55189 1.95+04   4.291 *************|*************|*************|**************|*************|*************|***********  | ",
" 5.01-06  74291 2.09+04   4.320 *************|*************|*************|**************|*************|*************|************ | ",
" 6.31-06  91439 2.04+04   4.310 *************|*************|*************|**************|*************|*************|************ | ",
" 7.94-06 173780 3.09+04   4.489 *************|*************|*************|**************|*************|*************|*************| ",
" 1.00-05 251263 3.54+04   4.549 *************|*************|*************|**************|*************|*************|*************|*",
" 1.26-05 232320 2.60+04   4.415 *************|*************|*************|**************|*************|*************|*************| ",
" 1.58-05 239628 2.13+04   4.329 *************|*************|*************|**************|*************|*************|************ | ",
" 2.00-05 227534 1.61+04   4.206 *************|*************|*************|**************|*************|*************|**********   | ",
" 2.51-05 550722 3.09+04   4.490 *************|*************|*************|**************|*************|*************|*************| ",
" 3.16-05 313019 1.40+04   4.145 *************|*************|*************|**************|*************|*************|*********    | ",
" 3.98-05 181177 6.42+03   3.807 mmmmmmmmmmmmm|mmmmmmmmmmmmm|mmmmmmmmmmmmm|mmmmmmmmmmmmmm|mmmmmmmmmmmmm|mmmmmmmmmmmmm|mmmmm        | ",
" 5.01-05 212683 5.98+03   3.777 *************|*************|*************|**************|*************|*************|****         | ",
" 6.31-05  94901 2.12+03   3.327 *************|*************|*************|**************|*************|************ |             | ",
" 7.94-05 268994 4.78+03   3.679 *************|*************|*************|**************|*************|*************|***          | ",
" 1.00-04 265893 3.75+03   3.574 *************|*************|*************|**************|*************|*************|*            | ",
" 1.26-04 135421 1.52+03   3.181 *************|*************|*************|**************|*************|**********   |             | ",
" 1.58-04   6117 5.44+01   1.736 *************|*************|*************|**************|***          |             |             | ",
" 2.00-04    695 4.91+00   0.691 *************|*************|*************|***         s |             |             |             | ",
" 2.51-04     38 2.13-01  -0.671 *************|************ |             |          s   |             |             |             | ",
" 3.16-04     24 1.07-01  -0.970 *************|********     |             |        s     |             |             |             | ",
" 3.98-04     15 5.31-02  -1.275 *************|****         |             |      s       |             |             |             | ",
" 5.01-04     12 3.38-02  -1.472 *************|*            |             |   s          |             |             |             | ",
" 6.31-04      5 1.12-02  -1.952 ********     |             |             | s            |             |             |             | ",
" 7.94-04      2 3.55-03  -2.450 *            |             |             s              |             |             |             | ",
"  total 3447731 1.00+00         d------------d-------------d-------------d--------------d-------------d-------------d-------------d-",
"",]
    return tally_data


@pytest.fixture
def f6_plus_tally_data(tmpdir):
    tally_data = ["1tally       46        nps =     3447731",
    "           tally type 6+   energy deposition                            units   mev/gram       ",
    "           particle(s): neutrons ",
    "",
    "           masses  ",
    "                   cell:       3            4                                                                      ",
    "                         1.36787E+00  1.67072E+00",
    " ",
    " cell  3                                                                                                                               ",
    "                 2.60440E-05 0.0005",
    " ",
    " cell  4                                                                                                                               ",
    "                 2.13145E-05 0.0005",
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
    " observed     random        0.00      yes          yes            0.00      yes         yes            increase    random       4.95",
    " passed?        yes          yes      yes          yes             yes      yes         yes                no        yes         yes",
    "",
    " ===================================================================================================================================",
    "",
    "",
    " warning.  the tally in the tally fluctuation chart bin did not pass  1 of the 10 statistical checks.",
    "",
    "1analysis of the results in the tally fluctuation chart bin (tfc) for tally 46 with nps = 3447731            print table 160",
    "",
    "",
    " normed average tally per history  = 2.60440E-05          unnormed average tally per history  = 3.56249E-05",
    " estimated tally relative error    = 0.0005               estimated variance of the variance  = 0.0000",
    " relative error from zero tallies  = 0.0000               relative error from nonzero scores  = 0.0005",
    "",
    " number of nonzero history tallies =     3447731          efficiency for the nonzero tallies  = 1.0000",
    " history number of largest  tally  =      703846          largest  unnormalized history tally = 7.70071E-04",
    " (largest  tally)/(average tally)  = 2.16161E+01          (largest  tally)/(avg nonzero tally)= 2.16161E+01",
    "",
    " (confidence interval shift)/mean  = 0.0000               shifted confidence interval center  = 2.60441E-05",
    "",
    "",
    " if the largest  history score sampled so far were to occur on the next history, the tfc bin quantities would change as follows:",
    "",
    "      estimated quantities           value at nps           value at nps+1           value(nps+1)/value(nps)-1.",
    "",
    "      mean                            2.60440E-05             2.60442E-05                     0.000006",
    "      relative error                  4.89083E-04             4.89117E-04                     0.000068",
    "      variance of the variance        1.27214E-06             1.29400E-06                     0.017183",
    "      shifted center                  2.60441E-05             2.60441E-05                     0.000000",
    "      figure of merit                 4.15890E+06             4.15833E+06                    -0.000137",
    "",
    " the estimated inverse power slope of the 200 largest  tallies starting at 2.85669E-04 is 4.9515",
    " the large score tail of the empirical history score probability density function appears to have no unsampled regions.",
    "",
    " fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (3.430E+06)*( 1.101E+00)**2 = (3.430E+06)*(1.213E+00) = 4.159E+06",
    "",
    "1unnormed tally density for tally 46          nonzero tally mean(m) = 3.562E-05   nps = 3447731              print table 161",
    "",
    " abscissa              ordinate   log plot of tally probability density function in tally fluctuation chart bin(d=decade,slope= 5.0)",
    "  tally  number num den log den:d-------------d--------------d-------------d--------------d--------------d--------------d-----------",
    " 3.16-07    611 2.72+03   3.435 **************|**************|*************|**************|**************|**********    |           ",
    " 3.98-07   1035 3.67+03   3.564 **************|**************|*************|**************|**************|************  |           ",
    " 5.01-07   1190 3.35+03   3.525 **************|**************|*************|**************|**************|***********   |           ",
    " 6.31-07   1636 3.66+03   3.563 **************|**************|*************|**************|**************|************  |           ",
    " 7.94-07   2281 4.05+03   3.607 **************|**************|*************|**************|**************|************  |           ",
    " 1.00-06   3138 4.43+03   3.646 **************|**************|*************|**************|**************|************* |           ",
    " 1.26-06   4350 4.87+03   3.688 **************|**************|*************|**************|**************|************* |           ",
    " 1.58-06   7016 6.24+03   3.795 **************|**************|*************|**************|**************|**************|           ",
    " 2.00-06   8272 5.85+03   3.767 **************|**************|*************|**************|**************|**************|           ",
    " 2.51-06  13705 7.69+03   3.886 **************|**************|*************|**************|**************|**************|*          ",
    " 3.16-06  27750 1.24+04   4.093 **************|**************|*************|**************|**************|**************|****       ",
    " 3.98-06  54241 1.92+04   4.284 **************|**************|*************|**************|**************|**************|*******    ",
    " 5.01-06  72824 2.05+04   4.312 **************|**************|*************|**************|**************|**************|********   ",
    " 6.31-06  89508 2.00+04   4.301 **************|**************|*************|**************|**************|**************|*******    ",
    " 7.94-06 169597 3.01+04   4.479 **************|**************|*************|**************|**************|**************|********** ",
    " 1.00-05 244532 3.45+04   4.538 **************|**************|*************|**************|**************|**************|***********",
    " 1.26-05 226623 2.54+04   4.405 **************|**************|*************|**************|**************|**************|*********  ",
    " 1.58-05 232880 2.07+04   4.316 **************|**************|*************|**************|**************|**************|********   ",
    " 2.00-05 220109 1.56+04   4.192 **************|**************|*************|**************|**************|**************|******     ",
    " 2.51-05 526709 2.96+04   4.471 **************|**************|*************|**************|**************|**************|********** ",
    " 3.16-05 300718 1.34+04   4.127 **************|**************|*************|**************|**************|**************|*****      ",
    " 3.98-05 180106 6.38+03   3.805 mmmmmmmmmmmmmm|mmmmmmmmmmmmmm|mmmmmmmmmmmmm|mmmmmmmmmmmmmm|mmmmmmmmmmmmmm|mmmmmmmmmmmmmm|           ",
    " 5.01-05 215302 6.06+03   3.782 **************|**************|*************|**************|**************|**************|           ",
    " 6.31-05 111140 2.48+03   3.395 **************|**************|*************|**************|**************|*********     |           ",
    " 7.94-05 275550 4.89+03   3.689 **************|**************|*************|**************|**************|************* |           ",
    " 1.00-04 263106 3.71+03   3.569 **************|**************|*************|**************|**************|************  |           ",
    " 1.26-04 152703 1.71+03   3.233 **************|**************|*************|**************|**************|*******       |           ",
    " 1.58-04  30964 2.76+02   2.440 **************|**************|*************|**************|**********    |              |           ",
    " 2.00-04   8141 5.75+01   1.760 **************|**************|*************|**************|              |              |           ",
    " 2.51-04   1552 8.71+00   0.940 **************|**************|*************|***           |              |              |           ",
    " 3.16-04    334 1.49+00   0.173 **************|**************|*****        |s             |              |              |           ",
    " 3.98-04     74 2.62-01  -0.581 **************|*********     |         s   |              |              |              |           ",
    " 5.01-04     26 7.32-02  -1.136 **************|*             |     s       |              |              |              |           ",
    " 6.31-04      4 8.94-03  -2.049 **            |              s             |              |              |              |           ",
    " 7.94-04      4 7.10-03  -2.149 *             |         s    |             |              |              |              |           ",
    "  total 3447731 1.00+00         d-------------d--------------d-------------d--------------d--------------d--------------d-----------",
    "",]
    return tally_data


def test_f2_init_creates_object(f2_tally_data):
    # arrange
    tally_data = f2_tally_data
    # act
    F2_object = tallies.F2Tally(tally_data)
    # assert
    assert type(F2_object) == tallies.F2Tally
    assert F2_object.tally_type == "particle flux averaged over a surface."
    assert F2_object.particles == "neutrons"
    assert F2_object.f_type == "F2"
    assert F2_object.dose_functions == ("DE2", "DF2")


def test_f2_init_calls_subclass_results(mocker, f2_tally_data):
    # arrange
    tally_data = f2_tally_data
    mocked_subclass_get_results = mocker.patch('eddymc.mcnp.tallies.F2Tally.get_results', return_value=None)
    mocked_superclass_get_results = mocker.patch('eddymc.mcnp.tallies.Tally.get_results', return_value=None)
    # act
    tallies.F2Tally(tally_data)
    # assert
    mocked_subclass_get_results.assert_any_call()
    mocked_superclass_get_results.assert_not_called()


def test_f2_tally_get_results(f2_tally_data):
    # arrange
    tally = tallies.F2Tally(f2_tally_data)
    # act
    tally.results = tally.get_results()
    # assert
    assert type(tally.results) == list
    assert tally.results[0]['surface'] == 'Surface  2'
    assert tally.results[0]['result'] == 1.11143E-03
    assert tally.results[0]['variance'] == 0.0001


def test_f2_tally_scale_result(f2_tally_data):
    # arrange
    F2_object = tallies.F2Tally(f2_tally_data)
    # act
    F2_object.scale_result(scaling_factor=3)
    # assert
    assert F2_object.results[0]['result'] == 1.11143E-03 * 3


def test_f4_init_creates_object(f4_tally_data):
    # arrange
    tally_data = f4_tally_data
    # act
    F4_object = tallies.F4Tally(tally_data)
    # assert
    assert type(F4_object) == tallies.F4Tally
    assert F4_object.tally_type == "track length estimate of particle flux."
    assert F4_object.particles == "neutrons"
    assert F4_object.f_type == "F4"
    assert F4_object.dose_functions == ("DE4", "DF4")


def test_f4_init_calls_subclass_results(mocker, f4_tally_data):
    # arrange
    tally_data = f4_tally_data
    mocked_subclass_get_results = mocker.patch('eddymc.mcnp.tallies.F4Tally.get_results', return_value=None)
    mocked_superclass_get_results = mocker.patch('eddymc.mcnp.tallies.Tally.get_results', return_value=None)
    # act
    tallies.F4Tally(tally_data)
    # assert
    mocked_subclass_get_results.assert_any_call()
    mocked_superclass_get_results.assert_not_called()


def test_f4_tally_get_results(f4_tally_data):
    # arrange
    tally = tallies.F4Tally(f4_tally_data)
    # act
    tally.results = tally.get_results()
    # assert
    assert type(tally.results) == list
    assert len(tally.results) == 1
    assert tally.results[0]['region'] == "Cell  3"
    assert tally.results[0]['result'] == 1.10032E-03
    assert tally.results[0]['variance'] == 0.0001


def test_f4_tally_scale_result(f4_tally_data):
    # arrange
    F4_object = tallies.F4Tally(f4_tally_data)
    # act
    F4_object.scale_result(scaling_factor=2)
    # assert
    assert F4_object.results[0]['result'] == 1.10032E-03 * 2


def test_f5_init_creates_object(f5_tally_data):
    # arrange
    tally_data = f5_tally_data
    # act
    F5_object = tallies.F5Tally(tally_data)
    # assert
    assert type(F5_object) == tallies.F5Tally
    assert F5_object.tally_type == "particle flux at a point detector."
    assert F5_object.particles == "neutrons"
    assert F5_object.f_type == "F5"
    assert F5_object.dose_functions == ("DE5", "DF5")


def test_f5_init_calls_subclass_results(mocker, f5_tally_data):
    # arrange
    tally_data = f5_tally_data
    mocked_subclass_get_results = mocker.patch('eddymc.mcnp.tallies.F5Tally.get_results', return_value=None)
    mocked_superclass_get_results = mocker.patch('eddymc.mcnp.tallies.Tally.get_results', return_value=None)
    # act
    tallies.F5Tally(tally_data)
    # assert
    mocked_subclass_get_results.assert_any_call()
    mocked_superclass_get_results.assert_not_called()


def test_f5_tally_get_results(f5_tally_data):
    # arrange
    tally = tallies.F5Tally(f5_tally_data)
    # act
    tally.results = tally.get_results()
    # assert
    assert type(tally.results) == list
    assert type(tally.results[0]) == dict
    assert tally.results[0]['x'] == 5
    assert tally.results[0]['y'] == 0
    assert tally.results[0]['z'] == 0
    assert tally.results[0]['result'] == 4.38636E-03
    assert tally.results[0]['variance'] == 0.0003


def test_f5_tally_with_multiple_detectors():
    # arrange
    tally_data = [
        "1tally       15        nps =     3904520",
        "           tally type 5    particle flux at a point detector.                                  ",
        "           particle(s): photons  ",
        "           this tally is modified by dose function DE15 and DF15.",
        " ",
        " detector located at x,y,z = 5.00000E+00 0.00000E+00 0.00000E+00",
        "                 2.40763E-04 0.0029",
        " ",
        " detector located at x,y,z = 5.00000E+00 0.00000E+00 0.00000E+00",
        " uncollided photon flux",
        "                 1.94034E-04 0.0025",
        " ",
        " detector score diagnostics                  cumulative          tally         cumulative",
        "                                             fraction of         per           fraction of",
        "   times average score     transmissions     transmissions       history       total tally",
        "        1.00000E-01                604         0.00202        2.68832E-09        0.00002",
        "        1.00000E+00               4488         0.01702        1.10010E-07        0.00065",
        "        2.00000E+00               9425         0.04853        6.46301E-07        0.00435",
        "        5.00000E+00              25646         0.13427        3.91143E-06        0.02678",
        "        1.00000E+01              78306         0.39605        2.76540E-05        0.18538",
        "        1.00000E+02             180200         0.99847        1.39508E-04        0.98546",
        "        1.00000E+03                349         0.99964        2.30379E-06        0.99867",
        "        1.00000E+38                  3         0.99965        1.71417E-07        0.99966",
        " before dd roulette                106         1.00000        6.00721E-08        1.00000",
        "",
        " average tally per history = 1.74368E-04            largest score = 2.85684E-01",
        " (largest score)/(average tally) = 1.63840E+03      nps of largest score =      361869",
        "",
        " score contributions by cell",
        "        cell      misses        hits    tally per history    weight per hit",
        "     1     1       22605      298884       1.74200E-04         2.27569E-03",
        "     2     2           1         210       1.62928E-07         3.02931E-03",
        "     3     3           0           1       3.52737E-10         1.37727E-03",
        "     4     4           0          32       4.36382E-09         5.32457E-04",
        "       total       22606      299127       1.74368E-04         2.27603E-03",
        "",
        " score misses",
        "   russian roulette on pd                        0",
        "   psc=0.                                     1738",
        "   russian roulette in transmission           5095",
        "   underflow in transmission                 15773",
        "   hit a zero-importance cell                    0",
        "   energy cutoff                                 0",
        " ",
        " detector located at x,y,z = 1.00000E+01 0.00000E+00 0.00000E+00",
        "                 5.98890E-05 0.0029",
        " ",
        " detector located at x,y,z = 1.00000E+01 0.00000E+00 0.00000E+00",
        " uncollided photon flux",
        "                 4.82377E-05 0.0025",
        " ",
        " detector score diagnostics                  cumulative          tally         cumulative",
        "                                             fraction of         per           fraction of",
        "   times average score     transmissions     transmissions       history       total tally",
        "        1.00000E-01                617         0.00206        6.86885E-10        0.00002",
        "        1.00000E+00               3653         0.01427        2.07056E-08        0.00049",
        "        2.00000E+00               7408         0.03901        1.27778E-07        0.00344",
        "        5.00000E+00              25450         0.12404        9.71558E-07        0.02582",
        "        1.00000E+01              63439         0.33597        5.68921E-06        0.15690",
        "        1.00000E+02             198434         0.99889        3.60837E-05        0.98825",
        "        1.00000E+03                222         0.99963        3.99978E-07        0.99747",
        "        1.00000E+38                  5         0.99965        9.47896E-08        0.99965",
        " before dd roulette                106         1.00000        1.51668E-08        1.00000",
        "",
        " average tally per history = 4.34036E-05            largest score = 1.64584E-01",
        " (largest score)/(average tally) = 3.79195E+03      nps of largest score =     2684859",
        "",
        " score contributions by cell",
        "        cell      misses        hits    tally per history    weight per hit",
        "     1     1       22396      299093       4.33479E-05         5.65887E-04",
        "     2     2           3         208       4.92899E-08         9.25257E-04",
        "     3     3           0           1       1.46115E-10         5.70511E-04",
        "     4     4           0          32       6.29140E-09         7.67653E-04",
        "       total       22399      299334       4.34036E-05         5.66158E-04",
        "",
        " score misses",
        "   russian roulette on pd                        0",
        "   psc=0.                                     1729",
        "   russian roulette in transmission           4997",
        "   underflow in transmission                 15673",
        "   hit a zero-importance cell                    0",
        "   energy cutoff                                 0",
        "",
        "",
        " ===================================================================================================================================",
        "",
        "           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc) bin of tally       15",
        "",
        " tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-",
        " behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope",
        "",
        " desired      random       <0.05      yes      1/sqrt(nps)       <0.10      yes        1/nps           constant    random      >3.00",
        " observed     random        0.00      yes          yes            0.00      yes         yes            constant    random       2.82",
        " passed?        yes          yes      yes          yes             yes      yes         yes               yes        yes          no",
        "",
        " ===================================================================================================================================",
        "",
        "",
        " warning.  the tally in the tally fluctuation chart bin did not pass  1 of the 10 statistical checks.",
        "",
        "1analysis of the results in the tally fluctuation chart bin (tfc) for tally 15 with nps = 3904520            print table 160",
        "",
        "",
        " normed average tally per history  = 2.40763E-04          unnormed average tally per history  = 2.40763E-04",
        " estimated tally relative error    = 0.0029               estimated variance of the variance  = 0.0009",
        " relative error from zero tallies  = 0.0022               relative error from nonzero scores  = 0.0019",
        "",
        " number of nonzero history tallies =      198128          efficiency for the nonzero tallies  = 0.0507",
        " history number of largest  tally  =      361869          largest  unnormalized history tally = 4.32843E-01",
        " (largest  tally)/(average tally)  = 1.79780E+03          (largest  tally)/(avg nonzero tally)= 9.12260E+01",
        "",
        " (confidence interval shift)/mean  = 0.0000               shifted confidence interval center  = 2.40767E-04",
        "",
        "",
        " if the largest  history score sampled so far were to occur on the next history, the tfc bin quantities would change as follows:",
        "",
        "      estimated quantities           value at nps           value at nps+1           value(nps+1)/value(nps)-1.",
        "",
        "      mean                            2.40763E-04             2.40874E-04                     0.000460",
        "      relative error                  2.89441E-03             2.92941E-03                     0.012094",
        "      variance of the variance        9.39070E-04             1.50118E-03                     0.598580",
        "      shifted center                  2.40767E-04             2.40769E-04                     0.000005",
        "      figure of merit                 1.16662E+05             1.13891E+05                    -0.023756",
        "",
        " the estimated inverse power slope of the 200 largest  tallies starting at 3.83869E-02 is 2.8181",
        " the history score probability density function appears to have an unsampled region at the largest  history scores:",
        " please examine. see print table 161.",
        "",
        " fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (3.816E+06)*( 1.748E-01)**2 = (3.816E+06)*(3.057E-02) = 1.167E+05",
        "",
    ]
    tally = tallies.F5Tally(tally_data)
    # act
    tally.results = tally.get_results()
    # assert
    assert len(tally.results) == 2
    assert tally.results[0]['result'] == 2.40763E-04
    assert tally.results[1]['result'] == 5.98890E-05


def test_f5_tally_scale_result(f5_tally_data):
    # arrange
    F5_object = tallies.F5Tally(f5_tally_data)
    # act
    F5_object.scale_result(scaling_factor=3)
    # assert
    assert F5_object.results[0]["result"] == 4.38636E-03 * 3


def test_f6_init_creates_object(f6_tally_data):
    # arrange
    tally_data = f6_tally_data
    # act
    F6_object = tallies.F6Tally(tally_data)
    # assert
    assert type(F6_object) == tallies.F6Tally
    assert F6_object.tally_type == "track length estimate of heating. units mev/gram"
    assert F6_object.particles == "neutrons"
    assert F6_object.f_type == "F6"
    assert F6_object.dose_functions == "This tally is not modified by any dose function"


def test_f6_init_creates_f6plus_object(f6_plus_tally_data):
    # arrange
    tally_data = f6_plus_tally_data
    # act
    F6_object = tallies.F6Tally(tally_data)
    # assert
    assert type(F6_object) == tallies.F6Tally
    assert F6_object.tally_type == "energy deposition units mev/gram"
    assert F6_object.particles == "Collision Heating"
    assert F6_object.f_type == "F6+"
    assert F6_object.dose_functions == "This tally is not modified by any dose function"


def test_f6_init_calls_subclass_results(mocker, f6_tally_data):
    # arrange
    tally_data = f6_tally_data
    mocked_subclass_get_results = mocker.patch('eddymc.mcnp.tallies.F6Tally.get_results', return_value=None)
    mocked_superclass_get_results = mocker.patch('eddymc.mcnp.tallies.Tally.get_results', return_value=None)
    # act
    tallies.F6Tally(tally_data)
    # assert
    mocked_subclass_get_results.assert_any_call()
    mocked_superclass_get_results.assert_not_called()


def test_f6_tally_get_results(f6_tally_data):
    # arrange
    tally = tallies.F6Tally(f6_tally_data)
    # act
    tally.results = tally.get_results()
    # assert
    assert type(tally.results) == dict
    assert tally.results['3']['region'] == "Cell 3"
    assert tally.results['3']['result'] == 2.45307E-05
    assert tally.results['3']['variance'] == 0.0005
    assert tally.results['4']['region'] == "Cell 4"
    assert tally.results['4']['result'] == 2.00761E-05
    assert tally.results['4']['variance'] == 0.0005


def test_f6_plus_tally_get_results(f6_plus_tally_data):
    # arrange
    tally = tallies.F6Tally(f6_plus_tally_data)
    # act
    tally.results = tally.get_results()
    # assert
    assert type(tally.results) == dict
    assert tally.results['3']['region'] == "Cell 3"
    assert tally.results['3']['result'] == 2.60440E-05
    assert tally.results['3']['variance'] == 0.0005
    assert tally.results['4']['region'] == "Cell 4"
    assert tally.results['4']['result'] == 2.13145E-05
    assert tally.results['4']['variance'] == 0.0005


def test_f6_tally_scale_results(f6_tally_data):
    # arrange
    F6_object = tallies.F6Tally(f6_tally_data)
    # act
    F6_object.scale_result(scaling_factor=2)
    # assert
    assert F6_object.results['3']['result'] == 2.45307E-05 * 2

