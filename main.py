import logging
import logging.config

logging.config.fileConfig("log.config")
logger = logging.getLogger("main")

for index in range(1000):
    logger.debug(f'Shows in the logging file {index}')
    logger.info(f'Shows on the console and in the logging file {index}')
