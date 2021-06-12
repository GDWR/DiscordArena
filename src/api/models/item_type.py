from enum import Enum


class ItemType(Enum):
    """Represent the type of an Item that can be converted into int for api and database"""
    Chest = 1
    Weapon = 2
