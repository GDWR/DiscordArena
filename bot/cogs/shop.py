from discord.ext.commands import Cog, Context, group

from arena_bot import ArenaBot


class Shop(Cog):
    """Cog holds Task commands"""

    def __init__(self, bot: ArenaBot):
        self.bot = bot

    @group()
    async def shop(self, ctx: Context):
        """Task group. Sends current task if currently doing one, else send help message."""
        if ctx.invoked_subcommand is None:
            await ctx.reply("Shop help message...")

    @shop.command()
    async def buy(self, ctx: Context):
        """Buy an item."""
        await ctx.reply("Buy...")

    @shop.command()
    async def sell(self, ctx: Context):
        """Sell an item."""
        await ctx.reply("Sell...")


def setup(bot: ArenaBot) -> None:
    """Add the cog to the bot"""
    bot.add_cog(Shop(bot))


def teardown(bot: ArenaBot) -> None:
    """Remove the cog cleanly"""
    bot.remove_cog('Shop')
