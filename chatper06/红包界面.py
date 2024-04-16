from PyQt5.QtWidgets import QApplication
from PyQt5 import uic
import sys
app = QApplication(sys.argv)
ui = uic.loadUi('红包.ui')
ui.show()
sys.exit(app.exec_())