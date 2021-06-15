# Development Setup

This project is using Poetry as its package manager and virtual environment.
[Install Poetry](https://python-poetry.org/docs/)

> "I'm the Poetry Guru, High-level King and All-stack Developer." - [DudeBro249](https://github.com/DudeBro249)

## Running the bot

#### Step-by-step Instructions
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
4. Create a `.env` and update the [settings](#Settings)
```shell
cp .env.example .env
```
5. Run the discord bot in development with:
```shell
poetry run task bot
```

### Commands to Remember:
+ `poetry run task bot` - Runs the discord bot
+ `poetry run task lint` - Lints the project with flake8
+ `poetry run task install-hooks` - Installs the git hooks for this project
+ `poetry run task pre-commit` - Runs the pre-commit hook across the entire project

### Pycharm Configurations
Included in this project are Pycharm configurations file contained in `.pycharm`. These should automatically be
detected and used by Pycharm for ease of development.
The [Poetry Plugin](https://plugins.jetbrains.com/plugin/14307-poetry) Should be able to detect our poetry config
and install automatically.

### Settings
You must have a `.env` file at the root of the project with at least the `TOKEN` variable set. Below are the other
environment variables you can change. There is a [.env.example](../.env.example) file that contains an example environment
file without the required values filled in.

#### Main Environment Variables
|Key            |Description                              |Default  |
|:---:          |:---:                                    |:---:    |
|TOKEN          |Discord bot token                        |NONE     |
|COMMAND_PREFIX |Bot prefix to use for non-slash commands |a!       |
|DATABASE_HOST  |Postgres database host                   |localhost|
|DATABASE_PORT  |Postgres database port                   |5432     |
|DATABASE_USER  |Postgres database username               |postgres |
|DATABASE_PASS  |Postgres database password               |postgres |
|LOG_LEVEL      |Logging level to record                  |WARNING  |


### Known Issues
- You must [set the source roots](https://stackoverflow.com/questions/4580101/python-add-pythonpath-during-command-line-module-run) when running it with the python in the terminal. The issue may look like `ModuleNotFoundError: No module named 'config'`.
