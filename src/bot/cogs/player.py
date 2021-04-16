from aiohttp import ClientResponseError
from discord.ext.commands import Context, Cog, command

from constants import environment
from ..arena_bot import ArenaBot


class Player(Cog):
    def __init__(self, bot: ArenaBot):
        self.bot = bot
        self._api_url = f"http://{environment.API_URL}"

    @command()
    async def join(self, ctx: Context):
        params = {
            "id": ctx.author.id,
            "display_name": ctx.author.display_name
        }

        async with self.bot.session.post(f"{self._api_url}/player", params=params) as response:
            try:
                response.raise_for_status()
                data = await response.json()
                await ctx.send(f"> {data}")
            except ClientResponseError:
                await ctx.send("> You already exist")


def setup(bot: ArenaBot):
    bot.add_cog(Player(bot))
