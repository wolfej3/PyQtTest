from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Events and Signals"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300

        self.InitWindow()


    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("kali.jpg"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.CreateButton()
        self.CreateButton2()

        self.show()

    def CreateButton(self):
        button = QPushButton("Click to Quit", self)
        button.setGeometry(QRect(100, 100, 125, 28))
        button.setIcon(QtGui.QIcon("CPS.jpg"))
        button.setIconSize(QtCore.QSize(40, 40))
        button.setToolTip("This will close the application")
        button.clicked.connect(self.clickme)

    def CreateButton2(self):
        button = QPushButton("Click to Halt", self)
        button.setGeometry(QRect(200, 200, 120, 28))
        button.setIcon(QtGui.QIcon("kali.jpg"))
        button.setIconSize(QtCore.QSize(40, 40))
        button.setToolTip("This will halt the application")
        button.clicked.connect(self.HardQuit)

    def clickme(self):
        print("System Quiting")
        sys.exit(0)

    def HardQuit(self):
        print("System HALT", file=sys.stderr)
        sys.exit(1)

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
