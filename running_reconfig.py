import time
import logging
import logging.config

logger = logging.getLogger("main")
logger.setLevel(logging.DEBUG)

standard_formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(standard_formatter)
logger.addHandler(console_handler)

file_handler = logging.FileHandler('logging.txt')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(standard_formatter)
logger.addHandler(file_handler)

listener = logging.config.listen(9000)
listener.start()

for index in range(100):
    logger.debug(f'Shows in the logging file {index}')
    logger.info(f'Shows on the console and in the logging file {index}')
    time.sleep(1)

logging.config.stopListening()
listener.join()
