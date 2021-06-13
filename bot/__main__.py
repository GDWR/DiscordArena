from config import TOKEN
from arena_bot import ArenaBot

def main() -> None:
    bot = ArenaBot.create()
    bot.load_extensions()

    bot.run(TOKEN)

if __name__ == "__main__":
    main()
