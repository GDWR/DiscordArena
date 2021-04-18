from dataclasses import dataclass, field
from typing import Union

from discord import Embed
from models.rarity import Rarity

from arena_bot import ArenaBot


@dataclass
class Item:
    """
    Representation of an Item

    This closely matches the Schema from the API.
    """

    id: int
    name: str
    owner_id: int
    value: int
    rarity: Rarity
    _rarity: Rarity = field(init=False, repr=False)

    @property
    def embed_field(self) -> dict[str, str]:
        """Get a embed field that represents the Item"""
        return {
            "name": f"`{self.id}` | {self.rarity.emoji} {self.name}",
            "value": f"Value: {self.value}"
        }

    @property
    async def embed(self) -> Embed:
        """Get a Embed that represents the Item"""
        embed = Embed(title=f"{self.rarity.emoji} {self.name}", colour=self.rarity.colour)
        embed.add_field(name="Item ID", value=str(self.id))
        embed.add_field(name="Value", value=str(self.value))

        bot = ArenaBot.instance
        owner = bot.get_user(self.owner_id)
        if owner is None:
            owner = await bot.fetch_user(self.owner_id)

        embed.set_author(name=owner.display_name, icon_url=owner.avatar_url)
        return embed

    @property
    def rarity(self) -> Rarity:
        """
        Get the rarity of the item.

        This has been done as a property to
        allow it to be set as a `str`, `int` or `Rarity`
        while being correctly be set as a `Rarity` type.
        """
        return self._rarity

    @rarity.setter
    def rarity(self, value: Union[int, str, Rarity]) -> None:
        if isinstance(value, int):
            self._rarity = Rarity(value)
        elif isinstance(value, Rarity):
            self._rarity = value
        elif isinstance(value, str):
            self._rarity = Rarity[value]
        else:
            raise TypeError(f"Cannot convert type of: {type(value)}")
