from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QPlainTextEdit,QMessageBox

import sys
import random as rd
class redbad():
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.windows = QMainWindow()
        self.windows.setWindowTitle('第一个pyqt界面')
        self.windows.resize(500, 400)
        self.windows.move(200, 200)

        self.textEdit = QPlainTextEdit(self.windows)
        self.textEdit.setPlaceholderText("输入红包个数")
        self.textEdit.move(25, 10)
        self.textEdit.resize(200, 30)

        self.textEdit2 = QPlainTextEdit(self.windows)
        self.textEdit2.setPlaceholderText("输入红包金额")
        self.textEdit2.move(25, 50)
        self.textEdit2.resize(200, 30)

        self.button = QPushButton('确定', self.windows)
        self.button.move(200, 300)
        self.button.clicked.connect(self.buttonOnCile)

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
    def buttonOnCile(self):
        num = int(self.textEdit.toPlainText())
        money = int(self.textEdit2.toPlainText())
        info = self.red_luker_money(num, money)
        QMessageBox.about(self.windows,
                          '结果',
                          f'''红包结果：{info}'''
                          )
start = redbad()
start.windows.show()
sys.exit(start.app.exec_())