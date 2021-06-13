import logging


class Log(object):
    """
    Class to be used as a decorator to log function execution.

    The name of the logger can be changed during initalisation by passing
    the name as a string.
    >>> @Log()
    ... def my_func():
    ...     pass
    ...
    >>> my_func()
    INFO:Calling my_func
    """

    def __init__(self, name: str = __name__):
        self.logger = logging.getLogger(name)

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            self.logger.info(f"Calling {func.__name__}")
            return func(*args, **kwargs)

        return wrapper
