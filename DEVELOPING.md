# Development Setup

Prerequisite: [Install Docker](https://docs.docker.com/install) on your local environment.

The base `docker-compose.yml` has the default config for a development environment. This has predefined config and
should be used in most cases.

To run the docker-compose for development I'd recommend setting up a docker-compose interpreter for
[Pycharm](https://www.jetbrains.com/help/pycharm/using-docker-compose-as-a-remote-interpreter.html). I'm pretty sure
VSCode also has this feature but I've never used it, if you wish to update this with a useful link. Just PR it.

### Pycharm Configurations
Included in this project are Pycharm configurations file contained in .pycharm.
These should automatically be detected and used by Pycharm for ease of development.
All that is required is a docker-compose interpreter.

### Running the bot
Within your Docker workspace you can use poetry to run the bot, linting, and tests. Below are listed the commands
that you should get familiar with.

You must have a `.env` file at the root of the project with at least the `TOKEN` variable set. Below are the other
environment variables you can change. There is a [.env.example](.env.example) file that contains a environment file
without the values filled in.

### Step by Step Instructions
1. Install `poetry`, a python package manager, with pip:
```shell
pip install -U poetry
```

2. Install the necessary dependencies for this project in the root directory with:
```shell
poetry install
```

3. Install the necessary git hooks for this project in the root directory with:
```shell
poetry run task install-hooks
```

4. Run the discord bot in development with:
```shell
poetry run task bot
```


#### Known Issues
- You must [set the source roots](https://stackoverflow.com/questions/4580101/python-add-pythonpath-during-command-line-module-run) when running it with the python in the terminal. The issue may look like `ModuleNotFoundError: No module named 'config'`.


Environment Variables
----------------------
|Key            |Value                                    |Default  |
|:---:          |:---:                                    |:---:    |
|TOKEN          |Discord bot token                        |NONE     |
|COMMAND_PREFIX |Bot prefix to use for non-slash commands |a!       |
|DATABASE_HOST  |Postgres database host                   |localhost|
|DATABASE_PORT  |Postgres database port                   |5432     |
|DATABASE_USER  |Postgres database username               |postgres |
|DATABASE_PASS  |Postgres database password               |postgres |
|LOG_LEVEL      |Logging level to record                  |WARNING  |

### Commands to Remember:

`poetry run task bot` - Runs the discord bot

`poetry run task lint` - Lints the project with flake8

`poetry run task install-hooks` - Installs the git hooks for this project

`poetry run task pre-commit` - Runs the pre-commit hook across the entire project
