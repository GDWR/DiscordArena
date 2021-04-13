import databases
import sqlalchemy

database = databases.Database("postgresql://postgres:postgres@localhost/postgres")
metadata = sqlalchemy.MetaData()

def create_all_tables():
    # Create the database
    import models

    engine = sqlalchemy.create_engine(str(database.url))
    metadata.create_all(engine)

