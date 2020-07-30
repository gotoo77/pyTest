from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QPushButton


class Window2(QMainWindow):

    def __init__(self):
        super(Window2, self).__init__()
        self.setGeometry(100, 100, 200, 50)
        self.move(50, 20)
        self.setWindowTitle("PyQt")
        # self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
        # self.home()

    # def home(self):
    #     btn = QPushButton("Quit", self)
    #     btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
    #     btn.resize(100, 100)
    #     btn.move(100, 100)
    #     self.show()
