from discord.ext.commands import Cog, Context, command

from arena_bot import ArenaBot
from models import Player as PlayerModel


class Player(Cog):
    """Cog holds basic `Player` commands such as `join`"""

    def __init__(self, bot: ArenaBot):
        self.bot = bot

    @command()
    async def profile(self, ctx: Context) -> None:
        """Display the profile of the author."""
        player = await PlayerModel.objects.get(id=ctx.author.id)
        await ctx.send(embed=player.embed)


def setup(bot: ArenaBot) -> None:
    """Add the cog to the bot"""
    bot.add_cog(Player(bot))


def teardown(bot: ArenaBot) -> None:
    """Remove the cog cleanly"""
    bot.remove_cog('Player')
