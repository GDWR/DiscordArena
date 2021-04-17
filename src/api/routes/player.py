from api.models import PlayerIn, Player, PlayerTable
from fastapi import APIRouter

router = APIRouter()


@router.get("/player/{id}", response_model=Player)
async def get_player(id: int) -> Player:
    """Returns a player based on its discord id"""
    retrieved_player = await PlayerTable.objects.get(id=id)
    return Player(**dict(retrieved_player))


@router.post("/player", response_model=Player)
async def new_player(player: PlayerIn) -> Player:
    """Adds a new player to the database and returns it"""
    player_to_add = Player(**{**player.dict()})
    added_player = await PlayerTable.objects.create(**player_to_add.dict())
    return Player(**dict(added_player))
