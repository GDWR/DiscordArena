from __future__ import annotations

import datetime

import orm
from database.db import database as db
from database.db import metadata
from pydantic import BaseModel, Field


class PlayerTable(orm.Model):
    """The player class used to help interact with `player` table in the database"""
    __tablename__ = "player"
    __database__ = db
    __metadata__ = metadata

    id = orm.Integer(primary_key=True, index=False)
    display_name = orm.String(max_length=50)
    join_date = orm.DateTime()


class PlayerIn(BaseModel):
    """API model to represent the data sent when creating a new Player."""
    id: int
    display_name: str


class Player(PlayerIn):
    """Represent the data sent to a client from the API."""
    join_date: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
