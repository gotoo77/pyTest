import logging
import logging.config


def debug():
    return "debug"


def info():
    return "info"


def warning():
    return "warning"


def error():
    return "error"


def critical():
    return "critical"


def fatal():
    return "fatal"


def val_to_lvl(argument):
    switcher = {
        logging.DEBUG: debug,
        logging.INFO: info,
        logging.WARNING: warning,
        logging.ERROR: error,
        logging.CRITICAL: critical,
        logging.FATAL: fatal,
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "Invalid logging level")
    # Execute the function
    print(func())


class myLog:

    def __init__(self, my_cfg_path, name):
        self.my_cfg_path = my_cfg_path
        # setup logger with this config
        logging.config.fileConfig(my_cfg_path)
        # create logger
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        # create console handler and set level to debug
        self.ch = logging.StreamHandler()
        self.ch.setLevel(logging.DEBUG)
        # create formatter
        self.formatter = logging.Formatter('%(asctime)s | %(name)s [%(levelname)s] > %(message)s')
        # add formatter to ch
        self.ch.setFormatter(self.formatter)
        # add ch to logger
        self.logger.addHandler(self.ch)

    def set_level(self, lvl=logging.DEBUG):
        if val_to_lvl("e"):
            self.logger.setLevel(lvl)
        else:
            print("error trying to set level : invalid log level")

    def d(self, msg):
        self.logger.debug(msg)

    def i(self, msg):
        self.logger.info(msg)

    def w(self, msg):
        self.logger.warning(msg)

    def e(self, msg):
        self.logger.error(msg)

    def c(self, msg):
        self.logger.critical(msg)
