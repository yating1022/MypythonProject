from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5 import uic
class Factorization(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('./ui/fact.ui', self)
        self.ui.pushButton.setText('输入因式分解的数字点我')
        self.ui.pushButton.clicked.connect(self.factorize)
    def factorize(self):
        self.list= []
        num = int(self.ui.lineEdit.text())
        self.fact_do(num)
        resu = '*'.join(map(str,self.list))
        if num == eval(resu):
            self.ui.textEdit.setText(str(num) + '=' + resu)
    def fact_do(self,num):
        for x in range(2,int(num**0.5)+1):
            if num % x == 0:
                self.list.append(x)
                self.fact_do(num/x)
                break
        else:
            self.list.append(num)
# app = QApplication([])
# windows = Factorization()
# windows.show()
# app.exec_()