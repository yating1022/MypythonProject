"""
testmd5ui - 

Author: leting130
Date: 2024/4/23
github:https://github.com/yating1022
"""
import hashlib

from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5 import uic
class testmd5(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('./ui/testmd5ui.ui',self)
        self.ui.pushButton.clicked.connect(self.md5update)
    def md5update(self):
        text = self.ui.textEdit.toPlainText()
        text_passwds = []
        size = int(self.ui.lineEdit.text())
        hash = hashlib.md5()
        for row in self.qiepian(size, text.encode('utf-8')):
            hash.update(row)
            text_passwd = hash.hexdigest()
            text_passwds.append(text_passwd)
        self.ui.listWidget.clear()
        for x in text_passwds:
            self.ui.listWidget.addItem(x)
    def qiepian(self,size, text):
        start = 0
        while start < len(text):
            qie = text[start:start + size]
            yield qie
            start = start + size
        return
# app = QApplication([])
# windows = testmd5()
# windows.show()
# app.exec_()