# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lbp.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_lbp(object):
    def setupUi(self, lbp):
        lbp.setObjectName(_fromUtf8("lbp"))
        lbp.resize(400, 600)
        self.gridLayout_2 = QtGui.QGridLayout(lbp)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.scrollArea = QtGui.QScrollArea(lbp)
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 382, 563))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_3 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.groupBox_3 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.processPushButton = QtGui.QPushButton(self.groupBox_3)
        self.processPushButton.setEnabled(True)
        self.processPushButton.setObjectName(_fromUtf8("processPushButton"))
        self.verticalLayout.addWidget(self.processPushButton)
        self.gridLayout_5.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.messagesPlainTextEdit = QtGui.QPlainTextEdit(self.groupBox)
        self.messagesPlainTextEdit.setReadOnly(True)
        self.messagesPlainTextEdit.setOverwriteMode(True)
        self.messagesPlainTextEdit.setObjectName(_fromUtf8("messagesPlainTextEdit"))
        self.gridLayout_4.addWidget(self.messagesPlainTextEdit, 0, 0, 1, 1)
        self.clearTextPushButton = QtGui.QPushButton(self.groupBox)
        self.clearTextPushButton.setObjectName(_fromUtf8("clearTextPushButton"))
        self.gridLayout_4.addWidget(self.clearTextPushButton, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 2, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_1 = QtGui.QLabel(self.groupBox_2)
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_1)
        self.radiusSpinBox = QtGui.QSpinBox(self.groupBox_2)
        self.radiusSpinBox.setMinimum(1)
        self.radiusSpinBox.setMaximum(50)
        self.radiusSpinBox.setProperty("value", 2)
        self.radiusSpinBox.setObjectName(_fromUtf8("radiusSpinBox"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.radiusSpinBox)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.npointsSpinBox = QtGui.QSpinBox(self.groupBox_2)
        self.npointsSpinBox.setMinimum(1)
        self.npointsSpinBox.setMaximum(100)
        self.npointsSpinBox.setProperty("value", 8)
        self.npointsSpinBox.setObjectName(_fromUtf8("npointsSpinBox"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.npointsSpinBox)
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.comboBox = QtGui.QComboBox(self.groupBox_2)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.comboBox)
        self.gridLayout_6.addLayout(self.formLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 1, 0, 1, 1)
        self.label_title = QtGui.QLabel(lbp)
        self.label_title.setObjectName(_fromUtf8("label_title"))
        self.gridLayout_2.addWidget(self.label_title, 0, 0, 1, 1)

        self.retranslateUi(lbp)
        QtCore.QMetaObject.connectSlotsByName(lbp)

    def retranslateUi(self, lbp):
        lbp.setWindowTitle(_translate("lbp", "Form", None))
        self.groupBox_3.setTitle(_translate("lbp", "Actions", None))
        self.processPushButton.setText(_translate("lbp", "Process", None))
        self.groupBox.setTitle(_translate("lbp", "Messages", None))
        self.clearTextPushButton.setText(_translate("lbp", "Clear messages", None))
        self.groupBox_2.setTitle(_translate("lbp", "Parameters", None))
        self.label_1.setText(_translate("lbp", "Radius", None))
        self.label_2.setText(_translate("lbp", "Number of Points", None))
        self.label_3.setText(_translate("lbp", "Method", None))
        self.label_title.setText(_translate("lbp", "Local Binary Pattern", None))

