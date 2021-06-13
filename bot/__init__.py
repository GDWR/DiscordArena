import logging

from config import LOG_LEVEL

logging.basicConfig(
    format="%(asctime)s - %(name)s: %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S",
    level=LOG_LEVEL,
)
