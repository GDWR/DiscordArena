from models import ItemIn, Item, ItemTable
from fastapi import APIRouter

router = APIRouter()


@router.get("/items/{id}", response_model=Item)
async def get_item(id: int) -> Item:
    """Returns a item based on its id"""
    retrieved_item = await ItemTable.objects.get(id=id)
    return Item(**dict(retrieved_item))


@router.post("/items", response_model=Item)
async def new_item(item: ItemIn) -> Item:
    """Adds a new player to the database and returns it"""
    added_item = await ItemTable.objects.create(**item.dict())
    return Item(**dict(added_item))
