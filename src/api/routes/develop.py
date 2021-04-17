from fastapi import APIRouter
from models import Item, ItemIn, ItemTable

router = APIRouter()


@router.post("/item")
async def new_item(item: ItemIn) -> Item:
    """Adds a new player to the database and returns it"""
    added_item = await ItemTable.objects.create(**item.dict())
    return Item(**dict(added_item))
