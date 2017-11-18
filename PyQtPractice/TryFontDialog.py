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

        self.btn_change_font.clicked.connect(self.btn_change_font_click)

        self.v_box.addWidget(self.lbl_1)
        self.v_box.addWidget(self.ed_1)
        self.v_box.addWidget(self.btn_change_font)

        self.setLayout(self.v_box)

    def btn_change_font_click(self):
        font = QtWidgets.qApp.font()
        print("Default\r\nFont Family: {}, Point Size: {}".format(font.family(), font.pointSize()))

        font, valid = QtWidgets.QFontDialog.getFont()
        if valid:
            print("Change to\r\nFont Family: {}, Point Size: {}".format(
                font.family(), font.pointSize()))
            QtWidgets.qApp.setFont(font)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())