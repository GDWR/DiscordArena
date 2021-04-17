from random import choices
from models import Rarity
from typing import Union


class RNG:
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
