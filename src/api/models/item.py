import orm
from database.db import database as db
from database.db import metadata
from pydantic import BaseModel


class ItemTable(orm.Model):
    """The ItemTable class used to help interact with `item` table in the database"""
    __tablename__ = "item"
    __database__ = db
    __metadata__ = metadata

    id = orm.Integer(primary_key=True, index=True)
    name = orm.String(max_length=50)
    owner_id = orm.Integer()
    value = orm.Integer()
    rarity = orm.Integer()


class ItemIn(BaseModel):
    """The base item input class"""
    name: str
    owner_id: int
    value: int
    rarity: int


class Item(ItemIn):
    """The output item class"""
    id: int

    class Config:
        """Allows subclassing other orm.Models"""
        orm_mode = True
