from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine

Base = declarative_base()

engine = create_async_engine(
    "postgresql+asyncpg://postgres:postgres@localhost/postgres"
)


async def create_all_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
