from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer
import time
class timetextui(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel()
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.witch = 50
        self.start = 0

    def button_clicked(self):
        self.start = time.perf_counter()
        self.update_text()

    def update_text(self):
        if self.witch >= 0:
            finished = '<font color="green">' + '*' * (50 - self.witch) + '</font>'
            unfinished = '<font color="red">' + '.' * self.witch + '</font>'
            percent = ((50 - self.witch) / 50) * 100
            runtime = time.perf_counter() - self.start
            text = "{:^3.0f}%[{}->{}]{:.2f}秒".format(percent, finished, unfinished, runtime)
            self.label.setText(text)
            self.witch -= 1
            QTimer.singleShot(100, self.update_text)

app = QApplication([])
windows = timetextui()
windows.show()
app.exec_()
