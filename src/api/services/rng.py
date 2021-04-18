from random import choices
from models import Rarity
from typing import Union


class RNG:
    """
    Class to be used when rolling for rarities.

    It's weights can be changed during initalisation by passing in
    a Rarity or a list of floats.
    >>> rng = RNG()
    >>> rng.roll() # Rolls using default weights
    >>>
    >>> rng = RNG(Rarity.Epic)
    >>> rng.roll() # Rolls using weights tailored towards Epic Rarity
    >>>
    >>> rng = RNG([50.077, 27.337, 16.916, 4.787, 0.815, 0.066, 0.002])
    >>> rng.roll() # Rolls using weights defined in the init.
    """

    def __init__(self, rarity_weights: Union[Rarity, list[float]] = None):
        if rarity_weights is None:
            self.weights = Rarity.Poor.weights

        else:
            if isinstance(rarity_weights, Rarity):
                self.weights = rarity_weights.weights

            elif isinstance(rarity_weights, list):
                self.weights = rarity_weights

        self.rewards: list[Rarity] = [
            Rarity.Poor,
            Rarity.Common,
            Rarity.Uncommon,
            Rarity.Rare,
            Rarity.Epic,
            Rarity.Legendary,
            Rarity.Mythical,
        ]

    def roll(self, k: int = 1) -> list[Rarity]:
        """
        :param k: The amount of times to roll
        :return: The rarities rolled
        """
        return choices(self.rewards, self.weights, k=k)
