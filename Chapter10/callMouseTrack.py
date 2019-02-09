import sys

from PyQt5.QtWidgets import QApplication, QDialog

from demoMouseTrack import QtCore, Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.setMouseTracking(True)
        self.ui.setupUi(self)
        self.show()

    def mouseMoveEvent(self, event):
        text = f"x: {event.x()}, y: {event.y()}"
        self.ui.label_move.setText(text)

    def mousePressEvent(self, event):
        if event.buttons() & QtCore.Qt.LeftButton:
            text = f"x: {event.x()}, y: {event.y()}"
            self.ui.label_press.setText(text)

    def mouseReleaseEvent(self, event):
        text = f"x: {event.x()}, y: {event.y()}"
        self.ui.label_release.setText(text)


def main():
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
