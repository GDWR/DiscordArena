# Contributing

Before contributing, please either claim an existing open issue or create a new issue to discuss your 
proposed changes with the core developers of this repo before making any changes.

When contributing to this project it must be done via a Fork.

### Branch naming
Branches should pre-fixed with either `bug/`, `feature/` or `documentation/` based on what they are made 
to accomplish.

### Flake8
A GitHub action has been created to run pylint on the repo during the pull request stage. 
If this fails, your pull request will not be accepted. 

This can be ran by using while in the root of the repo.

`pip3 install flake8 flake8-docstrings`
`python3 -m flake8 src/api`

### Development Environment
For documentation on the developing environment see [DEVELOPING](DEVELOPING.md)
