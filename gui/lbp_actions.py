from lbp import *
from Extractors import *
from PyQt4 import QtCore, QtGui
import matplotlib.pyplot as plt
import numpy as np
from ActionsGui import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:

    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)

except AttributeError:

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class LBP(QtGui.QFrame, Ui_lbp):
    mainWindow = None
    histograms = []

    # Conecta os botoes do modulo LBP as acoes
    def __init__(self, parent=None):
        super(LBP, self).__init__(parent)
        self.setupUi(self)
        self.fillCombobox()
        self.processPushButton.clicked.connect(self.process)
        self.clearTextPushButton.clicked.connect(self.clearMessages)

    def setMainWindow(self, mainWindow):
        self.mainWindow = mainWindow

    # Recupera os parametros colocados e roda o algoritmo nas imagens de alta e baixa densidade
    def process(self):
        method = self.comboBox.currentText()
        radius = self.radiusSpinBox.value()
        sampling_points = self.npointsSpinBox.value()
        self.messagesPlainTextEdit.setPlainText("Processing, please wait")

        images = []
        images.append(self.mainWindow.high)
        images.append(self.mainWindow.low)
        self.histograms = lbp(images, sampling_points, radius, method)
        self.messagesPlainTextEdit.setPlainText("Success")
        self.mainWindow.lbpResultSubWindows(self.histograms)

    # Preenchimento do combobox com os tipos de metodos disponiveis
    def fillCombobox(self):
        methods = ["default", "ror", "uniform", "nri_uniform", "var"]
        for x in methods:
            self.comboBox.addItem(x)

    def clearMessages(self):
        self.messagesPlainTextEdit.clear()


