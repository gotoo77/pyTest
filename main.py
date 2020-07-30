import sys
import getopt

from utils import my_print
from src.Dog import Dog
from utils.myLog import myLog
from src.Window import Window
from src.Window2 import Window2
from src.HelloWindow import HelloWindow
from utils.checkConfig import check_config

from PyQt5 import QtWidgets, QtGui

progName = "TestQtPy"
version = "0.1.1"


def do_pouet():
    p.cout("[" + sys._getframe().f_code.co_name + "] | pouet")


def run_GUI_demo_1():
    app = QtWidgets.QApplication(sys.argv)
    wTitle: str = progName + " (version : " + version + ")"
    GUI = HelloWindow(wTitle)
    GUI.show()
    sys.exit(app.exec_())


def run_GUI_demo_2():
    app = QtWidgets.QApplication(sys.argv)
    wTitle: str = progName + "run_GUI_demo_2 (version : " + version + ")"
    GUI = Window()
    GUI.show()
    sys.exit(app.exec_())


def run_GUI_demo_3():
    app = QtWidgets.QApplication(sys.argv)
    wTitle: str = progName + "run_GUI_demo_3 (version : " + version + ")"
    GUI = Window2()
    GUI.show()
    sys.exit(app.exec_())


def do_dog_stuff():
    fido = Dog('Fido')
    buddy = Dog('Buddy')
    fido.add_trick('roll over')
    buddy.add_trick('play dead')
    buddy.add_trick('fart')
    buddy.show_tricks()
    buddy.remove_trick('fart')
    buddy.remove_trick('shoot')
    fido.show_tricks()
    buddy.show_tricks()
    print(fido.remove_trick.__doc__)


def usage():
    print("usage is :")
    print("blablabla")


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "output="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(str(err))  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    output = None
    verbose = False
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-o", "--output"):
            output = a
        else:
            assert False, "unhandled option"


if __name__ == "__main__":

    main()

    p = my_print
    p.cerr("starting " + progName)
    do_pouet()
    my_cfg_path: str = 'config/logging.ini'
    # check the config path givens
    check_config(my_cfg_path)
    # do_dog_stuff()
    log = myLog(my_cfg_path, "my prog name")

    # 'application' code
    log.d('debug message')
    log.i('info message')
    log.w('warn message')
    log.e('error message')
    log.c('critical message')

    run_GUI_demo_1()
    # run_GUI_demo_2()
    # run_GUI_demo_3()
