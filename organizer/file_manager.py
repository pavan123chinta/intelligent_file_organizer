import os
import shutil


class FileManager:
    """
    Handles file organization logic:
    - Scans directory
    - Matches file extensions with categories
    - Creates category folders
    - Moves files
    """

    def __init__(self, base_path, categories, logger, dry_run=False):

        self.base_path = base_path
        self.categories = categories
        self.logger = logger
        self.dry_run = dry_run

        # Execution metrics
        self.total_files = 0
        self.moved_files = 0
        self.created_folders = 0
        self.unknown_files = 0

    def organize_files(self):
        """
        Organizes files in the base directory according to categories.
        """

        # Validate directory
        if not os.path.exists(self.base_path):
            self.logger.error(f"Directory '{self.base_path}' does not exist.")
            return

        files = os.listdir(self.base_path)

        # Count only actual files (not directories)
        self.total_files = len(
            [f for f in files if os.path.isfile(os.path.join(self.base_path, f))]
        )

        if self.total_files == 0:
            self.logger.info("No files found to organize.")
            return

        # Process each file
        for file in files:
            file_path = os.path.join(self.base_path, file)

            # Skip directories
            if os.path.isdir(file_path):
                continue

            file_extension = os.path.splitext(file)[1].lower()
            category_found = False

            for category, extensions in self.categories.items():

                if file_extension in extensions:

                    category_folder = os.path.join(self.base_path, category)

                    # Create category folder if not exists
                    if not os.path.exists(category_folder):
                        os.makedirs(category_folder)
                        self.created_folders += 1
                        self.logger.info(f"Created folder: {category_folder}")

                    destination = os.path.join(category_folder, file)

                    # Dry run mode
                    if self.dry_run:
                        self.logger.info(
                            f"[DRY RUN] Would move '{file}' to '{category}' folder."
                        )
                    else:
                        shutil.move(file_path, destination)
                        self.moved_files += 1
                        self.logger.info(
                            f"Moved '{file}' to '{category}' folder."
                        )

                    category_found = True
                    break

            # If no category matched
            if not category_found:
                self.unknown_files += 1
                self.logger.warning(
                    f"No category found for file: {file}"
                )

        # Execution Summary (runs once after loop)
        self.logger.info("----- Execution Summary -----")
        self.logger.info(f"Total files scanned: {self.total_files}")
        self.logger.info(f"Files moved: {self.moved_files}")
        self.logger.info(f"Folders created: {self.created_folders}")
        self.logger.info(f"Unknown files: {self.unknown_files}")
        self.logger.info("-----------------------------")
