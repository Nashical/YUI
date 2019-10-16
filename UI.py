import sys

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from YUI import *



class ProcessRunnable(QRunnable):
    def __init__(self, target, args):
        QRunnable.__init__(self)
        self.t = target
        self.args = args

    def run(self):
        self.t(*self.args)

    def start(self):
        QThreadPool.globalInstance().start(self)



def run(user_input, log):
    startYUI()
    
    QMetaObject.invokeMethod(log,
                "append", Qt.QueuedConnection, 
                Q_ARG(str, text))



class LogginOutput(QTextEdit):
    def __init__(self, parent=None):
        super(LogginOutput, self).__init__(parent)

        self.setReadOnly(True)
        self.setLineWrapMode(self.NoWrap)
        self.insertPlainText("")

    @pyqtSlot(str)
    def append(self, text):
        self.moveCursor(QTextCursor.End)
        current = self.toPlainText()

        if current == "":
            self.insertPlainText(text)
        else:
            self.insertPlainText("\n" + text)

        sb = self.verticalScrollBar()
        sb.setValue(sb.maximum())



class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        amount_input = QLineEdit()

        box = LogginOutput(self)

        self.startYUI(box, amount_input)
        
        self.top = 0
        self.left = 0
        self.width = 640
        self.height = 480
        self.title = "Yui-MHCP001"
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon("yui.ico"))
        self.setGeometry(self.left, self.top, self.width, self.height)
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        vboxlayout = QVBoxLayout()
        self.show()

    def startYUI(self, box, user_input):
        self.p = ProcessRunnable(target=run, args=(user_input.displayText(), box))
        self.p.start()

        
 
if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
