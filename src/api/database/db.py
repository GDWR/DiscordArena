from config import DATABASE_HOST, DATABASE_DB, DATABASE_USERNAME, DATABASE_PASSWORD
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_async_engine(
    f"postgresql+asyncpg://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_DB}"
)


async def create_all_tables():
    """Creates all SQL tables if they do not already exist in the database"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
