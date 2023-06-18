from richlogging import NewLogger, ColorMapping


class MyColorMap(ColorMapping):
    DEBUG = DEBUG = "\x1b[34m"

m = MyColorMap
s = NewLogger(m)
s.logger.debug("Hi")


