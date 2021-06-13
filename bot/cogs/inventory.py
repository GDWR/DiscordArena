from discord import Embed
from discord.ext.commands import Cog, command, Context

from arena_bot import ArenaBot
from models import Item


class Inventory(Cog):
    """Cog holds Inventory commands to filter and/or view items in the game."""
    def __init__(self, bot: ArenaBot):
        self.bot = bot

    @command()
    async def inventory(self, ctx: Context) -> None:
        """Display the inventory of the author."""
        items = await Item.objects.filter(owner_id=ctx.author.id).all()

        embed = Embed(title="Items", colour=ctx.author.colour)
        for item in items:
            embed.add_field(**item.embed_field)

        await ctx.reply(embed=embed)


def setup(bot: ArenaBot) -> None:
    """Add the cog to the bot"""
    bot.add_cog(Inventory(bot))


def teardown(bot: ArenaBot) -> None:
    """Remove the cog cleanly"""
    bot.remove_cog('Inventory')
