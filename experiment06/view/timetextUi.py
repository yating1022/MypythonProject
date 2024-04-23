"""
timetextUi - 

Author: leting130
Date: 2024/4/22
github:https://github.com/yating1022
"""
from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5 import uic
import time
class timetextui(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("./ui/timetextUi.ui", self)
        self.ui.button.clicked.connect(self.button_clicked)
    def button_clicked(self):
        witch = 50
        start = time.perf_counter()
        for x in range(witch + 1):
            finished = '<font color="green">' + '*' * x + '</font>'
            unfinished = '*' * (witch - x)
            percent = (x / witch) * 100
            runtime = time.perf_counter() - start
            text = "\r{:^3.0f}%[{}->{}]{:.2f}秒".format(percent, finished, unfinished, runtime)
            self.ui.label.setText(text)
            QApplication.processEvents()
            time.sleep(0.1)
# app = QApplication([])
# windows = timetextui()
# windows.show()
# app.exec_()