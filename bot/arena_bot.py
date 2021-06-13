from __future__ import annotations

import asyncio
from glob import glob
from pathlib import Path
import logging

from aiohttp import ClientSession
from discord import Intents
from discord.ext.commands import Bot, Context, CommandInvokeError

from config import COMMAND_PREFIX
from database import Database
from exceptions import NotFound


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
        self.logger = logging.getLogger(__name__)
        self.session = ClientSession()
        self.database = Database()
        asyncio.ensure_future(self.database.connect())

    async def on_ready(self) -> None:
        """Task when the bot logs in and is connected to the gateway."""
        self.logger.info(f"Bot Logged in as {self.user}")

    async def on_disconnect(self) -> None:
        """Task when the bot disconnects from the gateway."""
        self.logger.info("Bot Disconnected")
        await self.session.close()

    async def on_command_error(self, ctx: Context, exception: CommandInvokeError):
        """Handle global command errors."""
        if hasattr(exception, 'original') and isinstance(exception.original, NotFound):
            await ctx.reply(embed=exception.original.embed)
        else:
            raise exception

    def load_extensions(self) -> None:
        """Iterate through all the `.py` files found int `bot/cogs` and load them as cogs."""
        for file in map(Path, glob("cogs/*.py")):
            self.load_extension(f"cogs.{file.stem}")
            self.logger.info(f"Loaded cogs.{file.stem}")

    @classmethod
    def create(cls) -> ArenaBot:
        """Create the instance of the bot"""
        bot_intents = Intents.default()
        bot = cls(command_prefix=COMMAND_PREFIX, intents=bot_intents)
        return bot
