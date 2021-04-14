import aiohttp
from discord.ext.commands import Bot


class ArenaBot(Bot):
    def __init__(self, command_prefix, *args, **kwargs):
        super().__init__(command_prefix, *args, **kwargs)

        self.session = aiohttp.ClientSession()

    @staticmethod
    async def on_ready():
        print("Hi, I am here")
