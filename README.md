# Eddy

Eddy is a HTML output generator for MCNP and SCALE. It was created by Cerberus Nuclear. Cerberus Nuclear accepts no 
responsibility for the accuracy of any results presented with Eddy. 

Eddy taken an MCNP or SCALE output file, extracts the important data, 
and writes it to a user-friendly HTML file. 

All the code within this project is covered by GPLv3, the GNU Public Licence, Version 3, June 2007. A full copy of this 
licence is included with the source code; more information can be found at <https://www.gnu.org/licenses/>.

Eddy can be downloaded as either a pre-compiled executable, <from https://github.com/Cerberus-Nuclear/Eddy>,
or as source code from <https://github.com/Peter-Evans-Cerberus/Eddy-source>.

If using the executable version of Eddy, the logo that appears on the HTML output from Eddy will be whatever is saved 
as "Logo.png" in the \static directory. This logo can therefore be changed to the logo of your company by placing that 
logo in the \static directory and renaming it "Logo.png".

Eddy can be run from the command line with the output file and any applicable scaling factor as optional arguments;
if no such arguments are supplied a GUI will appear to request them.

The source code for Eddy can be run with python; if doing so python 3.6 or later is required, and the Jinja2 python 
package is needed; this can be installed using the pip package installer.
All other modules used by Eddy are either part of the python standard library or included with Eddy; other modules used 
to compile the source code into an executable can be found in the requirements.txt file.

General CLI usage: python3 Eddy.py [-o outputfile] [-sf scaling_factor] ---> outputfile.html 




