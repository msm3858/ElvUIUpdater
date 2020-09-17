import datetime
import os
import zipfile

from modules.logger import logger


class ZipFile:
    def __init__(self, static_directory_path):
        self.old_zip_filename = f"'old_elvui_{datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')}.zip'"
        self._zip_path = os.path.join(static_directory_path, self.old_zip_filename)
        self._compressed_directories = []

    @property
    def compressed_directories(self):
        return self._compressed_directories

    def add_directory_to_be_compressed(self, directory_path):
        self._compressed_directories.append(directory_path)

    def compress(self):
        logger.info(f"Zipping file... [{self.old_zip_filename}]")
        with zipfile.ZipFile(self._zip_path, "w") as zip_file:
            for directory in self._compressed_directories:
                for dirname, subdirs, files in os.walk(directory):
                    zip_file.write(dirname)
                    for filename in files:
                        zip_file.write(os.path.join(dirname, filename))