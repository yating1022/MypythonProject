from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QHBoxLayout, QTableWidget
from PyQt5 import uic
import random as rd



class Caipiao(QWidget):
    def __init__(self):
        super().__init__()  # 调用父类的 __init__ 方法
        self.ui = uic.loadUi('./ui/caipiao.ui',self)
        self.ui.pushButton.clicked.connect(self.buttondo)
        self.model = QStandardItemModel()
        self.ui.listView.setModel(self.model)

    def buttondo(self):
        num = int(self.ui.lineEdit.text())
        for i in range(1,num+1):
            string = QStandardItem(self.caipiao())
            self.model.appendRow(string)
    def caipiao(self):
        base = rd.sample(range(1, 35), 6)
        r = rd.choice(range(1, 17))
        return str(base) + "--" + str(r)

# app = QApplication([])
# start = Caipiao()
# start.ui.show()
# app.exec_()