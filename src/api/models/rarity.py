from enum import Enum

class Rarity(Enum):
    Poor: list[float] = [50.077, 27.337, 16.916, 4.787, 0.815, 0.066, 0.002]
    Common: list[float] = [27.738, 49.889, 16.781, 4.732, 0.777, 0.078, 0.005]
    Uncommon: list[float] = [10.5, 23.031, 55.163, 9.665, 1.455, 0.18, 0.006]
    Rare: list[float] = [0.0, 0.0, 11.403, 74.866, 13.362, 0.351, 0.018]
    Epic: list[float] = [0.0, 0.0, 0.0, 85.014, 13.451, 1.465, 0.07]
    Legendary: list[float] = [0.0, 0.0, 0.0, 10.0, 79.979, 9.509, 0.512]
    Mythical: list[float] = [0.0, 0.0, 0.0, 0.0, 10.0, 84.932, 5.068]
