from PyQt5.QtWidgets import QMainWindow, QAction, QApplication, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 创建三个 QAction 对象，并设置对应的文本
        action1 = QAction('显示控件1', self)
        action2 = QAction('显示控件2', self)
        action3 = QAction('显示控件3', self)

        # 将每个 QAction 添加到菜单中
        menu = self.menuBar().addMenu('菜单')
        menu.addAction(action1)
        menu.addAction(action2)
        menu.addAction(action3)

        # 连接每个 QAction 的 triggered 信号到对应的槽函数
        action1.triggered.connect(self.showWidget1)
        action2.triggered.connect(self.showWidget2)
        action3.triggered.connect(self.showWidget3)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('示例窗口')
        self.show()

    def showWidget1(self):
        # 清除现有的中央部件
        self.centralWidget().deleteLater()
        # 创建并显示控件1
        widget1 = QLabel('这是控件1', self)
        self.setCentralWidget(widget1)

    def showWidget2(self):
        # 清除现有的中央部件
        self.centralWidget().deleteLater()
        # 创建并显示控件2
        widget2 = QLabel('这是控件2', self)
        self.setCentralWidget(widget2)

    def showWidget3(self):
        # 清除现有的中央部件
        self.centralWidget().deleteLater()
        # 创建并显示控件3
        widget3 = QLabel('这是控件3', self)
        self.setCentralWidget(widget3)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
