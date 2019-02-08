import asyncio
import sys

from PyQt5.QtWidgets import QApplication, QDialog
from quamash import QEventLoop

from demoTwoProgressBarsAsync import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.invokeAsync)
        self.show()

    def invokeAsync(self):
        asyncio.ensure_future(self.updt(0.5, self.ui.progressBar1))
        asyncio.ensure_future(self.updt(1, self.ui.progressBar2))

    @staticmethod
    async def updt(delay, pbar):
        for i in range(0, 101, 10):
            await asyncio.sleep(delay)
            pbar.setValue(i)


def main():
    app = QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    window = MyForm()
    window.exec()

    with loop:
        loop.run_forever()
        loop.close()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
