from organizer.logger_config import setup_logger
from organizer.utils import load_config
from organizer.file_manager import FileManager


def main():
    logger = setup_logger()

    logger.info("Intelligent File Organizer Application Started")

    try:
        categories = load_config()
        logger.info(f"Loaded categories: {list(categories.keys())}")

        # Temporary test folder
        test_folder = "test_files"

        file_manager = FileManager(test_folder, categories, logger)
        file_manager.organize_files()

    except Exception as e:
        logger.error(f"Error: {e}")


if __name__ == "__main__":
    main()
