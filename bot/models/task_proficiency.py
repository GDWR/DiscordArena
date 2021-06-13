from __future__ import annotations

from orm import Model, Integer, ForeignKey

from config import PROFICIENCY_EXP_PER_LEVEL
from database import Database
from .task_type import TaskType
from .player import Player


class TaskProficiency(Model):
    """Representation of a Player Task Proficiency, this is a Database Object."""
    __tablename__ = "task_proficiency"
    __database__ = Database.database
    __metadata__ = Database.metadata

    id = Integer(primary_key=True, index=True)
    player = ForeignKey(Player)
    hunt_exp: int = Integer(default=0)
    gather_exp: int = Integer(default=0)
    mine_exp: int = Integer(default=0)
    lumber_exp: int = Integer(default=0)

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

    def task_level(self, task_type: TaskType) -> int:
        """Get the level for the task supplied"""
        if task_type is TaskType.Hunt:
            return self.hunt_level
        elif task_type is TaskType.Gather:
            return self.gather_level
        elif task_type is TaskType.Mine:
            return self.mine_level
        elif task_type is TaskType.Lumber:
            return self.lumber_level

    async def increment_exp(self, task_type: TaskType, amount: int) -> None:
        """Add experience to a task."""
        if task_type is TaskType.Hunt:
            await self.update(hunt_exp=self.hunt_exp + amount)
        elif task_type is TaskType.Gather:
            await self.update(gather_exp=self.gather_exp + amount)
        elif task_type is TaskType.Mine:
            await self.update(mine_exp=self.mine_exp + amount)
        elif task_type is TaskType.Lumber:
            await self.update(lumber_exp=self.lumber_exp + amount)

    @property
    def embed_fields(self) -> list[dict[str, str]]:
        """Get a list of embed fields that represents the Users Proficiencies"""
        return [
            {"name": f"`{task.name}`", "value": f"{level}"}
            for task, level in [(task_type, self.task_level(task_type)) for task_type in list(TaskType)]
        ]
