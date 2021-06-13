from abc import ABC, abstractmethod

from discord import Embed


class NotFound(ABC, Exception):
    """
    Base NotFound exception.

    This is subclassed to allow for more tailored error message for users.
    """
    def __init__(self, query: str):
        self.query = query

    @property
    @abstractmethod
    def embed(self) -> Embed:
        """Implements a Discord Friendly error message for the users."""
        raise NotImplementedError()


class PlayerNotFound(NotFound):
    """Raised when a Player has not been found in the database."""
    @property
    def embed(self) -> Embed:
        return Embed(title=f"Player not found", description=self.query)


class ItemNotFound(NotFound):
    """Raised when a Item has not been found in the database."""
    @property
    def embed(self) -> Embed:
        return Embed(title=f"Item not found", description=self.query)
