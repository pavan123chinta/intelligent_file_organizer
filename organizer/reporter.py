import os
from datetime import datetime


class Reporter:
    """
    Generates execution report file after processing.
    """

    def __init__(
        self,
        target_path,
        total_files,
        moved_files,
        created_folders,
        unknown_files,
        duplicates_found=0,
        duplicates_moved=0,
        dry_run=False,
    ):
        self.target_path = target_path
        self.total_files = total_files
        self.moved_files = moved_files
        self.created_folders = created_folders
        self.unknown_files = unknown_files
        self.duplicates_found = duplicates_found
        self.duplicates_moved = duplicates_moved
        self.dry_run = dry_run

    def generate_report(self):
        """
        Creates a timestamped report file inside reports/ folder.
        """

        reports_dir = "reports"

        if not os.path.exists(reports_dir):
            os.makedirs(reports_dir)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_filename = f"report_{timestamp}.txt"
        report_path = os.path.join(reports_dir, report_filename)

        with open(report_path, "w", encoding="utf-8") as file:
            file.write("Intelligent File Organizer Report\n")
            file.write("-----------------------------------\n\n")

            file.write(f"Execution Mode : {'DRY RUN' if self.dry_run else 'NORMAL'}\n")
            file.write(f"Target Path    : {self.target_path}\n\n")

            file.write("Execution Summary\n")
            file.write("-----------------\n")
            file.write(f"Total files scanned : {self.total_files}\n")
            file.write(f"Files moved         : {self.moved_files}\n")
            file.write(f"Folders created     : {self.created_folders}\n")
            file.write(f"Unknown files       : {self.unknown_files}\n\n")

            file.write("Duplicate Summary\n")
            file.write("-----------------\n")
            file.write(f"Total duplicates found : {self.duplicates_found}\n")
            file.write(f"Duplicates moved       : {self.duplicates_moved}\n")

        return report_path
