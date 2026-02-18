import os
from datetime import datetime


class Reporter:
    """
    Generates execution report file with summary details.
    """

    def __init__(self, base_path, total_files, moved_files,
                 created_folders, unknown_files, dry_run):
        self.base_path = base_path
        self.total_files = total_files
        self.moved_files = moved_files
        self.created_folders = created_folders
        self.unknown_files = unknown_files
        self.dry_run = dry_run

    def generate_report(self):
        """
        Creates a timestamped report file inside reports folder.
        """

        # Create reports folder if not exists
        if not os.path.exists("reports"):
            os.makedirs("reports")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_filename = f"reports/report_{timestamp}.txt"

        mode = "DRY RUN" if self.dry_run else "NORMAL"

        with open(report_filename, "w") as report_file:
            report_file.write("Intelligent File Organizer Report\n")
            report_file.write("---------------------------------\n")
            report_file.write(f"Execution Mode      : {mode}\n")
            report_file.write(f"Target Path         : {self.base_path}\n")
            report_file.write("\n")
            report_file.write("Execution Summary\n")
            report_file.write("-----------------\n")
            report_file.write(f"Total files scanned : {self.total_files}\n")
            report_file.write(f"Files moved         : {self.moved_files}\n")
            report_file.write(f"Folders created     : {self.created_folders}\n")
            report_file.write(f"Unknown files       : {self.unknown_files}\n")

        return report_filename
