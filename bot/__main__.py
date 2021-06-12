from config import TOKEN
from arena_bot import ArenaBot

bot = ArenaBot.create()
bot.load_extensions()

bot.run(TOKEN)
