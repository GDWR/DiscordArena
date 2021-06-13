from discord.ext.commands import Cog, Context, command

from arena_bot import ArenaBot
from models import Item


class Chest(Cog):
    """Cog holds Core commands"""

    def __init__(self, bot: ArenaBot):
        self.bot = bot

    @command()
    async def open(self, ctx: Context, chest_id: str) -> None:
        """Open a chest."""
        item = await Item.objects.get(id=chest_id)
        await ctx.reply(await item.embed)

def setup(bot: ArenaBot) -> None:
    """Add the cog to the bot"""
    bot.add_cog(Chest(bot))


def teardown(bot: ArenaBot) -> None:
    """Remove the cog cleanly"""
    bot.remove_cog('Chest')
