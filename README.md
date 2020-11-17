![logo](https://cerberusnuclear.com/wp-content/uploads/2020/10/EddyLinkedin.jpg)


[![PyPI version](https://badge.fury.io/py/eddy-mc.svg)](https://badge.fury.io/py/eddy-mc)

Eddy is a HTML output generator for MCNP and SCALE, it imports an MCNP or SCALE output file, extracts the important data, and writes it to a user-friendly HTML file.

This repository contains the the source code version of Eddy, however Eddy is also available as [a pre-compiled executable](https://github.com/Cerberus-Nuclear/Eddy).

Eddy can be run from the command line with the output file and any applicable scaling factor as optional arguments; if no such arguments are supplied a GUI will appear to request them.

General CLI usage:

```bash
python3 eddy.py [-o outputfile] [-sf scaling_factor]
```

Eddy is also available on the PyPI Python Package index as eddy-mc, in order to allow easier integration into other programs. It can be installed using pip:

```bash
pip install eddy-mc
```

and accessed using:

```python
from eddymc import eddy
eddy.main()
```

where `eddy.main()` can take the same two optional arguments; the filepath for the MCNP output and a scaling factor. If these are not supplied, the GUI will appear to request them when `eddy.main()` is called.

Requirements

- Python 3.6 or later
- Jinja2 Python package is required (will be included automatically if Eddy is installed via pip)
- pytest and pytest-mock Python packages are required to run the unit tests

<details>
  <summary>Example HTML outputs</summary>
  <img src="https://cerberusnuclear.com/wp-content/uploads/2020/10/eddy-screen-shot-2.jpg" name="image-name">
  <img src="https://cerberusnuclear.com/wp-content/uploads/2020/10/Results_Summary-1.jpg" name="image-name">
  <img src="https://cerberusnuclear.com/wp-content/uploads/2020/10/Results_Stats-1.jpg" name="image-name">
  <img src="https://cerberusnuclear.com/wp-content/uploads/2020/10/WarningsComments.jpg" name="image-name">
  <img src="https://cerberusnuclear.com/wp-content/uploads/2020/10/particles-1.jpg" name="image-name">
</details>
