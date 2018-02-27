import sys
import random
from PyQt5 import QtWidgets, QtGui, QtCore

class MyApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ed_1 = QtWidgets.QTextEdit()
        self.ed_2 = QtWidgets.QLineEdit()

        self.lbl_1 = QtWidgets.QLabel("count:")

        self.btn_next = QtWidgets.QPushButton("Next")
        self.btn_back = QtWidgets.QPushButton("Back")

        self.h_box = QtWidgets.QHBoxLayout()
        self.v_box = QtWidgets.QVBoxLayout()

        self.set_up()
        self.show()

    def set_up(self):
        self.setFont(QtGui.QFont("Arial", 12))
        self.setWindowTitle("Hello Word!")
        self.setGeometry(100, 100, 600, 400)
        icons = {
            0: QtGui.QIcon("icon\\chameleon.ico"),
            1: QtGui.QIcon("icon\\aol_mail.ico"),
            2: QtGui.QIcon("icon\\emotion_darth_wader.ico")
        }

        self.setWindowIcon(icons.get((random.randint(0, 9) % 3)))

        text = """In this text I want to highlight this zzwordyy and only this word.\n""" + \
               """Any other word shouldn't be highlighted"""
        self.ed_1.setText(text)

        self.ed_2.setValidator(QtGui.QIntValidator())

        self.h_box.addWidget(self.lbl_1)
        self.h_box.addWidget(self.ed_2)

        self.btn_next.clicked.connect(self.btn_next_click)
        self.btn_back.clicked.connect(self.btn_back_click)
        self.h_box.addWidget(self.btn_next)
        self.h_box.addWidget(self.btn_back)

        self.v_box.addWidget(self.ed_1)
        self.v_box.addLayout(self.h_box)

        self.setLayout(self.v_box)

    def btn_next_click(self):
        try:
            cursor = self.ed_1.textCursor()
            print(cursor.position())
            self.ed_1.setFocus()
            if self.ed_2.text():
                # cursor.setPosition(int(self.ed_2.text()))
                cursor.movePosition(QtGui.QTextCursor.Right, QtGui.QTextCursor.MoveAnchor, int(self.ed_2.text()))
            print(cursor.block().text())
            print(cursor.position())
            self.ed_1.setTextCursor(cursor)
        except Exception as e:
            print(e)

    def btn_back_click(self):
        cursor = self.ed_1.textCursor()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())