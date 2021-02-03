import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name="eddy_mc", 
    version="0.3.3",
    author="Cerberus Nuclear",
    author_email="nuclear@cerberusnuclear.com",
    description="Eddy, the MCNP and SCALE HTML output converter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Cerberus-Nuclear/Eddy-Source",
    packages=['eddymc', 'eddymc//mcnp', 'eddymc//scale', 'eddymc//static'],
    package_data={'eddymc//static': ['*']},
    install_requires=['Jinja2', 'importlib-resources'],
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        "Operating System :: OS Independent",
    ],
    scripts=['eddymc/eddy.py'],
    python_requires='>=3.6',
)
