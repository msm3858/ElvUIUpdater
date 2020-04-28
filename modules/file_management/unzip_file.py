import os
import zipfile
from modules.logger import logger


class UnZipFile:
    def __init__(self, zip_path, current_version, extracted_dir_name, static_directory_path):
        self._zip_path = zip_path
        self._current_version = current_version
        self._directory_to_extract_to = os.path.join(static_directory_path, extracted_dir_name)

    @property
    def extracted_directory(self):
        return self._directory_to_extract_to

    @property
    def elvui_version(self):
        return self._current_version

    def unzip(self):
        logger.info(f"Unzipping version: {self._current_version}... [FROM: {self._zip_path} TO: {self._directory_to_extract_to}]")
        if not os.path.exists(self._directory_to_extract_to):
            os.mkdir(self._directory_to_extract_to)
        with zipfile.ZipFile(self._zip_path, 'r') as zip_ref:
            zip_ref.extractall(self._directory_to_extract_to)