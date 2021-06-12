from __future__ import annotations

from orm import DateTime, BigInteger, Model

from database import Database


class Player(Model):
    """Representation of a Player, this is a Database Object."""
    __tablename__ = "player"
    __database__ = Database.database
    __metadata__ = Database.metadata

    id = BigInteger(primary_key=True, index=True)
    join_date = DateTime()
