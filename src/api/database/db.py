from ..constants import environment
import sqlalchemy
from databases import Database

metadata = sqlalchemy.MetaData()
database = Database(environment.DATABASE_URL)

def create_all_tables() -> None:
    engine = sqlalchemy.create_engine(str(database.url))
    metadata.create_all(engine)
