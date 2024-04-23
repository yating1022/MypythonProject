"""
An02sysui - 

Author: leting130
Date: 2024/4/23
github:https://github.com/yating1022
"""
import subprocess

from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5 import uic
import time
class An02sysui(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("./ui/An02sysui.ui", self)
        self.ui.Button.clicked.connect(self.ping)

    def startandendtime(fun):
        def wrapper(self,*args, **kwargs):
            start = time.perf_counter()
            fun(self,*args, **kwargs)
            end = time.perf_counter()
            setime = "运行时间 {:.2f} 秒".format(end - start)
            self.ui.labeltime.setText(setime)
        return wrapper

    @startandendtime
    def ping(self,n = 2,q=1, w=1):
        net = self.ui.iplineEdit.text()
        start = int(self.ui.startlineEdit.text())
        end = int(self.ui.endlineEdit.text())
        str2 = "icmp_seq"
        iplist = ''
        for x in range(start, end + 1):
            ip = net + '.' + str(x)
            command = ["ping", ip, "-c", str(q), "-w", str(w)]
            print(command)
            process = subprocess.Popen(command, stdout=subprocess.PIPE)
            output, _ = process.communicate()
            output = output.decode('utf-8')
            if str2 in output:
                print(ip, "通")
                iplist += ip + "-------------设备" + str(x) + '\n'
                self.ui.textEdit.setText(iplist)
            else:
                print(ip, "不通")
            print(iplist)
        with open('../ip.txt', 'w') as f:
            f.writelines(iplist)
# app = QApplication([])
# windows = An02sysui()
# windows.show()
# app.exec_()