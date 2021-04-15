from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from database import engine
from models import PlayerDTO, PlayerDB

router = APIRouter()


async def get_session() -> sessionmaker:
    """Provides the database session"""
    yield sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession
    )


@router.get("/player/{_id}", response_model=PlayerDTO)
async def get_player(_id: int, session: sessionmaker = Depends(get_session)) -> PlayerDTO:
    async with session() as sess:
        async with sess.begin():
            result = await sess.execute(select(PlayerDB).order_by(PlayerDB.id))
            first = result.scalars().first()

    return PlayerDTO.from_db(first)


@router.post("/player", response_model=PlayerDTO)
async def new_player(id: int, display_name: str, session: sessionmaker = Depends(get_session)) -> PlayerDTO:
    """Adds a new player to the database and returns it"""
    player = PlayerDB(
        id=id,
        display_name=display_name,
        join_date=datetime.utcnow()
    )

    async with session() as sess:
        try:
            async with sess.begin():
                sess.add(player)
        except IntegrityError:
            raise HTTPException(status_code=400, detail="Player already exists.")

    return PlayerDTO.from_db(player)
