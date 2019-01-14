import sys

from PyQt5.QtWidgets import QDialog, QApplication

from demoCalendar import *


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.calendarWidget.selectionChanged.connect(self.dispdate)
        self.ui.dateEdit.dateChanged.connect(self.dispcal)
        self.show()

    def dispdate(self):
        # self.ui.dateEdit.setDisplayFormat("MMM d yyyy")
        self.ui.dateEdit.setDate(self.ui.calendarWidget.selectedDate())

    def dispcal(self):
        self.ui.calendarWidget.setSelectedDate(self.ui.dateEdit.date())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
