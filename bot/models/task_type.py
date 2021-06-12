from enum import Enum

from discord import Colour


class TaskType(Enum):
    """Represent the type of an Task"""
    Hunt = 1
    Mine = 2
    Gather = 3
    Lumber = 4

    @property
    def colour(self) -> int:
        """Get the associated colour of a Task."""
        if self is TaskType.Hunt:
            return Colour.dark_gold()
        elif self is TaskType.Mine:
            return Colour.dark_gray()
        elif self is TaskType.Gather:
            return Colour.blue()
        elif self is TaskType.Lumber:
            return Colour.from_rgb(165, 42, 42)  # Brown
        else:
            return Colour.blurple()
