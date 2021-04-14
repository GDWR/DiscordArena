import os

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

DATABASE_URL = os.getenv('DATABASE_URL')
engine = create_async_engine(DATABASE_URL)


async def create_all_tables():
    """Creates all SQL tables if they do not already exist in the database"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
