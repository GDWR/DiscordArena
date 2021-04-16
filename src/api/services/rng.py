from random import choices
from models import Rarity
from typing import Union


class RNG:
    def __init__(self, weights: Union[Rarity, list[int]] = None):
        if weights is None:
            self.weights = Rarity.Poor.value

        else:
            if isinstance(weights, Rarity):
                self.weights = weights.value

            elif isinstance(weights, list):
                self.weights = weights

        self.rewards: list[Rarity] = [
            Rarity.Poor,
            Rarity.Common,
            Rarity.Uncommon,
            Rarity.Rare,
            Rarity.Epic,
            Rarity.Legendary,
            Rarity.Mythical,
        ]

    def roll(self, k: int = 1) -> Rarity:
        return choices(self.rewards, self.weights, k=k)
