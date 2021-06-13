from __future__ import annotations

import asyncio
from glob import glob
from pathlib import Path

from aiohttp import ClientSession
from discord import Intents
from discord.ext.commands import Bot, Context, CommandInvokeError
from orm import NoMatch

from config import COMMAND_PREFIX
from database import Database


class ArenaBot(Bot):
    """
    Subclass of `discord.ext.commands.Bot`

    This adds additional functionality:
     * aiohttp session
     * Singleton
     * load_extensions
    """
    instance = None

    # flake8: noqa: D102
    def __new__(cls, *args, **kwargs) -> ArenaBot:
        if cls.instance is None:
            cls.instance = super(ArenaBot, cls).__new__(cls)
        return cls.instance

    def __init__(self, command_prefix: str, *args, **kwargs):
        super().__init__(command_prefix, case_sensitive=False, *args, **kwargs)
        self.session = ClientSession()
        self.database = Database()
        asyncio.ensure_future(self.database.connect())

    async def on_ready(self) -> None:
        """Task when the bot logs in and is connected to the gateway."""
        print(f"Logged in as {self.user}")

    async def on_disconnect(self) -> None:
        """Task when the bot disconnects from the gateway."""
        await self.session.close()

    async def on_command_error(self, ctx: Context, exception: CommandInvokeError):
        """Handle global command errors."""
        if isinstance(exception.original, NoMatch):
            await ctx.reply(f"Please register your account with `{self.command_prefix}join`")
        else:
            raise exception



    def load_extensions(self) -> None:
        """Iterate through all the `.py` files found int `bot/cogs` and load them as cogs."""
        for file in map(Path, glob("bot/cogs/*.py")):
            self.load_extension(f"cogs.{file.stem}")

    @classmethod
    def create(cls) -> ArenaBot:
        """Create the instance of the bot"""
        bot_intents = Intents.default()
        bot = cls(
            command_prefix=COMMAND_PREFIX,
            intents=bot_intents
        )
        return bot
