import logging
import os

try:
    from config import LOG_LEVEL
except ModuleNotFoundError:
    print("Have you set your PYTHONPATH? Find out how to here https://stackoverflow.com/a/4580278/13859228")

# Set working directory to bot/
os.chdir(os.path.dirname(os.path.abspath(__file__)))

logging.basicConfig(
    format="[%(asctime)s] <%(levelname)s:%(name)s> %(message)s",
    datefmt="%H:%M:%S",
    level=LOG_LEVEL,
)

# Configure Imported loggers
logging.getLogger('discord').setLevel(logging.WARN)
logging.getLogger('asyncio').setLevel(logging.WARN)
