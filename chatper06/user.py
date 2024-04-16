from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5 import uic
class User(QWidget):
    def __init__(self):
        super().__init__()
        self.users={}
        self.users = self.ReadFile('users.csv')
        self.ui = uic.loadUi('./ui/user.ui', self)
        self.ui.addUser.clicked.connect(self.adduser)
        self.ui.tableWidget.setColumnCount(2)  # 设置列数为2，用于显示键和值
        self.ui.tableWidget.setHorizontalHeaderLabels(["用户名", "密码"])  # 设置表头
        self.ui.viewUser.clicked.connect(self.showList)
        self.ui.pushButton.setText('请点击菜单')
        self.ui.removeUser.clicked.connect(self.remove)
    def adduser(self):
        self.ui.pushButton.setText('请输入用户名并回车')
        self.ui.lineEdit.returnPressed.connect(self.addusername)
    def writeFile(self,file):
        with open('users.csv', 'w+') as fp:
            s=''
            for key,value in self.users.items():
                s=s+key+','+value+'\n'
            fp.writelines(s)#把每一行写入



    def addusername(self):
            self.username = self.ui.lineEdit.text()
            print(self.username)
            if self.username in self.users.keys():
                QMessageBox.about(self.ui, '提示', f'''用户已存在''')
                self.ui.pushButton.setText('请点击菜单')
            else:
                self.ui.pushButton.setText('请输入密码并回车')
                self.ui.lineEdit.returnPressed.disconnect(self.addusername)
                self.ui.lineEdit.returnPressed.connect(self.addpassword)
    def addpassword(self):
        self.password = self.ui.lineEdit.text()
        self.ui.lineEdit.returnPressed.disconnect(self.addpassword)
        print(self.username)
        print(self.password)
        self.users[self.username] = self.password
        self.writeFile('users.csv')
        self.showList()
        self.ui.pushButton.setText('请点击菜单')

    def showList(self):#查看用户命令
        # 清空表格
        self.tableWidget.setRowCount(0)
        # 逐个添加字典元素到表格中
        for row, (key, value) in enumerate(self.users.items()):
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(key)))  # 显示键
            self.tableWidget.setItem(row, 1, QTableWidgetItem(str(value)))  # 显示值

    def ReadFile(self,file):  # 读取的方法
        with open('users.csv', 'r+') as fp:
            lines = fp.readlines()
            for line in lines:
                d = line.strip('\n').split(sep=",")  # 分隔开来
                print(d)
                self.users[d[0]] = d[1]  # 存入
        return self.users

    def remove(self):
            currentrow = self.ui.tableWidget.currentRow()
            string = self.ui.tableWidget.item(currentrow,0).text()
            del self.users[string]
            QMessageBox.about(self.ui, '提示', f'''删除成功''')
            self.showList()
# app = QApplication([])
# start = User()
# start.ui.show()
# app.exec_()