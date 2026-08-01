import logging
from datetime import datetime
from loguru import logger
import sys, os

class LogGen:
    @staticmethod
    def get_logger(name):
        log_path = "logs"
        os.makedirs(log_path, exist_ok=True)
        ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        log_file = os.path.join(log_path, f"{name}_{ts}.log")
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        logger = logging.getLogger(name)

        if not logger.handlers:
            logger.setLevel(logging.INFO)
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger




# logger.remove()
# logger.add(sys.stdout, level="INFO")
# logger.add("logs/run.log", level="DEBUG", rotation="1 MB", retention="10 files")
#
# log = logger
