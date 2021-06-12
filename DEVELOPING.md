# Development Setup

Prerequisite: [Install Docker](https://docs.docker.com/install) on your local environment.

The base `docker-compose.yml` has the default config for a development environment. This has predefined config and 
should be used in most cases. 

To run the docker-compose for development I'd recommend setting up a docker-compose interpreter for 
[Pycharm](https://www.jetbrains.com/help/pycharm/using-docker-compose-as-a-remote-interpreter.html). I'm pretty sure 
VSCode also has this feature but I've never used it, if you wish to update this with a useful link. Just PR it.

### Running the bot
Within your Docker workspace you can use poetry to run the bot, run linting and run tests. Below are listed the commands
that you should get familiar with.

You must have a `.env` file at the root of the project with atleast the `TOKEN` variable set. Below are the other 
environment variables you can change. There is a [.env.example](.env.example) file that contains a environment file 
without the values filled in.

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