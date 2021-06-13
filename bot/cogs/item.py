from discord.ext.commands import Cog, Context, command

from arena_bot import ArenaBot
from models import Item as ItemModel


class Item(Cog):
    """Cog holds Task commands"""

    def __init__(self, bot: ArenaBot):
        self.bot = bot

    @command()
    async def item(self, ctx: Context, item_id: str):
        """Task group. Sends current task if currently doing one, else send help message."""
        item = await ItemModel.objects.get(id=item_id)
        await ctx.reply(await item.embed)


def setup(bot: ArenaBot) -> None:
    """Add the cog to the bot"""
    bot.add_cog(Item(bot))


def teardown(bot: ArenaBot) -> None:
    """Remove the cog cleanly"""
    bot.remove_cog('Item')
