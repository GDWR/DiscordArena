from discord.ext.commands import Cog, group, ExtensionNotFound, ExtensionAlreadyLoaded, NoEntryPointError, \
    ExtensionFailed, ExtensionNotLoaded


class CogManager(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.exceptions = (
            ExtensionNotFound, ExtensionAlreadyLoaded, NoEntryPointError, ExtensionFailed, ExtensionNotLoaded)

    @group()
    async def cog(self, ctx):
        await ctx.send("> Please use the following format `!` `cog` `<extension>` '<package>'(Optional)")

    @cog.command()
    async def reload(self, ctx, extension: str) -> None:
        try:
            await self.bot.reload_extension(f"cogs.{extension}")
            await ctx.send(f"> 🟢 {extension.capitalize()} Reloaded")
        except self.exceptions as exception:
            await ctx.send(f"> {extension} {exception}")

    @cog.command()
    async def load(self, ctx, extension: str) -> None:
        try:
            await self.bot.load_extension(f"cogs.{extension}")
            await ctx.send(f"> 🟢 {extension.capitalize()} Loaded")
        except self.exceptions as exception:
            await ctx.send(f"> {extension} {exception}")

    @cog.command()
    async def unload(self, ctx, extension: str) -> None:
        try:
            await self.bot.unload_extension(f"cogs.{extension}")
            await ctx.send(f"> 🟢 {extension.capitalize()} Unloaded")
        except self.exceptions as exception:
            await ctx.send(f"> {extension} {exception}")


def setup(bot):
    bot.add_cog(CogManager(bot))
