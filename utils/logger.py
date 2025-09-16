from loguru import logger
import sys, os

os.makedirs("logs", exist_ok=True)

logger.remove()
logger.add(sys.stdout, level="INFO")
logger.add("logs/run.log", level="DEBUG", rotation="1 MB", retention="10 files")

log = logger
