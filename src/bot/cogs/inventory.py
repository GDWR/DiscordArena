from typing import Optional

from discord import Embed
from discord.ext.commands import Cog
from discord_slash.cog_ext import cog_slash
from discord_slash import SlashContext

from arena_bot import ArenaBot
from config import API_URL
from discord_slash.utils.manage_commands import create_option

from constants.options import rarity_choices
from models.item import Item
from models.rarity import Rarity


class Inventory(Cog):
    """Cog holds Inventory commands to filter and/or view items in the game."""
    def __init__(self, bot: ArenaBot):
        self.bot = bot
        self._api_url = API_URL

    @cog_slash(
        name="inventory",
        description="View your inventory.",
        options=[
            create_option(
                name="page",
                description="Which page to view, beginning from 1",
                option_type=4,
                required=False
            ),
            create_option(
                name="rarity",
                description="Rarity to filter by",
                option_type=3,
                required=False,
                choices=rarity_choices
            )
        ]
    )
    async def inventory(self, ctx: SlashContext, rarity: Optional[str] = None, page: Optional[int] = 1) -> None:
        """
        View a Player inventory.
        with the ability to filter via Rarity and select a different page.
        """
        params = {
            "owner_id": ctx.author.id,
            "page": page - 1,
            "size": 25,
        }

        if rarity:
            params["rarity"] = Rarity[rarity].value

        async with self.bot.session.get(f"{self._api_url}/item", params=params) as response:
            response.raise_for_status()
            data = await response.json()

        items = [Item(**data) for data in data["items"]]

        embed = Embed(title="__**Inventory**__", colour=ctx.author.colour)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        total_pages = data["total"] // params["size"]
        embed.set_footer(text=f"Page {data['page'] + 1}/{total_pages + 1}")
        for item in items:
            embed.add_field(**item.embed_field)
        await ctx.send(embed=embed)

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
        """Get a item from the API using a item_id"""
        async with self.bot.session.get(f"{self._api_url}/item/{item_id}") as response:
            if response.status == 404:
                await ctx.send(f"> Item of ID {item_id} was not found.")
                return
            else:
                data = await response.json()

        await ctx.send(embed=await Item(**data).embed)


def setup(bot: ArenaBot) -> None:
    """Add the cog to the bot"""
    bot.add_cog(Inventory(bot))


def teardown(bot: ArenaBot) -> None:
    """Remove the cog cleanly"""
    bot.remove_cog('Inventory')
