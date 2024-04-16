from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5 import uic
import os
import sys
import socket
import time

class LogPy(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('./ui/LogPy.ui', self)
        self.ui.pushButton.clicked.connect(self.LogPy)
        self.ui.pushButton_2.clicked.connect(self.OpenLog)
        self.ui.pushButton_3.clicked.connect(self.clearlog)
        self.outlog = ''

    def OpenLog(self):
        with open('log.txt', 'r') as fp:
            data =fp.readlines()
            string =''
            for i in data:
                string += i
            # print(string)
            self.ui.textEdit.setText(string)
    def LogPy(self):
        self.ui.textEdit.setText('')
        self.muisic()
        self.add(5, 8)


    def add_log(fun):
        def wrapper(self,*args, **kwargs):
            result = fun(self,*args, **kwargs)
            now_time = time.ctime()
            hostname = socket.gethostname()
            process_full_name = sys.argv[0]
            print(process_full_name)
            process_name = os.path.split(process_full_name)[-1]
            info = '\n[%s]函数运行的结果是%s' % (fun.__name__, result)
            log = ' '.join([now_time, hostname, process_name, info])
            with open('log.txt', 'a') as fp:
                fp.write(log)
            fp.close()
            self.ui.textEdit.append(log)
            return result

        return wrapper

    def clearlog(self):
        with open('log.txt', 'w') as file:
            self.ui.textEdit.setText('')
            pass

    @add_log
    def muisic(self):
        time.sleep(1)
        self.outlog += "正在听音乐\n"

    @add_log
    def add(self,x, y):
        return x + y
# app = QApplication([])
# start = LogPy()
# start.show()
# app.exec_()