import sys
import threading
import time

from PyQt5.QtWidgets import QApplication, QDialog

from demoTwoProgressBarsLocks import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()


class MyThread(threading.Thread):
    def __init__(self, bar, lock):
        threading.Thread.__init__(self)
        self.bar = bar
        self.counter = 0
        self.lock = lock

    def run(self):
        print("Starting " + self.name)
        self.lock.acquire()
        while self.counter <= 100:
            time.sleep(0.5)
            self.bar.setValue(self.counter)
            self.counter += 10
        self.lock.release()
        print("Exiting " + self.name)


def main():
    app = QApplication(sys.argv)
    window = MyForm()

    lock = threading.Lock()

    thread1 = MyThread(window.ui.progressBar1, lock)
    thread1.start()
    thread2 = MyThread(window.ui.progressBar2, lock)
    thread2.start()

    window.exec()

    thread1.join()
    thread2.join()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
