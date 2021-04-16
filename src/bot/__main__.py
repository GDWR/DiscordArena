import discord
from discord.ext import commands

from glob import glob
from pathlib import Path
from constants import environment
from discord_slash import SlashCommand

from arena_bot import ArenaBot

bot = commands.Bot(command_prefix="!")
slash = SlashCommand(bot, sync_commands=True, override_type=True)

for file in map(Path, glob("bot/cogs/*.py")):
    bot.load_extension(f"cogs.{file.stem}")


bot.run(environment.TOKEN)
