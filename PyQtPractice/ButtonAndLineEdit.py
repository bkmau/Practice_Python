import sys
import random
from PyQt5 import QtWidgets, QtGui

class MyApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ed_1 = QtWidgets.QLineEdit()
        self.btn_1 = QtWidgets.QPushButton("Clear")
        self.btn_2 = QtWidgets.QPushButton("Print")
        self.btn_3 = QtWidgets.QPushButton("Nothing")
        self.h_box = QtWidgets.QHBoxLayout()
        self.v_box = QtWidgets.QVBoxLayout()

        self.set_up()
        self.show()

    def set_up(self):
        self.setFont(QtGui.QFont("Arial", 12))
        self.setWindowTitle("Hello Word!")
        self.setGeometry(100, 100, 300, 200)

        self.btn_1.clicked.connect(self.btn_click)
        self.btn_2.clicked.connect(self.btn_click)
        self.btn_3.clicked.connect(self.btn_click)

        self.v_box.addWidget(self.ed_1)
        self.v_box.addWidget(self.btn_1)
        self.v_box.addWidget(self.btn_2)
        self.v_box.addWidget(self.btn_3)

        self.setLayout(self.v_box)

    def btn_click(self):
        if self.sender().text() == "Print":
            print(self.ed_1.text())
        elif self.sender().text() == "Clear":
            self.ed_1.clear()


app = QtWidgets.QApplication(sys.argv)
window = MyApp()
sys.exit(app.exec_())