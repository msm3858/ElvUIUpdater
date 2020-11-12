from bs4 import BeautifulSoup
import os
import platform
import requests
import sys

from modules.logger import logger


class Downloader:

    def __init__(self, static_directory_path):
        self._client = ''
        self._download_page_url = 'https://www.tukui.org/download.php?ui=elvui'
        self._download_file_link_prefix = 'https://www.tukui.org/downloads/elvui-'
        self._current_page_content = None
        self._version_section_class_content = None
        self._elvui_current_version = None
        self._elvui_download_zip_link = None
        self._zip_file_path = os.path.join(static_directory_path, 'elvui.zip')

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, value):
        self._client = value

    @property
    def download_url(self):
        return self._download_page_url

    @property
    def current_elvui_version(self):
        return self._elvui_current_version

    @property
    def zip_file_path(self):
        return self._zip_file_path

    def _check_os(self):
        os_running = platform.system()
        logger.info(f"Current operating system: {os_running}")
        if os_running == 'Windows':
            self._client = 'win'
        else:
            logger.warning(f"Your system is not tested for this application. [System: {os_running}].")
            self._client = 'other'

    def _get_download_zip_link(self):
        self._elvui_download_zip_link = f'{self._download_file_link_prefix}{self._elvui_current_version}.zip'

    def _get_response(self, url, allow_redirects=None):
        while True:
            try:
                if allow_redirects:
                    return requests.get(url, allow_redirects=allow_redirects)
                else:
                    return requests.get(url, timeout=10)
            except requests.ConnectionError:
                logger.warning("Connection error. Trying again...")
            except requests.exceptions.ReadTimeout:
                logger.warning("Connection timeout error. Trying again...")


    def _get_content_from_page(self, url):
        logger.info(f"Requesting page... [PAGE: {url}")
        response = self._get_response(url)
        if response.status_code != 200:
            logger.error(f"Did not get proper response from server.\n"
                         f"Checked page: {url}. [CODE={response.status_code}]")
            sys.exit(1)
        else:
            self._current_page_content = BeautifulSoup(response.content, features="html.parser")

    def _get_content_download_page(self):
        self._get_content_from_page(self._download_page_url)

    def _get_elvui_current_version(self):
        self._elvui_current_version = self._current_page_content.find('b', {'class': "Premium"}).contents[0]
        logger.info(f"Found version: {self._elvui_current_version}")

    def _download_file(self):
        logger.info(f"Downloading zip file... [FROM: '{self._elvui_download_zip_link}' TO: '{self._zip_file_path}']")
        request = self._get_response(self._elvui_download_zip_link, allow_redirects=True)
        with open(self._zip_file_path, 'wb') as zip_file:
            zip_file.write(request.content)

    def run(self):
        self._check_os()
        self._get_content_download_page()
        self._get_elvui_current_version()
        self._get_download_zip_link()
        self._download_file()