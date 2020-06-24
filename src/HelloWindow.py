from PyQt5 import QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QGridLayout, QLabel, QLineEdit

from utils import my_print


class HelloWindow(QMainWindow):
    def __init__(self, title='progName', h=1024, w=765):
        QMainWindow.__init__(self)
        # custom print
        self.p = my_print
        # textbox
        self.tb1 = QLineEdit(self)
        strWelcome: str = "Hello, how are you today ?"
        self.setMinimumSize(QSize(h, w))
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon('assets/vr-gaming.png'))

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        gridLayout = QGridLayout(self)
        centralWidget.setLayout(gridLayout)

        label = QLabel(strWelcome, self)
        label.setAlignment(QtCore.Qt.AlignCenter)
        gridLayout.addWidget(label, 0, 0)

        self.home()

    def home(self):
        btn = QPushButton("Quit", self)
        btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn.resize(50, 50)
        btn.move(100, 100)

        btn2 = QPushButton("Hello", self)
        btn2.clicked.connect(self.say_hello)
        btn.resize(50, 50)
        btn2.move(200, 100)

        self.tb1.move(20, 20)
        self.tb1.resize(280, 40)
        self.tb1.hide()

        self.show()

    def say_hello(self):
        self.p.ok("Button clicked, Hello!")
        self.tb1.show()
