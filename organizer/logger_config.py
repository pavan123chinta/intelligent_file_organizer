import logging
import os
from datetime import datetime


def setup_logger():
    """
    Configures and returns a logger instance.
    Creates a logs directory if it does not exist.
    Generates a timestamped log file.
    """

    log_dir = "logs"

    # Create logs directory if it doesn't exist
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Create log filename with timestamp
    log_filename = datetime.now().strftime(f"{log_dir}/organizer_%Y%m%d_%H%M%S.log")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.FileHandler(log_filename),
            logging.StreamHandler()
        ]
    )

    return logging.getLogger(__name__)
