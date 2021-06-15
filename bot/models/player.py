from __future__ import annotations

from datetime import datetime

from discord import Colour, Embed
from orm import BigInteger, DateTime, Integer, Model

from arena_bot import ArenaBot
from database import Database


class Player(Model):
    """Representation of a Player, this is a Database Object."""

    __tablename__ = "player"
    __database__ = Database.database
    __metadata__ = Database.metadata

    id = BigInteger(primary_key=True, index=True)
    colour = Integer(default=lambda: Colour.random().value)
    coin = Integer(default=0)
    item_counter = Integer(default=0)
    join_date = DateTime(default=datetime.utcnow)

    @property
    async def embed(self) -> Embed:
        """Get a Embed that represents the Player"""
        bot = ArenaBot.instance

        if (discord_user := bot.get_user(self.id)) is None:
            discord_user = await bot.fetch_user(self.id)

        embed = Embed(
            title=discord_user.name,
            description=f"Coins: {self.coin}",
            colour=self.colour
        )

        embed.set_author(name=discord_user.display_name, icon_url=discord_user.avatar_url)
        return embed
