from bot.config import TOKEN
from bot.arena_bot import ArenaBot

def main() -> None:
    bot = ArenaBot.create()
    bot.load_extensions()

    bot.run(TOKEN)
