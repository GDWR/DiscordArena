from random import choices


class RNG:
    rarities: list[str] = [
        "Poor",
        "Common",
        "Uncommon",
        "Rare",
        "Epic",
        "Legendary",
        "Mythical",
    ]

    def poor(
        weights: list[int] = [50.077, 27.337, 16.916, 4.787, 0.815, 0.066, 0.002],
        rolls: int = 1,
    ):
        return choices(RNG.rarities, weights, k=rolls)

    def common(
        weights: list[int] = [27.738, 49.889, 16.781, 4.732, 0.777, 0.078, 0.005],
        rolls: int = 1,
    ):
        return choices(RNG.rarities, weights, k=rolls)

    def uncommon(
        weights: list[int] = [10.5, 23.031, 55.163, 9.665, 1.455, 0.18, 0.006],
        rolls: int = 1,
    ):
        return choices(RNG.rarities, weights, k=rolls)

    def rare(
        weights: list[int] = [0.0, 0.0, 11.403, 74.866, 13.362, 0.351, 0.018],
        rolls: int = 1,
    ):
        return choices(RNG.rarities, weights, k=rolls)

    def epic(
        weights: list[int] = [0.0, 0.0, 0.0, 85.014, 13.451, 1.465, 0.07],
        rolls: int = 1,
    ):
        return choices(RNG.rarities, weights, k=rolls)

    def legendary(
        weights: list[int] = [0.0, 0.0, 0.0, 10.0, 79.979, 9.509, 0.512], rolls: int = 1
    ):
        return choices(RNG.rarities, weights, k=rolls)

    def mythical(
        weights: list[int] = [0.0, 0.0, 0.0, 0.0, 10.0, 84.932, 5.068], rolls: int = 1
    ):
        return choices(RNG.rarities, weights, k=rolls)
