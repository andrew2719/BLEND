
import logging
import os
from settings import LOGS

_loggers = {}

def get_custom_logger(file_name):
    global _loggers

    # Check if a logger for the given file name already exists
    if file_name not in _loggers:
        # Create a new logger for the given file name
        logger = logging.getLogger(file_name)
        logger.setLevel(logging.INFO)

        # Create directory for logs if it doesn't exist
        log_directory = LOGS
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        # Create a file handler which logs even debug messages
        file_handler = logging.FileHandler(os.path.join(log_directory, f'{file_name}.log'))
        file_handler.setLevel(logging.INFO)

        # Create a formatter and set it for the handler
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        # Add the file handler to the logger
        logger.addHandler(file_handler)

        # Create and add a stream handler to log to console as well
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        _loggers[file_name] = logger

    return _loggers[file_name]

server_logger = get_custom_logger('server')
client_logger = get_custom_logger('client')


# logger1.info('This will be logged to file1.log')
# logger2.info('This will be logged to file2.log')
