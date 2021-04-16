from .constants import environment

from .arena_bot import ArenaBot

def main() -> None:
    bot = ArenaBot.create()
    bot.run(environment.TOKEN)

if __name__ == "__main__":
    main()
