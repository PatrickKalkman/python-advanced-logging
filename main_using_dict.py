import json
import logging
import logging.config

with open('log_dict.json') as f:
    config_dict = json.load(f)
    logging.config.dictConfig(config_dict)

logger = logging.getLogger("main")

for index in range(1000):
    logger.debug(f'Shows in the logging file {index}')
    logger.info(f'Shows on the console and in the logging file {index}')
