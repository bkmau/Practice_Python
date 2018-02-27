import sys
import random
from PyQt5 import QtWidgets, QtGui

class MyApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.lbl_1 = QtWidgets.QLabel("Hello World~")

        self.ed_1 = QtWidgets.QTextEdit()

        self.btn_change_color = QtWidgets.QPushButton("Change Color")
        self.btn_print_qss = QtWidgets.QPushButton("Print QSS")

        self.chk_using_qss = QtWidgets.QCheckBox("Using Q Style Sheet")
        self.gb_1 = QtWidgets.QGroupBox("Color")
        self.rb_red = QtWidgets.QRadioButton("red")
        self.rb_blue = QtWidgets.QRadioButton("blue")
        self.rb_green = QtWidgets.QRadioButton("green")

        self.h_box = QtWidgets.QHBoxLayout()
        self.v_box = QtWidgets.QVBoxLayout()

        self.set_up()

    def set_up(self):
        QtWidgets.qApp.setFont(QtGui.QFont("Arial", 12))
        self.setWindowTitle("Hello Word!")
        self.setGeometry(100, 100, 300, 200)
        icons = {
            0: QtGui.QIcon("icon\\chameleon.ico"),
            1: QtGui.QIcon("icon\\aol_mail.ico"),
            2: QtGui.QIcon("icon\\emotion_darth_wader.ico")
        }

        self.setWindowIcon(icons.get((random.randint(0, 9) % 3)))

        self.ed_1.insertPlainText("Hello world~")

        self.btn_change_color.clicked.connect(self.btn_change_color_click)
        self.btn_print_qss.clicked.connect(self.btn_print_qss_click)

        self.chk_using_qss.stateChanged.connect(self.chk_using_qss_state_change)
        self.rb_red.toggled.connect(self.rb_toggle)
        self.rb_blue.toggled.connect(self.rb_toggle)
        self.rb_green.toggled.connect(self.rb_toggle)

        self.h_box.addWidget(self.rb_red)
        self.h_box.addWidget(self.rb_blue)
        self.h_box.addWidget(self.rb_green)
        self.gb_1.setLayout(self.h_box)

        self.v_box.addWidget(self.lbl_1)
        self.v_box.addWidget(self.ed_1)
        self.v_box.addWidget(self.chk_using_qss)
        self.v_box.addWidget(self.gb_1)
        self.v_box.addWidget(self.btn_change_color)
        self.v_box.addWidget(self.btn_print_qss)

        self.setLayout(self.v_box)

    def btn_change_color_click(self):
        try:
            color = QtWidgets.QColorDialog.getColor()
            if color.isValid():
                if self.chk_using_qss.isChecked():
                    self.lbl_1.setStyleSheet(
                        "QLabel {{background-color: {}}}".format(color.name()))

                    text = self.ed_1.toPlainText()
                    self.ed_1.clear()
                    self.ed_1.setStyleSheet("QTextEdit {{color: {}}}".format(color.name()))
                    self.ed_1.setText(text)
                else:
                    self.lbl_1.setAutoFillBackground(True)
                    palette = self.lbl_1.palette()
                    palette.setColor(QtGui.QPalette.Window, color)
                    self.lbl_1.setPalette(palette)

                    text = self.ed_1.toPlainText()
                    self.ed_1.clear()
                    self.ed_1.setTextColor(color)
                    self.ed_1.setText(text)

        except Exception as e:
            print(e)

    def btn_print_qss_click(self):
        print("lbl_1: {}; ed_1: {}".format(self.lbl_1.styleSheet(), self.ed_1.styleSheet()))

    def chk_using_qss_state_change(self):
        if self.chk_using_qss.isChecked():
            # self.setStyleSheet("QWidget {font-family: Arial; font-size: 12pt;}")
            self.lbl_1.setStyleSheet(QtWidgets.qApp.styleSheet())
            text = self.ed_1.toPlainText()
            self.ed_1.clear()
            self.ed_1.setTextColor(QtWidgets.qApp.palette().text().color())
            self.ed_1.setText(text)
        else:
            self.lbl_1.setStyleSheet(QtWidgets.qApp.styleSheet())
            self.ed_1.setStyleSheet(QtWidgets.qApp.styleSheet())
            self.setFont(QtGui.QFont("Arial", 12))

            text = self.ed_1.toPlainText()
            self.ed_1.clear()
            self.ed_1.setTextColor(QtWidgets.qApp.palette().text().color())
            self.ed_1.setText(text)

    def rb_toggle(self):
        print(self.sender().text())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())