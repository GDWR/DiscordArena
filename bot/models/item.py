from __future__ import annotations

import random

from discord import Embed
from orm import Model, Integer, String, ForeignKey

from bot.arena_bot import ArenaBot
from bot.database import Database
from bot.models.rarity import Rarity
from .player import Player
from .item_type import ItemType


class ItemFactory:
    """Factory to contain the generic ways to create Items."""

    @staticmethod
    async def random(owner_id: int) -> Item:
        """Generate a fully random item."""
        return await Item.objects.create(
            name="Random",
            owner_id=owner_id,
            value=random.randint(1, 100),
            _rarity=random.choice(list(Rarity)).value,
            _item_type=random.choice(list(ItemType)).value
        )


class Item(Model):
    """Representation of an Item, this is a Database Object."""
    __tablename__ = "item"
    __database__ = Database.database
    __metadata__ = Database.metadata

    id = Integer(primary_key=True, index=True)
    name = String(max_length=50)
    player = ForeignKey(Player)
    value = Integer()
    _rarity = Integer()
    _item_type = Integer()

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
        owner = bot.get_user(self.player)
        if owner is None:
            owner = await bot.fetch_user(self.player)

        embed.set_author(name=owner.display_name, icon_url=owner.avatar_url)
        return embed

    @property
    def rarity(self) -> Rarity:
        """Get the rarity of the item."""
        return Rarity(self._rarity)

    @rarity.setter
    def rarity(self, value: Rarity) -> None:
        self._rarity = value.value

    @property
    def item_type(self) -> ItemType:
        """Get the type of the item."""
        return ItemType(self._item_type)

    @item_type.setter
    def item_type(self, value: ItemType) -> None:
        self._item_type = value.value
