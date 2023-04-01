import inspect
import logging
import os


class CustomLogger:
    def customLogger(logLevel=logging.INFO):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)

        # create file handler
        log_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utilities', 'logs', 'mylog.log'))
        logs_dir = os.path.dirname(log_file)
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)
        fileHandler = logging.FileHandler(log_file)

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s : %(message)s')

        # add formatter to file handler
        fileHandler.setFormatter(formatter)

        # add file handler to logger
        logger.addHandler(fileHandler)
        return logger
