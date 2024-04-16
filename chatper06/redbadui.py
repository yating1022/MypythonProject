from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox,QWidget
from PyQt5 import uic
import random as rd
class redbad(QWidget):
    def __init__(self):
        super().__init__()  # 调用父类的 __init__ 方法
        self.ui = uic.loadUi('./ui/redbad.ui', self)
        self.ui.button.clicked.connect(self.dored)
        self.model = QStandardItemModel()
        self.ui.listView.setModel(self.model)
    def red_luker_money(self,num, money):
        moneys = []
        total = 0
        for i in range(num):
            while True:
                if i == num - 1:
                    one = round(money - total, 2)
                    break
                else:
                    try:
                        one = round(rd.uniform(0.1, (money - total)), 2)
                        assert 0 <= one <= (3 * money / num)
                        break
                    except:
                        pass
            moneys.append(one)
            total += one
        return moneys
    def dored(self):
        num = int(self.ui.num.text())
        money = int(self.ui.money.text())
        string = self.red_luker_money(num,money)
        self.model.clear()
        for i in string:
            item = QStandardItem(str(i))
            self.model.appendRow(item)
# app = QApplication([])
# stats = redbad()
# stats.ui.show()
# app.exec_()