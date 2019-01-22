# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoFontDialog.ui',
# licensing of 'demoFontDialog.ui' applies.
#
# Created: Tue Jan 22 17:35:49 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(30, 60, 331, 221))
        self.textEdit.setObjectName("textEdit")
        self.pushButtonFont = QtWidgets.QPushButton(Dialog)
        self.pushButtonFont.setGeometry(QtCore.QRect(120, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Avenir")
        font.setPointSize(12)
        self.pushButtonFont.setFont(font)
        self.pushButtonFont.setObjectName("pushButtonFont")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))
        self.pushButtonFont.setText(QtWidgets.QApplication.translate("Dialog", "Change Font", None, -1))

