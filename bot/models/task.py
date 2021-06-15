from __future__ import annotations

from discord import Embed
from orm import BigInteger, Boolean, DateTime, ForeignKey, Integer, Model

from database import Database
from .task_type import TaskType
from .player import Player


class Task(Model):
    """Representation of a Task, this is a Database Object."""

    __tablename__ = "task"
    __database__ = Database.database
    __metadata__ = Database.metadata

    id = BigInteger(primary_key=True, index=True)
    player = ForeignKey(Player)
    completed = Boolean(default=False)
    _task_type = Integer()
    completion_date = DateTime()

    @property
    def task_type(self) -> TaskType:
        """Get the type of the task."""
        return TaskType(self._task_type)

    @task_type.setter
    def task_type(self, value: TaskType) -> None:
        self._task_type = value.value

    @property
    async def embed(self) -> Embed:
        """Get the embed representing the task."""
        return Embed(
            title=self.task_type.name,
            description=f"Completes at {self.completion_date}",
            colour=self.task_type.colour
        )
