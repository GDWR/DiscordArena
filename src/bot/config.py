import os
from dotenv import load_dotenv

from utils import setting


if os.getenv("ENVIRONMENT") is None:
    load_dotenv()

TOKEN = setting("TOKEN", required=True)
API_URL = setting("API_URL", "localhost:5432")
COMMAND_PREFIX = setting("COMMAND_PREFIX", "!")
