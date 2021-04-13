from __future__ import annotations

import orm
from datetime import datetime
from pydantic import BaseModel

from database.db import metadata, database


class PlayerDTO(BaseModel):
    id: int
    display_name: str
    join_date: datetime

    @classmethod
    def from_db(cls, player: PlayerDB) -> PlayerDTO:
        return cls(
            id=player.id,
            display_name=player.display_name,
            join_date=player.join_date
        )


class PlayerDB(orm.Model):
    __tablename__ = "player"
    __metadata__ = metadata
    __database__ = database

    id = orm.Integer(primary_key=True)
    display_name = orm.String(max_length=100)
    join_date = orm.DateTime()
