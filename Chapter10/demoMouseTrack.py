# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoMouseTrack.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(395, 289)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMouseTracking(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_move = QtWidgets.QLabel(Dialog)
        self.label_move.setMouseTracking(True)
        self.label_move.setObjectName("label_move")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_move)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setMouseTracking(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_press = QtWidgets.QLabel(Dialog)
        self.label_press.setMouseTracking(True)
        self.label_press.setObjectName("label_press")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_press)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setMouseTracking(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_release = QtWidgets.QLabel(Dialog)
        self.label_release.setMouseTracking(True)
        self.label_release.setObjectName("label_release")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_release)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Mouse move:"))
        self.label_move.setText(_translate("Dialog", "TextLabel"))
        self.label_2.setText(_translate("Dialog", "Mouse click:"))
        self.label_press.setText(_translate("Dialog", "TextLabel"))
        self.label_3.setText(_translate("Dialog", "Mouse release:"))
        self.label_release.setText(_translate("Dialog", "TextLabel"))

