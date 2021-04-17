from __future__ import annotations

import datetime
from pydantic import BaseModel

from ..database.db import metadata, database
import orm


class PlayerOut(BaseModel):
    """The base player model for serialization and deserialization with JSON"""
    record_id: int
    discord_id: int
    display_name: str
    join_date: datetime.date

class PlayerIn(BaseModel):
    """The base player model for serialization and deserialization with JSON"""
    discord_id: int
    display_name: str
    join_date: datetime.date

class PlayerNew(BaseModel):
    """The base player model for serialization and deserialization with JSON"""
    discord_id: int
    display_name: str

class PlayerTable(orm.Model):
    __tablename__ = "player"
    __database__ = database
    __metadata__ = metadata

    record_id = orm.Integer(primary_key=True)
    discord_id = orm.Integer()
    display_name = orm.String(max_length=100)
    join_date = orm.Date()
