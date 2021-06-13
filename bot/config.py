from os import getenv

from dotenv import load_dotenv

from utils.setting import setting

if getenv("ENVIRONMENT") is None:
    load_dotenv()

TOKEN = setting("TOKEN", required=True)
API_URL = setting("API_URL", "localhost:5432")
COMMAND_PREFIX = setting("COMMAND_PREFIX", "a!")
DATABASE_HOST = setting("DATABASE_HOST", "database")
DATABASE_PORT = setting("DATABASE_PORT", 5432, _type=int)
DATABASE_USER = setting("DATABASE_USER", "postgres")
DATABASE_PASS = setting("DATABASE_PASS", "postgres")

# Tasks
PROFICIENCY_EXP_PER_LEVEL = setting("PROFICIENCY_EXP_PER_LEVEL", 8, _type=int)
TASK_EXP_GAIN_MIN = setting("TASK_EXP_GAIN_MIN", 4, _type=int)
TASK_EXP_GAIN_MAX = setting("TASK_EXP_GAIN_MAX", 16, _type=int)
TASK_BASE_TIME = setting("TASK_BASE_TIME", 120, _type=int)  # Minutes
