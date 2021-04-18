from aiohttp import ClientResponseError
from discord import Embed, Colour
from discord.ext.commands import Cog
from discord_slash.cog_ext import cog_slash
from discord_slash import SlashContext

from arena_bot import ArenaBot
from config import API_URL


class Player(Cog):
    """Cog holds basic `Player` commands such as `join`"""

    def __init__(self, bot: ArenaBot):
        self.bot = bot
        self._api_url = API_URL

    @cog_slash(name="join", description="Register Your Account.")
    async def join(self, ctx: SlashContext) -> None:
        """Join the Arena, This will send a request to add the player to the database."""
        data = {
            "id": ctx.author.id,
            "display_name": ctx.author.display_name
        }

        async with self.bot.session.post(f"{self._api_url}/player", json=data) as response:
            try:
                response.raise_for_status()
                data = await response.json()
            except ClientResponseError as e:
                print(e)
                await ctx.send("> An error has occurred.")
                return

        embed = Embed(title="Welcome to the Arena!", colour=Colour.red())
        await ctx.send(embed=embed)


def setup(bot: ArenaBot) -> None:
    """Add the cog to the bot"""
    bot.add_cog(Player(bot))


def teardown(bot: ArenaBot) -> None:
    """Remove the cog cleanly"""
    bot.remove_cog('Player')
