from discord.ext.commands import Cog, Context, command

from bot.arena_bot import ArenaBot


class Item(Cog):
    """Cog holds Task commands"""

    def __init__(self, bot: ArenaBot):
        self.bot = bot

    @command()
    async def item(self, ctx: Context) -> None:
        """Task group. Sends current task if currently doing one, else send help message."""
        await ctx.reply("Item...")


def setup(bot: ArenaBot) -> None:
    """Add the cog to the bot"""
    bot.add_cog(Item(bot))


def teardown(bot: ArenaBot) -> None:
    """Remove the cog cleanly"""
    bot.remove_cog('Item')
