from discord.ext.commands import Cog, group, Context, ExtensionNotFound, ExtensionAlreadyLoaded, NoEntryPointError, \
    ExtensionFailed, ExtensionNotLoaded


class CogManager(Cog):
    """This cog handles loading, unloading and reloading cogs at runtime."""
    def __init__(self, bot):
        self.bot = bot
        self.exceptions = (
            ExtensionNotFound, ExtensionAlreadyLoaded, NoEntryPointError, ExtensionFailed, ExtensionNotLoaded)

    @group()
    async def cog(self, ctx: Context):
        """Command group to house the CogManger commands."""
        await ctx.send("> Please use the following format `!` `cog` `<extension>` '<package>'(Optional)")

    @cog.command()
    async def reload(self, ctx: Context, extension: str) -> None:
        """Reload a cog"""
        try:
            await self.bot.reload_extension(f"cogs.{extension}")
            await ctx.send(f"> 🟢 {extension.capitalize()} Reloaded")
        except self.exceptions as exception:
            await ctx.send(f"> {extension} {exception}")

    @cog.command()
    async def load(self, ctx: Context, extension: str) -> None:
        """Load a cog"""
        try:
            await self.bot.load_extension(f"cogs.{extension}")
            await ctx.send(f"> 🟢 {extension.capitalize()} Loaded")
        except self.exceptions as exception:
            await ctx.send(f"> {extension} {exception}")

    @cog.command()
    async def unload(self, ctx: Context, extension: str) -> None:
        """Unload a cog"""
        try:
            await self.bot.unload_extension(f"cogs.{extension}")
            await ctx.send(f"> 🟢 {extension.capitalize()} Unloaded")
        except self.exceptions as exception:
            await ctx.send(f"> {extension} {exception}")


def setup(bot):
    """Add the Cog"""
    bot.add_cog(CogManager(bot))
