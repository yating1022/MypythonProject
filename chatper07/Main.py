from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QVBoxLayout
from PyQt5 import uic
from moneyconver import *
from Factorization import *
from caipiao import *
from LogPy import *
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('./ui/main.ui', self)
        self.ui.CNY_USD.triggered.connect(self.widget1)
        self.ui.fact.triggered.connect(self.widget2)
        self.ui.caipiao.triggered.connect(self.widget3)
        self.ui.Logout.triggered.connect(self.widget4)
    def widget1(self):
        self.windows1 = CNY_USD()
        self.centralWidget().deleteLater()
        layout = QVBoxLayout()
        layout.addWidget(self.windows1)
        self.setCentralWidget(self.windows1)
    def widget2(self):
        self.windows2 = Factorization()
        self.centralWidget().deleteLater()
        layout = QVBoxLayout()
        layout.addWidget(self.windows2)
        self.setCentralWidget(self.windows2)
    def widget3(self):
        self.windows3 = Caipiao()#创建彩票窗口
        self.centralWidget().deleteLater()
        layout = QVBoxLayout()
        layout.addWidget(self.windows3)
        self.setCentralWidget(self.windows3)


    def widget4(self):
        self.windows4 = LogPy()
        self.centralWidget().deleteLater()
        layout = QVBoxLayout()
        layout.addWidget(self.windows4)
        self.setCentralWidget(self.windows4)

app = QApplication([])
windows = MainWindow()
windows.ui.show()
app.exec_()