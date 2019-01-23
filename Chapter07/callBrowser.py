import sys
from demoBrowser import Ui_Dialog
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QDialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButtonGo.clicked.connect(self.display_site)
        self.show()

    def display_site(self):
        self.ui.widget.load(QUrl(self.ui.lineEditURL.text()))


def main():
    app = QApplication(sys.argv)
    _ = MyForm()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
