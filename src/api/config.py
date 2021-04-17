import os
from dotenv import load_dotenv
from utils import setting

if os.getenv("ENVIRONMENT") is None:
    load_dotenv()


DATABASE_HOST = setting('DATABASE_HOST', "localhost")
DATABASE_PORT = setting('DATABASE_PORT', 5432)
DATABASE_USERNAME = setting('DATABASE_USERNAME', "postgres")
DATABASE_PASSWORD = setting('DATABASE_PASSWORD', "postgres")
DATABASE_DB = setting('DATABASE_DB', "postgres")
