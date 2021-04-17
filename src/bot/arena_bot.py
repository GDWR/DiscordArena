from __future__ import annotations

from glob import glob
from pathlib import Path

import aiohttp
import discord
from discord.ext.commands import Bot


class ArenaBot(Bot):
    def __init__(self, command_prefix, *args, **kwargs):
        super().__init__(command_prefix, *args, **kwargs)
        self.session = aiohttp.ClientSession()

    async def on_ready(self):
        print(f"Logged in as {self.user}")

    async def on_disconnect(self):
        await self.session.close()

    def load_extensions(self) -> None:
        for file in map(Path, glob("bot/cogs/*.py")):
            self.load_extension(f"bot.cogs.{file.stem}")

    @classmethod
    def create(cls) -> ArenaBot:
        bot_intents = discord.Intents.default()
        bot = cls(
            command_prefix='!',
            intents=bot_intents
        )
        return bot
