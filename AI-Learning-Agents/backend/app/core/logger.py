import logging
import os
from logging.handlers import RotatingFileHandler


LOG_DIRECTORY = "logs"
LOG_FILE = os.path.join(LOG_DIRECTORY, "app.log")


def setup_logging():

    # Create logs directory if it does not exist
    os.makedirs(LOG_DIRECTORY, exist_ok=True)

    # Get the root logger
    logger = logging.getLogger()

    # Set the minimum logging level
    logger.setLevel(logging.INFO)

    # Prevent duplicate log handlers during FastAPI reload
    if logger.handlers:
        return

    # Configure log format
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | "
        "%(name)s | %(filename)s:%(lineno)d | "
        "%(funcName)s() | %(message)s"
    )

    # Configure file logging with rotation
    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=5 * 1024 * 1024,
        backupCount=3,
        encoding="utf-8",
    )

    file_handler.setFormatter(formatter)

    # Configure console logging
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Add handlers to the root logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)