from typing import Optional

from fastapi import APIRouter
from fastapi_pagination import Page
from fastapi_pagination.ext.orm import paginate
from models import Item, ItemTable

router = APIRouter()


@router.get("/item/{id}", response_model=Item)
async def get_item(id: int) -> Item:
    """Returns a item based on its id"""
    retrieved_item = await ItemTable.objects.get(id=id)
    return Item(**dict(retrieved_item))


@router.get("/item", response_model=Page[Item])
async def get_items(
    owner_id: Optional[int] = None, 
    rarity: Optional[int] = None
):
    """Gets items based on query parameters"""
    items_queryset = ItemTable.objects
    if owner_id:
        items_queryset = items_queryset.filter(
            owner_id=int(owner_id),
        )
    if rarity:
        items_queryset = items_queryset.filter(
            rarity = int(rarity),
        )
    page = await paginate(items_queryset)
    return page
