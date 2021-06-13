from __future__ import annotations

from orm import BigInteger, Model

from bot.database import Database


class Guild(Model):
    """Representation of a Guild, this is a Database Object."""
    __tablename__ = "guild"
    __database__ = Database.database
    __metadata__ = Database.metadata

    id = BigInteger(primary_key=True, index=True)
