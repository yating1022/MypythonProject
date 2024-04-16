import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel,QWidget,QVBoxLayout
from PyQt5 import uic
from redbadui import *
from caipiao import *
from user import *
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('./ui/main.ui', self)
        self.ui.redbadbutton.triggered.connect(self.showWidget1)
        self.ui.caipiaobutton.triggered.connect(self.showWidget2)
        self.ui.user.triggered.connect(self.showWidget3)
    def showWidget1(self):
        self.redbad_widget = redbad()
        # 清除现有的中央部件
        self.centralWidget().deleteLater()
        # 创建并显示控件1
        # 创建并显示redbad界面
        layout = QVBoxLayout()
        layout.addWidget(self.redbad_widget)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    def showWidget2(self):
        self.caipiao_widget = Caipiao()#创建彩票窗口
        self.centralWidget().deleteLater()
        layout = QVBoxLayout()
        layout.addWidget(self.caipiao_widget)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    def showWidget3(self):
        self.user_widget = User()#
        self.centralWidget().deleteLater()
        layout = QVBoxLayout()
        layout.addWidget(self.user_widget)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
app = QApplication([])
stats = MainWindow()
stats.ui.show()
app.exec_()