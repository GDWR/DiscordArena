from os import getenv
from typing import Optional, Type, TypeVar

T = TypeVar("T")


def setting(name: str, default: Optional[T] = None, *, required: bool = False, _type: Type[T] = str) -> T:
    """
    Get a setting from the environment.
    Default and Required cannot be set at the same time.

    :param name: Environment variable name
    :param default: Value to use if variable is not assigned in environment, this will be converted to string
    :param required: If the variable is not assigned in the environment, raise an error
    :param _type: Cast the variable to the type specified
    :return: Environment variable casted to the `_type`
    """

    if default and required:
        raise EnvironmentError(
            f"Environment variable cannot have a default value and be required: {name} "
        )

    env_var = getenv(name, default)
    if env_var == "":
        env_var = default

    if required and env_var is None:
        raise EnvironmentError(f'Missing environment variable: {name}')

    if _type is not None:
        try:
            env_var = _type(env_var)
        except (TypeError, ValueError) as err:
            print(f"Could not convert Env Var {name} into type {_type}: {err}")
            exit()

    return env_var
