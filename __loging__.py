import logging

class Logger():
    def __init__(self):
        logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w",
                            format="%(asctime)s %(levelname)s %(message)s")
    def debug(self, message):
        logging.debug(message)
    def info(self, message):
        logging.info(message)
    def warning(self, message):
        logging.warning(message)
    def error(self, message):
        logging.error(message)
    def critical(self, message):
        logging.critical(message)
