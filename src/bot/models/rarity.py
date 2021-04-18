from enum import Enum

from discord import Colour


class Rarity(Enum):
    """
    This represents the Rarity of an object.
    This matches the database schema from the API
    """
    Poor = 1
    Common = 2
    Uncommon = 3
    Rare = 4
    Epic = 5
    Legendary = 6
    Mythical = 7

    @property
    def colour(self) -> Colour:
        """Get the associated Colour with the Rarity"""
        if self is Rarity.Poor:
            return Colour.dark_gray()
        elif self is Rarity.Common:
            return Colour.lighter_gray()
        elif self is Rarity.Uncommon:
            return Colour.green()
        elif self is Rarity.Rare:
            return Colour.blue()
        elif self is Rarity.Epic:
            return Colour.purple()
        elif self is Rarity.Legendary:
            return Colour.orange()
        elif self is Rarity.Mythical:
            return Colour.red()

    @property
    def emoji(self) -> str:
        """Get the associated emoji of the Rarity"""
        if self is Rarity.Poor:
            return "<:Poor:778072653604716566>"
        elif self is Rarity.Common:
            return "<:Common:650371678861393951>"
        elif self is Rarity.Uncommon:
            return "<:Uncommon:650371677821337601>"
        elif self is Rarity.Rare:
            return "<:Rare:650371680463749120>"
        elif self is Rarity.Epic:
            return "<:Epic:650371673731760165>"
        elif self is Rarity.Legendary:
            return "<:Legendary:650371681709457408>"
        elif self is Rarity.Mythical:
            return "<:Mythical:650371681050951700>"
