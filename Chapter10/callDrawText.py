import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QFont, QPainter
from PyQt5.QtWidgets import QApplication, QDialog

from demoDrawText import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setMouseTracking(True)
        self.ui.pushButton.clicked.connect(self.display_text)

        self.text = self.ui.textEdit.toPlainText()
        self.fontName = self.ui.listWidget.currentItem().text()
        self.fontSize = int(self.ui.comboBox.itemText(self.ui.comboBox.currentIndex()))

    def display_text(self):
        self.text = self.ui.textEdit.toPlainText()
        self.fontName = self.ui.listWidget.currentItem().text()
        self.fontSize = int(self.ui.comboBox.itemText(self.ui.comboBox.currentIndex()))
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setPen(QColor(168, 34, 3))
        qp.setFont(QFont(self.fontName, self.fontSize))
        qp.drawText(event.rect(), Qt.AlignCenter, self.text)
        qp.end()


def main():
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
