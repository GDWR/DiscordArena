from __future__ import annotations

from datetime import datetime

from discord import Embed, Colour
from orm import DateTime, BigInteger, Model, Integer

from bot.arena_bot import ArenaBot
from bot.database import Database


class Player(Model):
    """Representation of a Player, this is a Database Object."""
    __tablename__ = "player"
    __database__ = Database.database
    __metadata__ = Database.metadata

    id = BigInteger(primary_key=True, index=True)
    colour = Integer(default=lambda: Colour.random().value)
    join_date = DateTime(default=datetime.utcnow)

    @property
    async def embed(self) -> Embed:
        """Get a Embed that represents the Player"""
        bot = ArenaBot.instance

        if (discord_user := bot.get_user(self.id)) is None:
            discord_user = await bot.fetch_user(self.id)

        embed = Embed(title=discord_user.name, colour=self.colour)

        embed.set_author(name=discord_user.display_name, icon_url=discord_user.avatar_url)
        return embed
