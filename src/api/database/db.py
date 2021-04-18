import sqlalchemy
from config import DATABASE_USERNAME, DATABASE_HOST, DATABASE_DB, DATABASE_PASSWORD
from databases import Database

database = Database(f"postgresql+asyncpg://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_DB}")
metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(str(database.url))


def create_all_tables() -> None:
    metadata.create_all(engine)


def drop_all_tables() -> None:
    metadata.drop_all(engine)
