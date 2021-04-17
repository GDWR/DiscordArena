import os
from typing import Any


def setting(name: str, default: Any = None, *, required: bool = False) -> str:
    """
    Get a setting from the environment.
    Default and Required cannot be set at the same time.

    :param name: Environment variable name
    :param default: Value to use if variable is not assigned in environment
    :param required: If the variable is not assigned in teh environment, raise an error
    :return:
    """

    if default and required:
        raise EnvironmentError(
            f"Environment variable cannot have a default value and be required: {name} "
        )

    env_var = os.getenv(name, default)
    if required and env_var is None:
        raise EnvironmentError(f'Missing environment variable: {name}')
    return env_var
