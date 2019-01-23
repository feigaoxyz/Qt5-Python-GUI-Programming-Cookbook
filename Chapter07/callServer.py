import sys, time
import socket
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import QCoreApplication
from threading import Thread
from socketserver import ThreadingMixIn
from demoServer import *

TCP_IP = "0.0.0.0"
TCP_PORT = 80
BUFFER_SIZE = 1024


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
        self.ui.textEditMessages.append("Server: " + self.ui.lineEditMessage.text())
        self.ui.lineEditMessage.setText("")
        for client in self.thread.threads:
            client.conn.send(text.encode("utf-8"))


class ServerThread(Thread):
    def __init__(self, window):
        Thread.__init__(self)
        self.window = window
        self.threads = []
        self.window.thread = self

    def run(self):
        tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcpServer.bind((TCP_IP, TCP_PORT))
        self.threads = []

        tcpServer.listen(4)
        while True:
            (conn, (ip, port)) = tcpServer.accept()
            newthread = ClientThread(ip, port, conn, window)
            newthread.start()
            self.threads.append(newthread)

        for t in self.threads:
            t.join()


class ClientThread(Thread):
    def __init__(self, ip, port, conn, window):
        Thread.__init__(self)
        self.window = window
        self.ip = ip
        self.port = port
        self.conn = conn

    def run(self):
        while True:
            data = self.conn.recv(1024)
            window.textEditMessages.append(
                "Client ({}:{}) : ".format(self.ip, self.port) + data.decode("utf-8")
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    serverThread = ServerThread(window)
    serverThread.start()
    window.exec()
    sys.exit(app.exec_())
