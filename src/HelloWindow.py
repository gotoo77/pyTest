from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QIntValidator, QFont
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QGridLayout, QLabel, QLineEdit

from utils import my_print


class HelloWindow(QMainWindow):
    def __init__(self, title='progName', h=1024, w=765):
        QMainWindow.__init__(self)
        # custom print
        self.p = my_print

        strWelcome: str = "Hello, how are you today ?"
        self.setMinimumSize(QSize(h, w))
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon('assets/vr-gaming.png'))

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        self.gridLayout = QGridLayout(self)
        self.centralWidget.setLayout(self.gridLayout)

        self.label = QLabel(strWelcome, self)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.label, 0, 0)

        self.btn1 = QPushButton("Quit", self)
        self.btn1.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.btn1.resize(50, 50)
        self.btn1.move(100, 100)
        self.btn1.resize(50, 50)

        self.btn2 = QPushButton("Hello", self)
        self.btn2.clicked.connect(self.say_hello)
        self.btn2.move(200, 100)

        self.btn3 = QPushButton("Show", self)
        self.btn3.clicked.connect(self.showLE)
        self.btn3.move(300, 200)

        self.btn4 = QPushButton("Hide", self)
        self.btn4.clicked.connect(self.hideLE)
        self.btn4.move(300, 240)

        self.e1 = QLineEdit(self)
        self.e1.setValidator(QIntValidator())
        self.e1.setMaxLength(4)
        self.e1.setAlignment(Qt.AlignRight)
        self.e1.setFont(QFont("Arial", 18))
        self.e1.move(400, 210)
        self.e1.resize(100, 30)
        self.e1.hide()
        # btn2.clicked.connect(self.showButtonEvent)

        # show widget
        self.show()

    def showLE(self):
        self.e1.show()

    def hideLE(self):
        self.e1.hide()

    def say_hello(self):
        self.p.cout("Button clicked, Hello!")
