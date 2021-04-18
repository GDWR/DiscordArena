from typing import Optional

from fastapi import APIRouter, HTTPException
from fastapi_pagination import Page
from fastapi_pagination.ext.orm import paginate
from models import Item, ItemTable, ItemIn
from orm import NoMatch
from services import RNG
from models import Rarity

from random import choice

router = APIRouter()


@router.get("/item/{id}", response_model=Item)
async def get_item(id: int) -> Item:
    """Returns a item based on its id"""
    try:
        retrieved_item = await ItemTable.objects.get(id=id)
    except NoMatch:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        return Item(**dict(retrieved_item))


@router.get("/item", response_model=Page[Item])
async def get_items(owner_id: Optional[int] = None, rarity: Optional[int] = None):
    """Gets items based on query parameters"""
    items_queryset = ItemTable.objects
    if owner_id:
        items_queryset = items_queryset.filter(
            owner_id=int(owner_id),
        )
    if rarity:
        items_queryset = items_queryset.filter(
            rarity=int(rarity),
        )
    page = await paginate(items_queryset)
    return page


@router.post("/open_chest", response_model=Item)
async def open_chest(owner_id: int, rarity: int):
    rng = RNG(Rarity(rarity))
    result: Rarity = rng.roll()[0]
    weapon: str = choice(["Sword", "Sheild", "Bow", "Staff"])
    item: ItemIn = ItemIn(
        name=weapon, owner_id=owner_id, value=10, rarity=result.value, type=1
    )
    added_item = await ItemTable.objects.create(**item.dict())
    return Item(**dict(added_item))
