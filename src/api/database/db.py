import sqlalchemy
from api.constants import DATABASE_URL
from databases import Database

database = Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()


def create_all_tables():
    engine = sqlalchemy.create_engine(str(database.url))
    metadata.create_all(engine)
