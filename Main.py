from Utils import *
from FirstLevel import FirstLevel
from gui.ActionsGui import MainWindow

from ImageProcessing import *
from PyQt4.QtGui import QApplication
import sys





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()