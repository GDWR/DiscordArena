from enum import Enum


class Rarity(Enum):
    Poor: int = 1
    Common: int = 2
    Uncommon: int = 3
    Rare: int = 4
    Epic: int = 5
    Legendary: int = 6
    Mythical: int = 7

    @property
    def weights(self) -> list[float]:
        if self.value is Rarity.Poor:
            return [50.077, 27.337, 16.916, 4.787, 0.815, 0.066, 0.002]

        if self.value is Rarity.Common:
            return [27.738, 49.889, 16.781, 4.732, 0.777, 0.078, 0.005]

        if self.value is Rarity.Uncommon:
            return [10.5, 23.031, 55.163, 9.665, 1.455, 0.18, 0.006]

        if self.value is Rarity.Rare:
            return [0.0, 0.0, 11.403, 74.866, 13.362, 0.351, 0.018]

        if self.value is Rarity.Epic:
            return [0.0, 0.0, 0.0, 85.014, 13.451, 1.465, 0.07]

        if self.value is Rarity.Legendary:
            return [0.0, 0.0, 0.0, 10.0, 79.979, 9.509, 0.512]

        if self.value is Rarity.Mythical:
            return [0.0, 0.0, 0.0, 0.0, 10.0, 84.932, 5.068]