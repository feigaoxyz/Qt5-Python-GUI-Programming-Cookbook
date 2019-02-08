import sys
import threading
import time

from PySide2.QtWidgets import QApplication, QDialog

from demoProgressBarThread import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.progressBar.setValue(0)
        self.show()


class MyThread(threading.Thread):
    def __init__(self, window):
        threading.Thread.__init__(self)
        self.form = window
        self.counter = 0

    def run(self):
        print("Starting " + self.name)
        while self.counter <= 100:
            time.sleep(1)
            self.form.ui.progressBar.setValue(self.counter)
            self.counter += 10
        print("Exiting " + self.name)


def main():
    app = QApplication(sys.argv)
    window = MyForm()
    thread1 = MyThread(window)
    thread1.start()
    window.exec()
    # thread1.join()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
