#! python3
import os
from modules.file_management.zip_file import ZipFile
from modules.file_management.replace_dirs import ReplaceDirs
from modules.file_management.unzip_file import UnZipFile
from modules.downloader import Downloader


from modules.logger import logger
from modules.arg_parser import args


def main():
    static_path = os.path.join(os.getcwd(), 'Static')
    blizzard_addons_directory_path = f'{args.blizz_addon_path}'
    addons = os.listdir(blizzard_addons_directory_path)
    extracted_elvui_directory = os.path.join(static_path, args.extracted_elvui)

    if not os.path.exists(static_path):
        logger.info(f"Creating static path: {static_path}.")
        os.mkdir(static_path)

    # Download handling.
    downloader = Downloader(static_directory_path=static_path)
    downloader.run()

    # Zipping Handling.
    zip_file = UnZipFile(
        zip_path=downloader.zip_file_path,
        current_version=downloader.current_elvui_version,
        extracted_dir_name=args.extracted_elvui,
        static_directory_path=static_path)
    zip_file.unzip()

    # ElvUI addons backuping.
    elvui_addons = list(filter(lambda dir: (str(dir).lower().find('elvui') > -1), addons))
    elvui_directories = list(
        map(lambda elvui_directory: os.path.join(blizzard_addons_directory_path, elvui_directory),
            elvui_addons))
    backup_file_handler = ZipFile(static_directory_path=static_path)
    for elvui_directory in elvui_directories:
        backup_file_handler.add_directory_to_be_compressed(elvui_directory)
    backup_file_handler.compress()

    # ElvUI file replacement.
    replace_handler = ReplaceDirs(
        blizzard_addons_path=args.blizz_addon_path,
        extracted_version_path=f'{extracted_elvui_directory}')
    replace_handler.replace()


if __name__ == '__main__':
    logger.info("Starting program...")
    main()
