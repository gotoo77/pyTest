# Welcome

import os
import sys

from utils import my_print
from src.Dog import Dog
from utils.myLog import myLog
from src.Window import Window
from src.HelloWindow import HelloWindow

from PyQt5 import QtWidgets

progName = "TestQtPy"
version = "0.1.0"

errors = {0: 'OK',
          1: 'Error in config file'}


def do_something():
    p.ok("[" + sys._getframe().f_code.co_name + "] | pouet")


def check_config(cfg_path):
    if os.path.exists(cfg_path):
        p.ok("[" + sys._getframe().f_code.co_name + "] | OK : found logging config at '" + cfg_path + "'")
    else:
        p.err("[" + sys._getframe().f_code.co_name + "] | Error no logging config found at '" + cfg_path + "' !")
        exit(errors[1])


def run():
    app = QtWidgets.QApplication(sys.argv)
    wTitle: str = progName + " (version : " + version + ")"
    GUI = HelloWindow(wTitle)
    # GUI = Window()
    GUI.show()
    sys.exit(app.exec_())


def do_dog_stuff():
    d = Dog('Fido')
    e = Dog('Buddy')
    d.add_trick('roll over')
    e.add_trick('play dead')
    d.show_tricks()
    e.show_tricks()


if __name__ == "__main__":
    p = my_print
    do_something()
    p.err("Test")

    my_cfg_path: str = 'config/logging.ini'

    # check the config path given
    check_config(my_cfg_path)

    do_dog_stuff()

    log = myLog(my_cfg_path, "my prog name")

    # 'application' code
    log.d('debug message')
    log.i('info message')
    log.w('warn message')
    log.e('error message')
    log.c('critical message')

    # app = QtWidgets.QApplication(sys.argv)
    # mainWin = HelloWindow()
    # mainWin.show()
    #
    # sys.exit(app.exec_())

    run()
