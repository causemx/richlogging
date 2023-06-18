import logging
from richlogging import Logger, ColorMapping

# Usage 1: Using basic logging

dev_logger: logging.Logger = logging.getLogger(name='dev')
dev_logger.setLevel(logging.DEBUG)

dev_logger.debug('debug message')
dev_logger.info('info message')
dev_logger.warning('warning message')
dev_logger.error('error message')
dev_logger.critical('critical message')

# Usage 1: No config logger, using basic color mapping.
l1 = Logger("foo1")
l1.logger.debug("debug message")
l1.logger.info("info message")
l1.logger.warning("warning message")
l1.logger.error("error message")
l1.logger.critical("critical message")

# Usage 2: No config logger, using basic color mapping.
class MyColorMap(ColorMapping):
    DEBUG = "\x1b[38;5;255m"
    INFO = "\x1b[38;5;252m"
    WARNING = "\x1b[38;5;248m"
    ERROR = "\x1b[38;5;244m"
    CRITICAL = "\x1b[38;5;232m"

l2 = Logger("foo2", MyColorMap())
l2.logger.debug("debug message")
l2.logger.info("info message")
l2.logger.warning("warning message")
l2.logger.error("error message")
l2.logger.critical("critical message")
