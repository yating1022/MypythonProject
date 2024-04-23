"""
isRegisterui.py - 

Author: leting130
Date: 2024/4/23
github:https://github.com/yating1022
"""
import json
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5 import uic
class RegisterUI(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('./ui/isRegister.ui', self)
        self.ui.pushButton.clicked.connect(self.run)
    def run(self):
        with open("./user_json.json", 'r', encoding="utf-8") as f:
            user_data = json.load(f)
            while True:
                user = self.ui.userEdit.text()
                if user in user_data:
                    QMessageBox.about(self.ui, '提示', f'''账户已存在''')
                    self.ui.userEdit.clear()
                    self.ui.passwordEdit.clear()
                    return
                else:
                    password = self.ui.passwordEdit.text()
                    user_data[user] = password
                    with open("../user_json.json", 'w', encoding="utf-8") as f:
                        json.dump(user_data, f, ensure_ascii=False)
                    QMessageBox.about(self.ui, '提示', f'''注册成功''')
                    self.ui.userEdit.clear()
                    self.ui.passwordEdit.clear()
                    return
# app = QApplication([])
# windows = RegisterUI()
# windows.show()
# app.exec_()