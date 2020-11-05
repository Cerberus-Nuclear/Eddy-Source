## Eddy Contributor Guidelines

First off, thanks for taking the time to contribute to Eddy!

The following is a set of guidelines for contributing to Eddy, which is hosted in the Cerberus-Nuclear Organization on GitHub. 
These are guidelines, not strict rules, but following them means that your pull request is far more likely to be accepted.
Use your best judgment, and feel free to propose changes to this document in a pull request.

### Table Of Contents

 * [Code of Conduct](#code-of-conduct)
 * [Reporting Bugs](#reporting-bugs)
 * [Suggesting New Features](#suggesting-new-features)
 * [Contributing Code](#contributing-code)
 * [Python Style Guide](#python-style-guide)

### Code of Conduct

This project and everyone participating in it is governed by the [Eddy Code of Conduct](CODE_OF_CONDUCT.md). 
By participating, you are expected to uphold this code. Please report unacceptable behavior to [nuclear@cerberusnuclear.com](mailto:nuclear@cerberusnuclear.com).

### Reporting Bugs

Bugs are tracked as [GitHub issues](https://guides.github.com/features/issues/). Please check the open issues to see if this bug has already been reported. 
If the bug is mentioned in a closed issue, please open a new issue and link the closed issue in the description.

### Suggesting New Features

Improvement suggestions are tracked as [GitHub issues](https://guides.github.com/features/issues/). When suggesting an enhancement, please provide the following:
* Use a clear and descriptive title for the issue to identify the suggestion.
* Provide a step-by-step description of the suggested enhancement in as many details as possible.
* Describe the current behavior and explain which behavior you expected to see instead and why.

### Contributing Code

* Any new code contributions should be provided through a new branch, with a descriptive branch name describing the feature being introduced or the issue being resolved.
* Any new code additions should also come with relevant unit tests written with pytest (at the time of writing this guide, the pytest suite for eddy is only partially complete,
but any new code should have tests provided before it is added to the codebase).
* When a bug-fix is submitted, a new unit test should also be provided that replicates the bug, to ensure that the same bug does not re-emerge at a later stage.
* Any new modules, functions, methods or classes should start with a docstring explaining the intended behaviour, along with the name and type of any arguments and return values.

### Python Style Guide

All python code contributions are expected to be [PEP 8](https://www.python.org/dev/peps/pep-0008/) compliant to aid readability and consistency throughout the codebase. 
Non-PEP 8 compliant code may be accepted in exceptional circumstances, where divergence from the PEP significantly improves code readability.
