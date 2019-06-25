from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        title = "Py QT5 Button"
        left = 500
        top =200
        width =300
        height =250
        iconName = "kali.jpg"

        self.setWindowTitle(title
        )
        self.setWindowIcon(QtGui.QIcon(iconName))
        self.setGeometry(left,top, width, height)

        self.UiComponents()

        self.show()

    def UiComponents(self):
        button = QPushButton("Click", self)
        #button.setGeometry(QRect(100,100, 111.28))
        button.setIcon(QtGui.QIcon("kali.jpg"))
        button.setIconSize(QtCore.QSize(40,40))
        button.setToolTip("This is a Button")

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())


