import aiohttp
from discord.ext.commands import Bot


class ArenaBot(Bot):
    def __init__(self, command_prefix, *args, **kwargs):
        super().__init__(command_prefix, *args, **kwargs)

        self.session = aiohttp.ClientSession()

    async def on_ready(self):
        print(f"Logged in as {self.user}")

    async def on_disconnect(self):
        await self.session.close()
