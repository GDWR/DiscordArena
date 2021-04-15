from glob import glob
from pathlib import Path
from constants import environment

from arena_bot import ArenaBot


bot = ArenaBot(command_prefix="!")


for file in map(Path, glob("bot/cogs/*.py")):
    bot.load_extension(f"cogs.{file.stem}")


bot.run(environment.TOKEN)
