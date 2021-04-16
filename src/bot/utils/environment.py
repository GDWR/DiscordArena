import os
from typing import Any
from dotenv import load_dotenv


def load_env_dev() -> None:
    """Loads environment variables if application is being run in the development environment"""
    if os.getenv("ENVIRONMENT") is None:
        load_dotenv()


def setting(name: str, default: Any = None) -> str:
    """Retrieves an environment variable and if it does not exist, throws an `EnvironmentError`"""
    load_env_dev()
    environment_variable = os.getenv(name)
    if not environment_variable:
        if not default:
            raise EnvironmentError(f'Missing environment variable: {name}')
        return str(default)
    return str(environment_variable)
