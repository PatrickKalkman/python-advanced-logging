import logging
import logging.config


def main():
    logging.getLogger().setLevel(logging.WARN)

    logger = logging.getLogger("a")
    logger.setLevel(logging.INFO)

    standard_formatter = logging.Formatter(
        '%(asctime)s %(levelname)s %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(standard_formatter)
    logger.addHandler(console_handler)

    for index in range(1000):
        logger.debug(f'logging from a {index}')
        handlerAB()
        handlerABC()


def handlerAB():
    handler_logger_a_b = logging.getLogger("a.b")
    handler_logger_a_b.info("From handler a.b")


def handlerABC():
    handler_logger_a_b_c = logging.getLogger("a.b.c")
    handler_logger_a_b_c.info("From handler a.b.c")


main()
