import sys
import os
from PyQt5 import QtWidgets, QtGui


class MyApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ed_1 = QtWidgets.QTextEdit()
        self.btn_1 = QtWidgets.QPushButton("Clear")
        self.btn_2 = QtWidgets.QPushButton("Save")
        self.btn_3 = QtWidgets.QPushButton("Open")

        self.h_box = QtWidgets.QHBoxLayout()
        self.v_box = QtWidgets.QVBoxLayout()

        self.set_up()
        self.show()

    def set_up(self):
        self.setFont(QtGui.QFont("Arial", 12))
        self.setWindowTitle("Hello Word!")
        self.setGeometry(100, 100, 300, 200)

        self.btn_1.clicked.connect(self.btn_1_click)
        self.btn_2.clicked.connect(self.btn_2_click)
        self.btn_3.clicked.connect(self.btn_3_click)

        self.h_box.addWidget(self.btn_1)
        self.h_box.addWidget(self.btn_2)
        self.h_box.addWidget(self.btn_3)

        self.v_box.addWidget(self.ed_1)
        self.v_box.addLayout(self.h_box)

        self.setLayout(self.v_box)

    def btn_1_click(self):
        self.ed_1.clear()

    def btn_2_click(self):
        name = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save File", os.getenv("HOME"), "Plain text(*.txt);;XML(*.xml);;All(*)")
        if name[0]:
            with open(name[0], "w") as f:
                f.write(self.ed_1.toPlainText())

    def btn_3_click(self):
        name = QtWidgets.QFileDialog.getOpenFileName(
            self, "Open File", os.getenv("HOME"), "Plain text(*.txt);;XML(*.xml);;All(*)")
        if name[0]:
            with open(name[0], "r", encoding="UTF-8") as f:
                self.ed_1.setText(f.read())


app = QtWidgets.QApplication(sys.argv)
window = MyApp()
sys.exit(app.exec_())