from __future__ import annotations

from orm import Model, Integer, ForeignKey

from config import PROFICIENCY_EXP_PER_LEVEL
from database import Database
from .player import Player


class TaskProficiency(Model):
    """Representation of a Player Task Proficiency, this is a Database Object."""
    __tablename__ = "task_proficiency"
    __database__ = Database.database
    __metadata__ = Database.metadata

    id = Integer(primary_key=True, index=True)
    player = ForeignKey(Player)
    hunt_exp: int = Integer()
    gather_exp: int = Integer()
    mine_exp: int = Integer()
    lumber_exp: int = Integer()

    @staticmethod
    def _exp_to_level(exp: int) -> int:
        """
        Get the current level from exp.

        This has been made as a function to make
        it easier to change the functionality at a
        later date.
        """
        return exp // PROFICIENCY_EXP_PER_LEVEL

    @property
    def hunt_level(self) -> int:
        """Retrieve the hunt_level from the users exp"""
        return self._exp_to_level(self.hunt_exp)

    @property
    def gather_level(self) -> int:
        """Retrieve the gather_level from the users exp"""
        return self._exp_to_level(self.gather_exp)

    @property
    def mine_level(self) -> int:
        """Retrieve the mine_level from the users exp"""
        return self._exp_to_level(self.mine_exp)

    @property
    def lumber_level(self) -> int:
        """Retrieve the lumber_level from the users exp"""
        return self._exp_to_level(self.lumber_exp)
