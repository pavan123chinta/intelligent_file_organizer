from organizer.logger_config import setup_logger
from organizer.utils import load_config


def main():
    logger = setup_logger()

    logger.info("Intelligent File Organizer Application Started")

    try:
        categories = load_config()
        logger.info(f"Loaded categories: {list(categories.keys())}")

    except Exception as e:
        logger.error(f"Error loading configuration: {e}")


if __name__ == "__main__":
    main()
