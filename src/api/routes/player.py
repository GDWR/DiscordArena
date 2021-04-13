from datetime import datetime
from fastapi import APIRouter

from models import PlayerDTO, PlayerDB

router = APIRouter()


@router.get("/player/{_id}", response_model=PlayerDTO)
async def get_player(_id: int) -> PlayerDTO:
    player: PlayerDB = await PlayerDB.objects.get(id=_id)

    return PlayerDTO.from_db(player)



@router.post("/player", response_model=PlayerDTO)
async def new_player(display_name: str) -> PlayerDTO:
    player: PlayerDB = await PlayerDB.objects.create(
        display_name=display_name,
        join_date=datetime.utcnow()
    )

    return PlayerDTO.from_db(player)
