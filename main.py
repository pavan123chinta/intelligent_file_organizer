import argparse
import os

from organizer.logger_config import setup_logger
from organizer.utils import load_config
from organizer.file_manager import FileManager
from organizer.duplicate_handler import DuplicateHandler
from organizer.reporter import Reporter


def parse_arguments():
    """
    Parses command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Intelligent File Organizer Tool"
    )

    parser.add_argument(
        "--path",
        type=str,
        required=True,
        help="Path of the folder to organize"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simulate file organization without making changes"
    )

    parser.add_argument(
        "--remove-duplicates",
        action="store_true",
        help="Move duplicate files to Duplicates folder"
    )

    return parser.parse_args()


def main():
    args = parse_arguments()
    logger = setup_logger()

    logger.info("Intelligent File Organizer Application Started")

    target_path = os.path.abspath(args.path)

    if not os.path.exists(target_path):
        logger.error(f"Provided path does not exist: {target_path}")
        return

    if args.dry_run:
        logger.info("Running in DRY RUN mode (no files will be modified)")

    try:
        # Load categories from config.json
        categories = load_config()
        logger.info(f"Loaded categories: {list(categories.keys())}")

        # -------- FILE ORGANIZATION --------
        file_manager = FileManager(
            base_path=target_path,
            categories=categories,
            logger=logger,
            dry_run=args.dry_run
        )

        file_manager.organize_files()

        # -------- DUPLICATE DETECTION --------
        duplicate_handler = DuplicateHandler(
            base_path=target_path,
            logger=logger,
            dry_run=args.dry_run,
            remove_duplicates=args.remove_duplicates
        )

        duplicate_count = duplicate_handler.find_duplicates()

        # -------- REPORT GENERATION --------
        reporter = Reporter(
            target_path=target_path,
            total_files=file_manager.total_files,
            moved_files=file_manager.moved_files,
            created_folders=file_manager.created_folders,
            unknown_files=file_manager.unknown_files,
            dry_run=args.dry_run,
            duplicates_found=duplicate_count
        )

        report_path = reporter.generate_report()
        logger.info(f"Report generated at: {report_path}")

    except Exception as e:
        logger.error(f"Error: {e}")


if __name__ == "__main__":
    main()
