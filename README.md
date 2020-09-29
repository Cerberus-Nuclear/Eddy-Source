# Eddy

Eddy is a HTML output generator for MCNP and SCALE. It was created by Cerberus Nuclear. Cerberus Nuclear accepts no 
responsibility for the accuracy of any results presented with Eddy. 

Eddy taken an MCNP or SCALE output file, extracts the important data, 
and writes it to a user-friendly HTML file. 

All the code within this project is covered by GPLv3, the GNU Public Licence, Version 3, June 2007. A full copy of this 
licence is included with the source code; more information can be found at <https://www.gnu.org/licenses/>.

Eddy can be downloaded as either a pre-compiled executable, from <https://github.com/Cerberus-Nuclear/Eddy>,
or as source code from <https://github.com/Cerberus-Nuclear/Eddy-Source>.

The source code for Eddy can be run with python; if doing so python 3.6 or later is required, and the Jinja2 python 
package is needed; this can be installed using the pip package installer.
All other modules used by Eddy are either part of the python standard library or included with Eddy; other modules used 
to compile the source code into an executable can be found in the requirements.txt file.

If using the source code to compile an executable, make sure to include the files in the .\static folder; if using 
pyinstaller then these should be included in the 'datas' section of a spec file. An example of such a spec file is
included in with the source code; the 'pathex' and 'datas' variables will have to be changed to match the file location
where you have Eddy installed.

Eddy can be run from the command line with the output file and any applicable scaling factor as optional arguments;
if no such arguments are supplied a GUI will appear to request them.

General CLI usage: python3 Eddy.py [-o outputfile] [-sf scaling_factor] ---> outputfile.html 

This software is provided by Cerberus Nuclear Limited "as is" and any express or implied warranties, including, 
but not limited to, the implied warranties of merchantability and fitness for a particular purpose are disclaimed. 
In no event shall cerberus nuclear limited be liable for any direct, indirect, incidental, special, exemplary, 
or consequential damages (including, but not limited to, procurement of substitute goods or services; loss of use, 
data, or profits; or business interruption) however caused and on any theory of liability, whether in contract, 
strict liability, or tort (including negligence or otherwise) arising in any way out of the use of this software, 
even if advised of the possibility of such damage.




