from api.models import PlayerIn, PlayerOut, PlayerTable
from fastapi import APIRouter

router = APIRouter()


@router.get("/player/{id}", response_model=PlayerOut)
async def get_player(id: int) -> PlayerOut:
    """Returns a player based on its discord id"""
    retrieved_player = await PlayerTable.objects.get(id=id)
    return PlayerOut(**dict(retrieved_player))


@router.post("/player", response_model=PlayerOut)
async def new_player(player: PlayerIn) -> PlayerOut:
    """Adds a new player to the database and returns it"""
    player_to_add = PlayerOut(**{**player.dict()})
    added_player = await PlayerTable.objects.create(**player_to_add.dict())
    return PlayerOut(**dict(added_player))
