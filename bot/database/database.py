import sqlalchemy
from config import DATABASE_USER, DATABASE_HOST, DATABASE_PORT, DATABASE_PASS
from databases import Database as db
import logging


class Database:
    """
    Database class to contain all functionality.

    This maybe expanded into having a cache system.
    """
    database = db(f"postgresql://{DATABASE_USER}:{DATABASE_PASS}@{DATABASE_HOST}:{DATABASE_PORT}")
    metadata = sqlalchemy.MetaData()
    _engine = sqlalchemy.create_engine(str(database.url))
    logger = logging.getLogger(__name__)

    async def connect(self) -> None:
        """Connect to the database."""
        self.logger.info(f"Connecting to database: {self.database.url}")
        await self.database.connect()
        self.logger.info(f"Connected to database: {self.database.url}")
        self.create_all_tables()

    async def disconnect(self) -> None:
        """Disconnect from the database."""
        await self.database.disconnect()

    def create_all_tables(self) -> None:
        """Create all tables that are subclasses of `orm.Model` if they do not exist"""
        self.metadata.create_all(self._engine)
        self.logger.info("Created all tables.")

    def drop_all_tables(self) -> None:
        """Drop all tables"""
        self.metadata.drop_all(self._engine)
        self.logger.warning("Droped all tables.")
