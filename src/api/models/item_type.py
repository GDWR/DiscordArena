from enum import Enum


class ItemType(Enum):
    """Represent the type of an Item that can be converted into int for api and database"""
    Chest: int = 1
    Weapon: int = 2
