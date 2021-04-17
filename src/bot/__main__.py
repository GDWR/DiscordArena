from config import TOKEN
from discord_slash import SlashCommand

from arena_bot import ArenaBot

bot = ArenaBot.create()
SlashCommand(bot, sync_commands=True, override_type=True)

bot.load_extensions()
bot.run(TOKEN)
