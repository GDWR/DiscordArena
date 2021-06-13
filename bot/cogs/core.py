from discord.ext.commands import Cog, Context, command

from arena_bot import ArenaBot
from models import Player


class Core(Cog):
    """Cog holds Core commands"""

    def __init__(self, bot: ArenaBot):
        self.bot = bot

    @command()
    async def join(self, ctx: Context) -> None:
        """Join if not already."""
        if not await Player.objects.filter(id=ctx.author.id).exists():
            await Player.objects.create(id=ctx.author.id)
            # Get back from database to reconstruct object correctly.
            player = await Player.objects.get(id=ctx.author.id)
            await ctx.send(embed=await player.embed)

    @command()
    async def profile(self, ctx: Context) -> None:
        """Display the profile of the author."""
        player = await Player.objects.get(id=ctx.author.id)
        await ctx.send(embed=player.embed)


def setup(bot: ArenaBot) -> None:
    """Add the cog to the bot"""
    bot.add_cog(Core(bot))


def teardown(bot: ArenaBot) -> None:
    """Remove the cog cleanly"""
    bot.remove_cog('Core')
