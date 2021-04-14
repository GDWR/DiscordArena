import os
from utils import load_env_dev

load_env_dev()

TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise EnvironmentError("Missing Environment Variable: TOKEN")

API_URL = os.getenv("API_URL")
if not API_URL:
    raise EnvironmentError("Missing Environment Variable: API_URL")
