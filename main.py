from organizer.reporter import Reporter
import argparse
import os

from organizer.logger_config import setup_logger
from organizer.utils import load_config
from organizer.file_manager import FileManager


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
        help="Simulate file organization without moving files"
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
        logger.info("Running in DRY RUN mode (no files will be moved)")

    try:
        categories = load_config()
        logger.info(f"Loaded categories: {list(categories.keys())}")

        file_manager = FileManager(
            base_path=target_path,
            categories=categories,
            logger=logger,
            dry_run=args.dry_run
        )

        file_manager.organize_files()

        # Generate execution report
        reporter = Reporter(
            target_path,
            file_manager.total_files,
            file_manager.moved_files,
            file_manager.created_folders,
            file_manager.unknown_files,
            args.dry_run
        )

        report_path = reporter.generate_report()
        logger.info(f"Report generated at: {report_path}")


    except Exception as e:
        logger.error(f"Error: {e}")


if __name__ == "__main__":
    main()
