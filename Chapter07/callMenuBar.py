import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter
from PyQt5 import QtCore

from demoMenuBar import Ui_MainWindow


class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.pos1 = [0, 0]
        self.pos2 = [0, 0]
        self.toDraw = ""

        self.ui.actionDraw_Circle.triggered.connect(self.drawCircle)
        self.ui.actionDraw_Rectangle.triggered.connect(self.drawRectangle)
        self.ui.actionDraw_Line.triggered.connect(self.drawLine)

        self.ui.actionPage_Setup.triggered.connect(self.pageSetup)
        self.ui.actionSet_Password.triggered.connect(self.setPassword)

        self.ui.actionCut.triggered.connect(self.cutMethod)
        self.ui.actionCopy.triggered.connect(self.copyMethod)
        self.ui.actionPaste.triggered.connect(self.pasteMethod)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.toDraw == "rectangle":
            width = abs(self.pos2[0] - self.pos1[0])
            height = abs(self.pos2[1] - self.pos1[1])
            qp.drawRect(min(self.pos1[0], self.pos2[0]), min(
                self.pos1[1], self.pos2[1]), width, height)
        elif self.toDraw == "line":
            qp.drawLine(self.pos1[0], self.pos1[1], self.pos2[0], self.pos2[1])
        elif self.toDraw == "circle":
            width = self.pos2[0] - self.pos1[0]
            height = self.pos2[1] - self.pos1[1]
            rect = QtCore.QRect(self.pos1[0], self.pos1[1], width, height)
            startAngle = 0
            arcLength = 360 * 16
            qp.drawArc(rect, startAngle, arcLength)
        qp.end()

    def mousePressEvent(self, event):
        if event.buttons() & QtCore.Qt.LeftButton:
            self.pos1[0], self.pos1[1] = event.pos().x(), event.pos().y()

    def mouseReleaseEvent(self, event):
        self.pos2[0], self.pos2[1] = event.pos().x(), event.pos().y()
        self.update()

    def drawCircle(self):
        self.ui.label.setText("")
        self.toDraw = "circle"

    def drawRectangle(self):
        self.ui.label.setText("")
        self.toDraw = "rectangle"

    def drawLine(self):
        self.ui.label.setText("")
        self.toDraw = "line"

    def pageSetup(self):
        self.ui.label.setText("Page Setup")

    def setPassword(self):
        self.ui.label.setText("Set Password")

    def cutMethod(self):
        self.ui.label.setText("Cut")

    def copyMethod(self):
        self.ui.label.setText("Copy")

    def pasteMethod(self):
        self.ui.label.setText("Paste")


def main():
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
