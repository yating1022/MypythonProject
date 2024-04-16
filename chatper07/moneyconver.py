from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
from PyQt5 import uic

class CNY_USD(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("./ui/CNY_USD.ui", self)
        self.ui.pushButton.clicked.connect(self.conver)
    def conver(self):
        string = self.ui.lineEdit.text()
        type = string[-3:]
        self.money = 0.00
        if type == 'CNY':
            self.money = float(string[0:-3])
            self.str = str(round(self.money/7.23,2))+" USD"
            self.ui.textEdit.setText(self.str)
        elif type == 'USD':
            self.money = float(string[0:-3])
            self.str = str(round(self.money * 7.23,2))+" CNY"
            self.ui.textEdit.setText(self.str)
        else:
            QMessageBox.about(self.ui, '提示', f'''格式错误''')
# app = QApplication([])
# start = CNY_USD()
# start.show()
# app.exec_()
