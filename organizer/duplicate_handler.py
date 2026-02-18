import os
import hashlib
import shutil


class DuplicateHandler:

    def __init__(self, base_path, logger, dry_run=False, remove_duplicates=False):
        self.base_path = base_path
        self.logger = logger
        self.dry_run = dry_run
        self.remove_duplicates = remove_duplicates
        self.duplicates_found = 0
        self.duplicates_moved = 0

    def get_file_hash(self, file_path):
        hash_md5 = hashlib.md5()

        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)

        return hash_md5.hexdigest()

    def find_duplicates(self):
        self.logger.info("Starting duplicate file detection...")

        hashes = {}
        duplicates_folder = os.path.join(self.base_path, "Duplicates")

        for root, dirs, files in os.walk(self.base_path):
            for file in files:

                file_path = os.path.join(root, file)

                # Skip duplicates folder itself
                if "Duplicates" in file_path:
                    continue

                file_hash = self.get_file_hash(file_path)

                if file_hash in hashes:
                    self.duplicates_found += 1
                    original = hashes[file_hash]

                    self.logger.warning(
                        f"Duplicate found: {file_path} (same as {original})"
                    )

                    if self.remove_duplicates:

                        if not os.path.exists(duplicates_folder):
                            os.makedirs(duplicates_folder)

                        destination = os.path.join(
                            duplicates_folder,
                            os.path.basename(file_path)
                        )

                        if self.dry_run:
                            self.logger.info(
                                f"[DRY RUN] Would move duplicate {file_path} to {destination}"
                            )
                        else:
                            shutil.move(file_path, destination)
                            self.duplicates_moved += 1
                            self.logger.info(
                                f"Moved duplicate {file_path} to Duplicates folder"
                            )

                else:
                    hashes[file_hash] = file_path

        self.logger.info(f"Total duplicates found: {self.duplicates_found}")
        self.logger.info(f"Duplicates moved: {self.duplicates_moved}")

        return self.duplicates_found
