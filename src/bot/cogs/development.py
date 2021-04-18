import random

from discord import Embed, Member
from discord.ext.commands import Cog
from discord_slash.cog_ext import cog_slash
from discord_slash import SlashContext
from discord_slash.utils.manage_commands import create_option

from arena_bot import ArenaBot
from config import API_URL
from constants.options import rarity_choices
from models.rarity import Rarity


class Development(Cog):
    """Cog that holds development tools, this isn't loaded in Production."""
    def __init__(self, bot: ArenaBot):
        self.bot = bot

    @cog_slash(
        name="make",
        guild_ids=[566407576686952480],
        description="Development: Make Item",
        options=[
            create_option(
                name="name",
                description="Name of the item",
                required=True,
                option_type=3
            ),
            create_option(
                name="value",
                description="Value of the item",
                required=True,
                option_type=4,
            ),
            create_option(
                name="rarity",
                description="Rarity of the item",
                required=True,
                option_type=3,
                choices=rarity_choices
            ),
            create_option(
                name="owner",
                description="Owner of the item",
                option_type=6,
                required=True
            ),
        ]
    )
    async def make_item(self, ctx: SlashContext, name: str, value: int, rarity: str, owner: Member) -> None:
        """Make a single item with full control over its fields"""
        rarity = Rarity[rarity]
        item_data = {
            "name": name,
            "owner_id": owner.id,
            "value": value,
            "rarity": rarity.value
        }
        async with self.bot.session.post(f"{API_URL}/item", json=item_data) as response:
            response.raise_for_status()
            data = await response.json()
            item_id = data.get("id")

        embed = Embed(title=name, colour=rarity.colour)
        embed.add_field(name="Item ID", value=str(item_id))
        embed.add_field(name="Value", value=str(value))
        embed.set_author(name=owner.display_name, icon_url=owner.avatar_url)

        await ctx.send(embed=embed)

    @cog_slash(
        name="make_random",
        guild_ids=[566407576686952480],
        description="Development: Make a Random Item",
        options=[
            create_option(
                name="owner",
                description="Owner of the item",
                option_type=6,
                required=True
            ),
            create_option(
                name="amount",
                description="How many to make",
                option_type=3,
                required=True
            )
        ]
    )
    async def make_random_item(self, ctx: SlashContext, owner: Member, amount: int) -> None:
        """Make random items for a member"""
        for _ in range(int(amount)):
            name = "Test Item"
            value = random.randint(1, 1000)
            rarity = random.choice(list(Rarity))

            item_data = {
                "name": name,
                "owner_id": owner.id,
                "value": value,
                "rarity": rarity.value
            }
            async with self.bot.session.post(f"{API_URL}/item", json=item_data) as response:
                response.raise_for_status()
                data = await response.json()
                item_id = data.get("id")

            embed = Embed(title=name, colour=rarity.colour)
            embed.add_field(name="Item ID", value=str(item_id))
            embed.add_field(name="Value", value=str(value))
            embed.set_author(name=owner.display_name, icon_url=owner.avatar_url)


def setup(bot: ArenaBot) -> None:
    """Add the cog"""
    bot.add_cog(Development(bot))


def teardown(bot: ArenaBot) -> None:
    """Remove the cog"""
    bot.remove_cog('Development')
