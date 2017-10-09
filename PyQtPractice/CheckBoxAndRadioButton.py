import sys
from PyQt5 import QtWidgets, QtGui

class MyApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.lbl_1 = QtWidgets.QLabel()

        self.btn_1 = QtWidgets.QPushButton("Clear")
        self.btn_2 = QtWidgets.QPushButton("Finish")

        self.gb_1 = QtWidgets.QGroupBox("Gender")
        self.rb_1 = QtWidgets.QRadioButton("Male")
        self.rb_2 = QtWidgets.QRadioButton("Female")

        self.gb_2 = QtWidgets.QGroupBox("What fruits do you like it?")
        self.chk_1 = QtWidgets.QCheckBox("Apple")
        self.chk_2 = QtWidgets.QCheckBox("Banana")
        self.chk_3 = QtWidgets.QCheckBox("Cherry")
        self.chk_4 = QtWidgets.QCheckBox("Durian")

        self.h_box_1 = QtWidgets.QHBoxLayout()
        self.h_box_2 = QtWidgets.QHBoxLayout()

        self.v_box_1 = QtWidgets.QVBoxLayout()
        self.v_box_2 = QtWidgets.QVBoxLayout()

        self.set_up()
        self.show()

    def set_up(self):
        self.setFont(QtGui.QFont("Arial", 12))
        self.setWindowTitle("Hello Word!")
        self.setGeometry(100, 100, 300, 200)

        self.v_box_2.addWidget(self.rb_1)
        self.v_box_2.addWidget(self.rb_2)
        self.gb_1.setLayout(self.v_box_2)

        self.h_box_1.addWidget(self.chk_1)
        self.h_box_1.addWidget(self.chk_2)
        self.h_box_1.addWidget(self.chk_3)
        self.h_box_1.addWidget(self.chk_4)
        self.gb_2.setLayout(self.h_box_1)

        self.h_box_2.addWidget(self.btn_1)
        self.h_box_2.addWidget(self.btn_2)

        self.v_box_1.addWidget(self.gb_1)
        self.v_box_1.addWidget(self.gb_2)
        self.v_box_1.addLayout(self.h_box_2)

        self.btn_1.clicked.connect(self.btn_click)
        self.btn_2.clicked.connect(self.btn_click)

        self.setLayout(self.v_box_1)

    def btn_click(self):
        if self.sender().text() == "Clear":
            self.rb_1.setAutoExclusive(False)
            self.rb_1.setChecked(False)
            self.rb_1.setAutoExclusive(True)
            self.rb_2.setAutoExclusive(False)
            self.rb_2.setChecked(False)
            self.rb_2.setAutoExclusive(True)
            self.chk_1.setChecked(False)
            self.chk_2.setChecked(False)
            self.chk_3.setChecked(False)
            self.chk_4.setChecked(False)
        else:
            QtWidgets.QMessageBox().about(self, "Thanks!!", "Thank You!!")
            self.close()


app = QtWidgets.QApplication(sys.argv)
window = MyApp()
sys.exit(app.exec_())