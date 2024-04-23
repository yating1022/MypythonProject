"""
mainUi - 

Author: leting130
Date: 2024/4/22
github:https://github.com/yating1022
"""
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout
from experiment06.view.timetextUi import *
from experiment06.view.An02sysui import *
from experiment06.view.configeditui import *
from experiment06.view.testmd5ui import *
from experiment06.view.isRegisterui import *
class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('./ui/main.ui',self)
        self.ui.action1.triggered.connect(self.windows1)
        self.ui.action2.triggered.connect(self.windows2)
        self.ui.action3.triggered.connect(self.windows3)
        self.ui.action4.triggered.connect(self.windows4)
        self.ui.action5.triggered.connect(self.windows5)
    def windows1(self):
        self.windows1 = timetextui()
        self.centralWidget().deleteLater()
        layout = QVBoxLayout()
        layout.addWidget(self.windows1)
        self.setCentralWidget(self.windows1)
    def windows2(self):
        self.windows2 = An02sysui()
        self.centralWidget().deleteLater()
        layout = QVBoxLayout()
        layout.addWidget(self.windows2)
        self.setCentralWidget(self.windows2)
    def windows3(self):
        self.windows3 = testmd5()
        self.centralWidget().deleteLater()
        layout = QVBoxLayout()
        layout.addWidget(self.windows3)
        self.setCentralWidget(self.windows3)
    def windows4(self):
        self.windows4 = Configeditui()
        self.centralWidget().deleteLater()
        layout = QVBoxLayout()
        layout.addWidget(self.windows4)
        self.setCentralWidget(self.windows4)
    def windows5(self):
        self.windows5 = RegisterUI()
        self.centralWidget().deleteLater()
        layout = QVBoxLayout()
        layout.addWidget(self.windows5)
        self.setCentralWidget(self.windows5)


app = QApplication([])
window = Ui_MainWindow()
window.show()
app.exec_()