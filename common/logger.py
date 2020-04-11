import logging

LOG_FORMATTER = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

def setup_logger(name, log_file, level=logging.INFO):
    """To setup as many loggers as you want"""

    handler = logging.FileHandler(log_file)        
    handler.setFormatter(LOG_FORMATTER)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

# Set up logger into seperate file: INFO, DEBUG, WARNING/ERROR
# INFO
_info_log = setup_logger('_info_log', 'log\INFO.log')
# DEBUG/WARNING
_debug_log = setup_logger('_debug_log', 'log\DEBUG.log', level=logging.DEBUG)
# ERROR
_error_log = setup_logger('_error_log', 'log\ERROR.log')

