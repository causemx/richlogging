from collections.abc import Mapping
import logging
from enum import Enum
from typing import Any


class ColorMapping:
    DEBUG = "\x1b[37m"
    INFO = "\x1b[32m"
    WARNING = "\x1b[33m"
    ERROR = "\x1b[31m"
    CRITICAL = "\x1b[36m"
    RESET = "\x1b[0m"


class CustomFormatter(logging.Formatter):

    def __init__(self, fmt: str | None = None, 
                 datefmt: str | None = None,
                 style : str = "%",
                 validate: bool = True, *,
                 defaults: Mapping[str, Any] | None = None,
                 cmap: ColorMapping) -> None:
        super().__init__(fmt, datefmt, style, validate, defaults=defaults)
        
        _format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
        
        self.FORMATS = {
            # logging.DEBUG: cmap.DEBUG + _format + self.reset,
            logging.DEBUG: cmap.DEBUG + _format,
            logging.INFO: cmap.INFO + _format,
            logging.WARNING: cmap.WARNING + _format,
            logging.ERROR: cmap.ERROR + _format,
            logging.CRITICAL: cmap.CRITICAL + _format
        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)
    
# create logger with 'spam_application'
logger = logging.getLogger("My_app")
logger.setLevel(logging.DEBUG)

# create console handler with a higher log level

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

c = ColorMapping
ch.setFormatter(CustomFormatter(cmap=c))

logger.addHandler(ch)

# Usage

logger.debug("debug message")
logger.info("info message")
logger.warning("warning message")
logger.error("error message")
logger.critical("critical message")