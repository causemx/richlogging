# richlogging
Enriching logging library of python.


## Reqirement
- python >= 3.4

## Installation
```sh
pip3 install richlogging
```

## Usage
- Basic usage
```python
from richlogging import *
_logger = Logger([logger_name])
_logger.logger.debug([message])
_logger.logger.info([message])
_logger.logger.warn([message])
_logger.logger.error([message])
_logger.logger.critical([message])
```
- Output
![Imgur](https://i.imgur.com/AL4dTva.png)

Or you can customized color mapping by overrwriting ColorMapping class.
- ASCI Color code table
![Imgur](https://i.imgur.com/MGGdzJB.png)

Add class below:
```python
class MyColorMap(ColorMapping):
    DEBUG = "\x1b[38;5;255m"
    INFO = "\x1b[38;5;252m"
    WARNING = "\x1b[38;5;248m"
    ERROR = "\x1b[38;5;244m"
    CRITICAL = "\x1b[38;5;232m"
```
- Output
![Imgur](https://i.imgur.com/iv7GdDL.png)