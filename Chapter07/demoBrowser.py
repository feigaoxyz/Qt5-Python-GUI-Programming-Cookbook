# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demobrowser.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWebEngineWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEditURL = QtWidgets.QLineEdit(Dialog)
        self.lineEditURL.setObjectName("lineEditURL")
        self.horizontalLayout.addWidget(self.lineEditURL)
        self.pushButtonGo = QtWidgets.QPushButton(Dialog)
        self.pushButtonGo.setObjectName("pushButtonGo")
        self.horizontalLayout.addWidget(self.pushButtonGo)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.widget = QtWebEngineWidgets.QWebEngineView(Dialog)
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter URL:"))
        self.pushButtonGo.setText(_translate("Dialog", "Go"))
