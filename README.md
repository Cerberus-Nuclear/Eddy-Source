# Eddy

Eddy is a HTML output generator for MCNP and SCALE, it imports an MCNP or SCALE output file, extracts the important data, and writes it to a user-friendly HTML file.

This is the executable version of Eddy. The exectuable itself is the Eddy_beta_02.exe file found in the top level Eddy folder. It can be run simply by double-clicking on this executable.

Eddy can be run from the command line with the output file and any applicable scaling factor as optional arguments; if no such arguments are supplied a GUI will appear to request them.

General CLI usage: python3 Eddy.py [-o outputfile] [-sf scaling_factor] ---> outputfile.html

Eddy can be downloaded as either a pre-compiled executable, from <https://github.com/Cerberus-Nuclear/Eddy>,
or as source code from <https://github.com/Cerberus-Nuclear/Eddy-Source>.

The source code for Eddy can be run with python 3.6 or later and the Jinja2 python 
package is required. All other modules used by Eddy are either part of the python standard library or included with Eddy; other modules used 
to compile the source code into an executable can be found in the requirements.txt file.

All the code within this project is covered by GPLv3, the GNU Public Licence, Version 3, June 2007. A full copy of this licence is included with the source code; more information can be found at https://www.gnu.org/licenses/.

Disclaimer: The material embodied in this software is provided to you "as-is" and without warranty of any kind, express, implied or otherwise, including without limitation, any warranty of fitness for a particular purpose. In no event shall the Cerberus Nuclear Limited be liable to you or anyone else for any direct, special, incidental, indirect or consequential damages of any kind, or any damages whatsoever, including without limitation, loss of profit, loss of use, savings or revenue, or the claims of third parties, whether or not Cerberus Nuclear Limited has been advised of the possibility of such loss, however caused and on any theory of liability, arising out of or in connection with the possession, use or performance of this software.
