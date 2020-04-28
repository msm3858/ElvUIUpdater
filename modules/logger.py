import logging


def prepare_logger():
    # Create logger with 'elvui_downloader_app'.
    logger_inner = logging.getLogger('elvui_downloader_app')
    logger_inner.setLevel(logging.DEBUG)
    # Create file handler which logs even debug messages.
    file_handler = logging.FileHandler('./replace_elvui.log')
    file_handler.setLevel(logging.DEBUG)
    # Create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger_inner.addHandler(file_handler)
    return logger_inner


logger = prepare_logger()
