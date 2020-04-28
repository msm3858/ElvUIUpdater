import os
import shutil

from modules.logger import logger


class ReplaceDirs:
    def __init__(self, blizzard_addons_path, extracted_version_path):
        self._blizzard_addons_path = blizzard_addons_path
        self._extracted_new_version_path = extracted_version_path

    @staticmethod
    def copy_and_overwrite(from_path, to_path):
        logger.info("Working on replacing files.")
        logger.info(f"[FROM: {from_path}, TO: {to_path}")
        if os.path.exists(to_path):
            shutil.rmtree(to_path)
        shutil.copytree(from_path, to_path)

    def replace(self):
        for new_elvui_dir in os.listdir(self._extracted_new_version_path):
            self.copy_and_overwrite(os.path.join(self._extracted_new_version_path, new_elvui_dir), os.path.join(self._blizzard_addons_path, new_elvui_dir))
