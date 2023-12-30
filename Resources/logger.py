import logging
from settings import APP_LOG
def setup_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # File handler
    file_handler = logging.FileHandler(APP_LOG)
    file_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_format)
    logger.addHandler(file_handler)

    # Console handler (optional)
    console_handler = logging.StreamHandler()
    console_format = logging.Formatter('%(levelname)s - %(message)s')
    console_handler.setFormatter(console_format)
    logger.addHandler(console_handler)

    return logger

server_logger = setup_logger('sever_logger')
client_logger = setup_logger('client_logger')