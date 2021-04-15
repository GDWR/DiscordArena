from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel
from sqlalchemy import Column, String, Date, BigInteger

from database.db import Base


class PlayerDTO(BaseModel):
    """The base player model for serialization and deserialization with JSON"""
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


class PlayerDB(Base):
    """The player class used to help interact with `players` table in the database"""
    __tablename__ = "player"

    id = Column(BigInteger, primary_key=True)
    display_name = Column(String)
    join_date = Column(Date)
