from datetime import datetime

from fastapi import APIRouter

from ..models import PlayerNew, PlayerOut, PlayerTable, PlayerIn

router = APIRouter()


@router.get("/player/{_id}", response_model=PlayerOut)
async def get_player(_id: int) -> PlayerOut:
    retrieved_players = await PlayerTable.objects.filter(discord_id=_id).all()
    if len(retrieved_players) > 0:
        return PlayerOut(**dict(retrieved_players[0]))


@router.post("/player", response_model=PlayerOut)
async def new_player(player: PlayerNew) -> PlayerOut:
    """Adds a new player to the database and returns it"""
    player_input = PlayerIn(**{
        **player.dict(),
        'join_date': datetime.utcnow()
    })
    added_player = await PlayerTable.objects.create(**player_input.dict())
    return PlayerOut(**dict(added_player))
