import contextlib
from typing import Optional
import logging

def configure_logging(log_file: str) -> Optional[logging.Logger]:
    """Configure the logger and return the logger instance."""
    logger = logging.getLogger('function_logger')
    logger.setLevel(logging.INFO)

    with contextlib.closing(logging.FileHandler(log_file)) as file_handler:
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger

    # If the context manager exits due to an exception, the file handler
    # will be closed automatically, and the logger will not be returned.
    return None