from aiohttp import ClientResponseError
from discord.ext.commands import Cog
from discord_slash.cog_ext import cog_slash
from discord_slash import SlashContext

from arena_bot import ArenaBot
from config import API_URL


class Player(Cog):
    def __init__(self, bot: ArenaBot):
        self.bot = bot
        self._api_url = f"http://{API_URL}"

    @cog_slash(name="join", description="Register Your Account.")
    async def join(self, ctx: SlashContext) -> None:
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


def setup(bot: ArenaBot) -> None:
    bot.add_cog(Player(bot))


def teardown(bot: ArenaBot) -> None:
    bot.remove_cog('Player')
