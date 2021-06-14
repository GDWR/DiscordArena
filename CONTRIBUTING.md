# Contributing

Before contributing, please either claim an existing open issue or create a new issue to discuss your
proposed changes with the core developers of this repo before making any changes.

When contributing to this project it must be done via a Fork.

### Branch naming
Branches should pre-fixed with either `bug/`, `feature/` or `documentation/` based on what they are made
to accomplish.

### Flake8
A GitHub action has been created to run flake8 on the repo during the pull request stage.
If this fails, your pull request will not be accepted.

You can run linting using commands from the root of the repo.

`poetry install` - Installs all poetry dependencies

`poetry run task lint` - Lints the project using flake8

See [here](/DEVELOPING.md#commands-to-remember) for more useful commands

### Development Environment
For documentation on the developing environment see [here](DEVELOPING.md)
