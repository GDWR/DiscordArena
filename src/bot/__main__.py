from bot.constants import environment
from discord_slash import SlashCommand

from bot.arena_bot import ArenaBot

def main() -> None:
    bot = ArenaBot.create()
    SlashCommand(bot, sync_commands=True, override_type=True)

    bot.load_extensions()
    bot.run(environment.TOKEN)

if __name__ == "__main__":
    main()
