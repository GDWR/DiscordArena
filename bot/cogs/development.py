from discord.ext.commands import Cog, command, Context

from arena_bot import ArenaBot
from models import ItemFactory


class Development(Cog):
    """
    Cog that holds development tools, this isn't loaded in Production.

    Feel free to add any useful commands that will help with development.
    """

    def __init__(self, bot: ArenaBot):
        self.bot = bot

    @command()
    async def random_item(self, ctx: Context) -> None:
        """Generate a random item for the author."""
        item = await ItemFactory.random(ctx.author.id)
        await ctx.reply(embed=await item.embed)


def setup(bot: ArenaBot) -> None:
    """Add the cog"""
    bot.add_cog(Development(bot))


def teardown(bot: ArenaBot) -> None:
    """Remove the cog"""
    bot.remove_cog('Development')
