import sqlalchemy
from bot.config import DATABASE_USER, DATABASE_HOST, DATABASE_PORT, DATABASE_PASS
from databases import Database as db


class Database:
    """
    Database class to contain all functionality.

    This maybe expanded into having a cache system.
    """
    database = db(f"postgresql://{DATABASE_USER}:{DATABASE_PASS}@{DATABASE_HOST}:{DATABASE_PORT}")
    metadata = sqlalchemy.MetaData()
    _engine = sqlalchemy.create_engine(str(database.url))

    async def connect(self) -> None:
        """Connect to the database."""
        print(f"Connecting to database: {self.database.url}")
        await self.database.connect()
        print(f"Connected to database: {self.database.url}")
        self.create_all_tables()

    async def disconnect(self) -> None:
        """Disconnect from the database."""
        await self.database.disconnect()

    def create_all_tables(self) -> None:
        """Create all tables that are subclasses of `orm.Model` if they do not exist"""
        self.metadata.create_all(self._engine)

    def drop_all_tables(self) -> None:
        """Drop all tables"""
        self.metadata.drop_all(self._engine)
