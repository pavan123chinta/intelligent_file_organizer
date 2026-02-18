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

    def __init__(self, base_path, categories, logger):
        self.base_path = base_path
        self.categories = categories
        self.logger = logger

    def organize_files(self):
        """
        Organizes files in the base directory according to categories.
        """

        if not os.path.exists(self.base_path):
            self.logger.error(f"Directory '{self.base_path}' does not exist.")
            return

        files = os.listdir(self.base_path)

        if not files:
            self.logger.info("No files found to organize.")
            return

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
                        self.logger.info(f"Created folder: {category_folder}")

                    destination = os.path.join(category_folder, file)

                    shutil.move(file_path, destination)
                    self.logger.info(f"Moved '{file}' to '{category}' folder.")

                    category_found = True
                    break

            if not category_found:
                self.logger.warning(f"No category found for file: {file}")
