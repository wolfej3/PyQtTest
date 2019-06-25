import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtGui

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Window Test"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300

        self.InitWindow()


    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("kali.jpg"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.show()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())