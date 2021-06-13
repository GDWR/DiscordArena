from discord.ext.commands import Cog, command, Context

from arena_bot import ArenaBot
from models import ItemFactory
from database import Database

class Development(Cog):
    """Cog that holds development tools, this isn't loaded in Production."""

    def __init__(self, bot: ArenaBot):
        self.bot = bot

    @command()
    async def random_item(self, ctx: Context) -> None:
        """Generate a random item for the author."""
        item = await ItemFactory.random(ctx.author.id)
        await ctx.send(embed=await item.embed)

    @command()
    async def reload_tables(self, ctx: Context) -> None:
        """Drop and create all the tables."""
        self.bot.database.drop_all_tables()
        self.bot.database.create_all_tables()
        
    @command()
    async def ping(self, ctx: Context) -> None:
        """Sends the ping in ms."""
        await ctx.send(f"Ping is {round(self.bot.latency * 1000)}ms")

def setup(bot: ArenaBot) -> None:
    """Add the cog"""
    bot.add_cog(Development(bot))


def teardown(bot: ArenaBot) -> None:
    """Remove the cog"""
    bot.remove_cog('Development')
