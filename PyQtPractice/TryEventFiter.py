import sys
import random
from PyQt5 import QtCore, QtWidgets, QtGui

class MyApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.v_box = QtWidgets.QVBoxLayout()

        self.ed_1 = QtWidgets.QTextEdit()

        self.btn = QtWidgets.QPushButton("Press me to make fun~")

        self.frm_empty = QtWidgets.QFrame()

        self.set_up()

    def set_up(self):
        self.setFont(QtGui.QFont("Arial", 12))
        self.setWindowTitle("Hello Word!")
        icons = {
            0: QtGui.QIcon("icon\\chameleon.ico"),
            1: QtGui.QIcon("icon\\aol_mail.ico"),
            2: QtGui.QIcon("icon\\emotion_darth_wader.ico")
        }

        self.setWindowIcon(icons.get((random.randint(0, 9) % 3)))

        self.frm_empty.resize(500, 350)

        self.ed_1.installEventFilter(self)
        self.frm_empty.setMouseTracking(True)
        self.frm_empty.installEventFilter(self)
        self.btn.installEventFilter(self)

        self.v_box.addWidget(self.ed_1)
        self.v_box.addWidget(self.frm_empty)
        self.v_box.addWidget(self.btn)

        # self.frm_right.setMouseTracking(True)
        # self.frm_right.installEventFilter(self)

        # self.frm_left.setMouseTracking(True)
        # self.frm_left.installEventFilter(self)

        self.btn.clicked.connect(self.btn_click)

        self.setLayout(self.v_box)

    def eventFilter(self, obj, event):
        if (type(obj) == QtWidgets.QTextEdit) and \
                (event.type() == QtCore.QEvent.KeyPress):
            print(event.key())

        elif event.type() == QtCore.QEvent.MouseMove:
            print(type(obj))

        return False

    def showEvent(self, event):
        self.resize(800, 600)
        center = QtWidgets.QApplication.desktop().availableGeometry()
        x = (center.width() - self.width()) / 2
        y = (center.height() - self.height()) / 2
        self.move(x, y)

    def btn_click(self):
        QtWidgets.QMessageBox.information(self, "Say Hi", "Hello World", QtWidgets.QMessageBox.Ok)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())