import sys
import random
from PyQt5 import QtWidgets, QtGui, QtCore

class MyApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.lbl_1 = QtWidgets.QLabel("Hello World~")

        self.ed_1 = QtWidgets.QPlainTextEdit()

        self.btn_change_font = QtWidgets.QPushButton("Font Dialog")

        self.v_box = QtWidgets.QVBoxLayout()

        self.set_up()

    def set_up(self):
        self.setFont(QtGui.QFont("Arial", 12))
        self.setWindowTitle("Hello Word!")
        self.setGeometry(100, 100, 300, 200)
        icons = {
            0: QtGui.QIcon("icon\\chameleon.ico"),
            1: QtGui.QIcon("icon\\aol_mail.ico"),
            2: QtGui.QIcon("icon\\emotion_darth_wader.ico")
        }

        self.setWindowIcon(icons.get((random.randint(0, 9) % 3)))

        self.ed_1.insertPlainText("Hello world~")

        self.btn_change_font.clicked.connect(self.btn_change_font_click)

        self.v_box.addWidget(self.lbl_1)
        self.v_box.addWidget(self.ed_1)
        self.v_box.addWidget(self.btn_change_font)

        self.setLayout(self.v_box)

    def btn_change_font_click(self):
        font, valid = QtWidgets.QFontDialog.getFont()
        if valid:
            self.lbl_1.setFont(font)
            self.ed_1.setFont(font)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())