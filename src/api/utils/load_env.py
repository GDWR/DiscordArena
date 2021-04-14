from dotenv import load_dotenv
import os

def load_env_dev() -> None:
    """Loads environment variables if app is being run in the development environment"""
    if os.getenv("ENVIRONMENT") == None:
        load_dotenv()
