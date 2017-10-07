import sys
import random
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt

class MyApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ed_1 = QtWidgets.QLineEdit()
        self.btn_1 = QtWidgets.QPushButton("Clear")
        self.btn_2 = QtWidgets.QPushButton("Print")
        self.slider_1 = QtWidgets.QSlider(Qt.Horizontal)
        self.h_box = QtWidgets.QHBoxLayout()
        self.v_box = QtWidgets.QVBoxLayout()

        self.set_up()
        self.show()

    def set_up(self):
        self.setFont(QtGui.QFont("Arial", 12))
        self.setWindowTitle("Hello Word!")
        self.setGeometry(100, 100, 300, 200)

        self.btn_1.clicked.connect(
            lambda: self.btn_click(self.btn_1, "You were clicked Clear button!"))
        self.btn_2.clicked.connect(
            lambda: self.btn_click(self.btn_2, "You were clicked Print button!"))

        self.slider_1.setMinimum(0)
        self.slider_1.setMaximum(99)
        self.slider_1.setValue(random.randint(0, 99))
        self.slider_1.setTickInterval(10)
        self.slider_1.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_1.valueChanged.connect(self.slider_1_value_change)

        self.v_box.addWidget(self.ed_1)
        self.v_box.addWidget(self.btn_1)
        self.v_box.addWidget(self.btn_2)
        self.v_box.addWidget(self.slider_1)

        self.setLayout(self.v_box)

    def btn_click(self, btn, msg):
        if btn.text() == "Print":
            print(self.ed_1.text())
        elif btn.text() == "Clear":
            self.ed_1.clear()
        print(msg)

    def slider_1_value_change(self):
        self.ed_1.setText(str(self.slider_1.value()))

app = QtWidgets.QApplication(sys.argv)
window = MyApp()
sys.exit(app.exec_())