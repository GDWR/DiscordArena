from discord.ext.commands import Cog, Context, command
from orm import NoMatch

from arena_bot import ArenaBot
from exceptions import ItemNotFound
from models import Item, ItemFactory, ItemType


class Chest(Cog):
    """Cog holds Core commands"""

    def __init__(self, bot: ArenaBot):
        self.bot = bot

    @command()
    async def open(self, ctx: Context, chest_id: str):
        """Open a chest."""
        chest_id = chest_id.upper()

        try:
            item = await Item.objects.get(item_id=chest_id)
        except NoMatch as err:
            raise ItemNotFound(chest_id) from err

        if item.item_type is not ItemType.Chest:
            return await ctx.reply("> That's not a Chest.")

        await item.delete()
        new_item = await ItemFactory.random(ctx.author.id)
        await ctx.reply(embed=await new_item.embed)


def setup(bot: ArenaBot) -> None:
    """Add the cog to the bot"""
    bot.add_cog(Chest(bot))


def teardown(bot: ArenaBot) -> None:
    """Remove the cog cleanly"""
    bot.remove_cog('Chest')
