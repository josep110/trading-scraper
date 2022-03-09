import sys, scraper
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class TS_Interface(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'TradeScrape'
        self.left = 10
        self.right = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.urlBox = QLineEdit(self)
        self.urlBox.move(170,210)
        self.urlBox.resize(280,40)

        self.button = QPushButton('Run Scraper', self)
        self.button.setToolTip('runs the scraper')
        self.button.clicked.connect(self.on_click)
        self.button.move(170,260)

        self.show()

    @pyqtSlot()
    def on_click(self):
        url = self.urlBox.text()
        scraper.go(url)