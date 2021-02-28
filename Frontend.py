import sys

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from YUI import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(635, 435)
        self.generalLayout = QVBoxLayout()
        
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        
        # Create the display and the buttons
        self._createDisplay()
        #self._createButtons()

    def _createDisplay(self):

        self.display = QLineEdit()

        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)

        self.generalLayout.addWidget(self.display)

    def setDisplayText(self, text):
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        return self.display.text()

    def clearDisplay(self):
        self.setDisplayText('')

def main():
    YUI = QApplication(sys.argv)

    view = Window()
    view.setWindowTitle("Yui-MHCP001")
    view.setWindowIcon(QtGui.QIcon("yui.ico"))
    view.show()

    sys.exit(YUI.exec_())

if __name__ == '__main__':
    main()
