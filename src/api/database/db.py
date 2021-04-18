import sqlalchemy
from config import DATABASE_USERNAME, DATABASE_HOST, DATABASE_DB, DATABASE_PASSWORD
from databases import Database

database = Database(f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_DB}")
metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(str(database.url))


def create_all_tables() -> None:
    """Create all tables that are subclasses of `orm.Model` if they do not exist"""
    metadata.create_all(engine)


def drop_all_tables() -> None:
    """Drop all tables"""
    metadata.drop_all(engine)
