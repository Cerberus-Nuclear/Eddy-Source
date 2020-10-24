# Eddy

![logo](https://cerberusnuclear.com/wp-content/uploads/2020/10/EddyLinkedin.jpg)

Eddy is a HTML output generator for MCNP and SCALE, it imports an MCNP or SCALE output file, extracts the important data, and writes it to a user-friendly HTML file.

This is the executable version of Eddy. The exectuable itself is the
Eddy_beta_02.exe file found in the top level Eddy folder. It can be run simply
by double-clicking on this executable.

Eddy can be run from the command line with the output file and any applicable scaling factor as optional arguments; if no such arguments are supplied a GUI
will appear to request them.

General CLI usage: 
```bash
python3 eddy.py [-o outputfile] [-sf scaling_factor] ---> outputfile.html
```

Eddy can be downloaded as:
- [a pre-compiled executable](https://github.com/Cerberus-Nuclear/Eddy)
- [source code](https://github.com/Cerberus-Nuclear/Eddy-Source)

The source code for Eddy can be run with python 3.6 or later and the Jinja2
python package is required. All other modules used by Eddy are either part of
the python standard library or included with Eddy; other modules used to
compile the source code into an executable can be found in the requirements.txt file.

<details>
  <summary>Example HTML outputs</summary><details>
  <img src="https://cerberusnuclear.com/wp-content/uploads/2020/10/eddy-screen-shot-2.jpg" name="image-name">
  <img src="https://cerberusnuclear.com/wp-content/uploads/2020/10/Results_Summary-1.jpg" name="image-name">
  <img src="https://cerberusnuclear.com/wp-content/uploads/2020/10/Results_Stats-1.jpg" name="image-name">
  <img src="https://cerberusnuclear.com/wp-content/uploads/2020/10/WarningsComments.jpg" name="image-name">
  <img src="https://cerberusnuclear.com/wp-content/uploads/2020/10/particles-1.jpg" name="image-name">
</details>
