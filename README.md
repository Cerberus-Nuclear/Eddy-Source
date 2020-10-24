![logo](https://cerberusnuclear.com/wp-content/uploads/2020/10/EddyLinkedin.jpg)

Eddy is a HTML output generator for MCNP and SCALE, it imports an MCNP or SCALE output file, extracts the important data, and writes it to a user-friendly HTML file.

This repository contains the the source code version of Eddy, however Eddy is also available as [a pre-compiled executable](https://github.com/Cerberus-Nuclear/Eddy).

Eddy can be run from the command line with the output file and any applicable scaling factor as optional arguments; if no such arguments are supplied a GUI will appear to request them.

General CLI usage: 
```bash
python3 eddy.py [-o outputfile] [-sf scaling_factor]
```

Requirements
- Python 3.6 or later 
- Jinja2 Python package is required

<details>
  <summary>Example HTML outputs</summary>
  <img src="https://cerberusnuclear.com/wp-content/uploads/2020/10/eddy-screen-shot-2.jpg" name="image-name">
  <img src="https://cerberusnuclear.com/wp-content/uploads/2020/10/Results_Summary-1.jpg" name="image-name">
  <img src="https://cerberusnuclear.com/wp-content/uploads/2020/10/Results_Stats-1.jpg" name="image-name">
  <img src="https://cerberusnuclear.com/wp-content/uploads/2020/10/WarningsComments.jpg" name="image-name">
  <img src="https://cerberusnuclear.com/wp-content/uploads/2020/10/particles-1.jpg" name="image-name">
</details>
