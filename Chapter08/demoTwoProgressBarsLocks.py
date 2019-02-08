# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoTwoProgressBarsLocks.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(395, 101)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.progressBar1 = QtWidgets.QProgressBar(Dialog)
        self.progressBar1.setProperty("value", 24)
        self.progressBar1.setTextVisible(True)
        self.progressBar1.setObjectName("progressBar1")
        self.verticalLayout.addWidget(self.progressBar1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.progressBar2 = QtWidgets.QProgressBar(Dialog)
        self.progressBar2.setProperty("value", 24)
        self.progressBar2.setObjectName("progressBar2")
        self.verticalLayout.addWidget(self.progressBar2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Downloading the file"))
        self.label_2.setText(_translate("Dialog", "Scanning for Virus"))

