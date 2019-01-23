# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoServer.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonSend = QtWidgets.QPushButton(Dialog)
        self.pushButtonSend.setObjectName("pushButtonSend")
        self.gridLayout.addWidget(self.pushButtonSend, 3, 1, 1, 1)
        self.lineEditMessage = QtWidgets.QLineEdit(Dialog)
        self.lineEditMessage.setObjectName("lineEditMessage")
        self.gridLayout.addWidget(self.lineEditMessage, 3, 0, 1, 1)
        self.textEditMessages = QtWidgets.QTextEdit(Dialog)
        self.textEditMessages.setObjectName("textEditMessages")
        self.gridLayout.addWidget(self.textEditMessages, 2, 0, 1, 2)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonSend.setText(_translate("Dialog", "Send"))
        self.label.setText(_translate("Dialog", "Server"))

