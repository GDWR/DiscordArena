from enum import Enum

from discord import Colour


class Rarity(Enum):
    """Represent rarity within Discord Arena."""
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

    @property
    def weights(self) -> list[float]:
        """Get the weights of the Rarity for RNG."""
        if self is Rarity.Poor:
            return [50.077, 27.337, 16.916, 4.787, 0.815, 0.066, 0.002]

        if self is Rarity.Common:
            return [27.738, 49.889, 16.781, 4.732, 0.777, 0.078, 0.005]

        if self is Rarity.Uncommon:
            return [10.5, 23.031, 55.163, 9.665, 1.455, 0.18, 0.006]

        if self is Rarity.Rare:
            return [0.0, 0.0, 11.403, 74.866, 13.362, 0.351, 0.018]

        if self is Rarity.Epic:
            return [0.0, 0.0, 0.0, 85.014, 13.451, 1.465, 0.07]

        if self is Rarity.Legendary:
            return [0.0, 0.0, 0.0, 10.0, 79.979, 9.509, 0.512]

        if self is Rarity.Mythical:
            return [0.0, 0.0, 0.0, 0.0, 10.0, 84.932, 5.068]
