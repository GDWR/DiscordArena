from enum import Enum
from typing import Optional

from aiohttp import ClientResponseError
from discord import Member, Embed, Colour
from discord.ext.commands import Cog
from discord_slash.cog_ext import cog_slash, cog_subcommand
from discord_slash import SlashContext

from arena_bot import ArenaBot
from config import API_URL
from discord_slash.utils.manage_commands import create_option, create_choice


class Rarity(Enum):
    Poor = 1
    Common = 2
    Uncommon = 3
    Rare = 4
    Epic = 5
    Legendary = 6
    Mythical = 7

    @property
    def colour(self) -> Colour:
        if self is Rarity.Poor:
            return Colour.dark_gray()
        elif self is Rarity.Common:
            return Colour.lighter_gray()
        elif self is Rarity.Uncommon:
            return Colour.green()
        elif self is Rarity.Rare:
            return Colour.blue()
        elif self is Rarity.Epic:
            return Colour.purple()
        elif self is Rarity.Legendary:
            return Colour.orange()
        elif self is Rarity.Mythical:
            return Colour.red()


class Inventory(Cog):
    def __init__(self, bot: ArenaBot):
        self.bot = bot
        self._api_url = API_URL

    @cog_slash(
        name="inventory",
        description="View your inventory.",
        options=[
            create_option(
                name="rarity",
                description="Rarity to filter by",
                option_type=3,
                required=False,
                choices=[
                    create_choice(
                        name="Poor",
                        value="Poor"
                    ),
                    create_choice(
                        name="Common",
                        value="Common"
                    ),
                    create_choice(
                        name="Uncommon",
                        value="Uncommon"
                    ),
                    create_choice(
                        name="Rare",
                        value="Rare"
                    ),
                    create_choice(
                        name="Epic",
                        value="Epic"
                    ),
                    create_choice(
                        name="Legendary",
                        value="Legendary"
                    ),
                    create_choice(
                        name="Mythical",
                        value="Mythical"
                    )
                ]
            )
        ]
    )
    async def inventory(self, ctx: SlashContext, rarity: Optional[str] = None) -> None:
        if rarity is None:
            await ctx.send("> Getting all items")
        else:
            await ctx.send(f"> Getting {rarity} items")

    @cog_slash(
        name="item",
        description="Get an item",
        options=[
            create_option(
                name="item_id",
                description="The id of the item to view",
                option_type=4,
                required=True
            ),
        ]
    )
    async def get_item(self, ctx: SlashContext, item_id: int):

        async with self.bot.session.get(f"{self._api_url}/item/{item_id}") as response:
            response.raise_for_status()
            item = await response.json()

        rarity = Rarity(item["rarity"])

        embed = Embed(title=item["name"], colour=rarity.colour)
        embed.add_field(name="Item ID", value=str(item["id"]))
        embed.add_field(name="Value", value=str(item["value"]))

        owner = self.bot.get_user(item["owner_id"])
        if owner is None:
            owner = await self.bot.fetch_user(item["owner_id"])

        embed.set_author(name=owner.display_name, icon_url=owner.avatar_url)
        await ctx.send(embed=embed)


    @cog_slash(
        name="make",
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
                choices=[
                    create_choice(
                        name="Poor",
                        value="Poor"
                    ),
                    create_choice(
                        name="Common",
                        value="Common"
                    ),
                    create_choice(
                        name="Uncommon",
                        value="Uncommon"
                    ),
                    create_choice(
                        name="Rare",
                        value="Rare"
                    ),
                    create_choice(
                        name="Epic",
                        value="Epic"
                    ),
                    create_choice(
                        name="Legendary",
                        value="Legendary"
                    ),
                    create_choice(
                        name="Mythical",
                        value="Mythical"
                    )
                ]
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
        rarity = Rarity[rarity]
        item_data = {
            "name": name,
            "owner_id": owner.id,
            "value": value,
            "rarity": rarity.value
        }
        async with self.bot.session.post(f"{self._api_url}/item", json=item_data) as response:
            response.raise_for_status()
            data = await response.json()
            item_id = data.get("id")


        embed = Embed(title=name, colour=rarity.colour)
        embed.add_field(name="Item ID", value=str(item_id))
        embed.add_field(name="Value", value=str(value))
        embed.set_author(name=owner.display_name, icon_url=owner.avatar_url)

        await ctx.send(embed=embed)


def setup(bot: ArenaBot) -> None:
    bot.add_cog(Inventory(bot))


def teardown(bot: ArenaBot) -> None:
    bot.remove_cog('Inventory')
