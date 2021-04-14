import os

from utils.load_env import load_env_dev

load_env_dev()

DATABASE_URL = os.getenv('DATABASE_URL')
if not DATABASE_URL:
    raise EnvironmentError("Missing Environment Variable: DATABASE_URL")
