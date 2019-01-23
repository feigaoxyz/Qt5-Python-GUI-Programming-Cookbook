import sys
import socket
from PyQt5.QtWidgets import QApplication, QDialog
from threading import Thread
from demoClient import Ui_Dialog


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.textEditMessages = self.ui.textEditMessages
        self.ui.pushButtonSend.clicked.connect(self.dispMessage)
        self.show()

    def dispMessage(self):
        text = self.ui.lineEditMessage.text()
        self.ui.textEditMessages.append("Client: " + self.ui.lineEditMessage.text())
        self.conn.send(text.encode("utf-8"))
        self.ui.lineEditMessage.setText("")


class ClientThread(Thread):
    def __init__(self, window):
        Thread.__init__(self)
        self.window = window

    def run(self):
        TCP_IP = socket.gethostname()
        TCP_PORT = 80
        BUFFER_SIZE = 1024
        self.window.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.window.conn.connect((TCP_IP, TCP_PORT))
        while True:
            data = self.window.conn.recv(BUFFER_SIZE)
            if data:
                window.textEditMessages.append("Server: " + data.decode("utf-8"))
            else:
                break
        self.window.conn.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    client = ClientThread(window)
    client.start()
    window.exec()
    sys.exit(app.exec_())
