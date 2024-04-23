"""
configeditui.py - 

Author: leting130
Date: 2024/4/23
github:https://github.com/yating1022
"""
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5 import uic
import configparser
class Configeditui(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('./ui/configedit.ui',self)
        self.ui.pushButton.clicked.connect(self.run)
    def run(self):
        myconfig = configparser.ConfigParser()
        myconfig.read("config.ini")
        string = myconfig.sections()
        print(string)
        if myconfig.has_section("database"):
            items = myconfig.items("database")
            print(items)
            values = myconfig.get("database", "port")
            print("port为" + values)
            has_encoding = myconfig.has_option("database", "encoding")
            print(has_encoding)
            if has_encoding:
                myconfig.remove_option("database", "encoding")
                myconfig.write(open('../config.ini', 'w'))
            else:
                myconfig.set("database", "encoding", "utf-8")
                myconfig.write(open('../config.ini', 'w'))
        else:
            myconfig["database"] = {"host": "127.0.0.1", "user": "root", "password": "123", "port": 3306, "db": "pet"}
# app = QApplication([])
# windwos = Configeditui()
# windwos.show()
# app.exec_()