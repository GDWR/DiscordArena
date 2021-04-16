import aiohttp
from discord.ext.commands import Bot
from glob import glob
from pathlib import Path


class ArenaBot(Bot):
    def __init__(self, command_prefix, *args, **kwargs):
        super().__init__(command_prefix, *args, **kwargs)

        self.session = aiohttp.ClientSession()

    async def on_ready(self):
        print(f"Logged in as {self.user}")
    
    async def on_disconnect(self):
        await self.session.close()
    
    @classmethod
    def create(cls) -> 'ArenaBot':
        bot = cls(
            command_prefix='!'
        )
        for file in map(Path, glob(".cogs/*.py")):
            bot.load_extension(f"cogs.{file.stem}")

        return bot
