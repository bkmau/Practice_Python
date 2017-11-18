import sys
import random
from PyQt5 import QtWidgets, QtGui, QtCore

class MyApp(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.lbl_1 = QtWidgets.QLabel("self is")
        self.lbl_2 = QtWidgets.QLabel(str(self))
        self.lbl_3 = QtWidgets.QLabel("QtWidgets.QApplication.desktop().availableGeometry()")
        self.lbl_4 = QtWidgets.QLabel(str(QtWidgets.QApplication.desktop().availableGeometry()))

        self.lbl_5 = QtWidgets.QLabel("self.frameGeometry():")
        self.lbl_6 = QtWidgets.QLabel("self.pos():")
        self.lbl_7 = QtWidgets.QLabel("self.x():")
        self.lbl_8 = QtWidgets.QLabel("self.y():")
        self.lbl_9 = QtWidgets.QLabel("self.frameSize()")
        self.lbl_10 = QtWidgets.QLabel("self.frameGeometry().width()")
        self.lbl_11 = QtWidgets.QLabel("self.frameGeometry().height()")
        self.lbl_12 = QtWidgets.QLabel("self.geometry()")
        self.lbl_13 = QtWidgets.QLabel("self.geometry().x()")
        self.lbl_14 = QtWidgets.QLabel("self.geometry().y()")
        self.lbl_15 = QtWidgets.QLabel("self.rect():")
        self.lbl_16 = QtWidgets.QLabel("self.size():")
        self.lbl_17 = QtWidgets.QLabel("self.width():")
        self.lbl_18 = QtWidgets.QLabel("self.geometry().width()")
        self.lbl_19 = QtWidgets.QLabel("self.height():")
        self.lbl_20 = QtWidgets.QLabel("self.geometry().height():")
        self.lbl_21 = QtWidgets.QLabel("self.minimumSize()")
        self.lbl_22 = QtWidgets.QLabel("self.minimumWidth()")
        self.lbl_23 = QtWidgets.QLabel("self.minimumHeight()")
        self.lbl_24 = QtWidgets.QLabel("self.maximumSize()")
        self.lbl_25 = QtWidgets.QLabel("self.maximumWidth()")
        self.lbl_26 = QtWidgets.QLabel("self.maximumHeight()")

        self.ed_5 = QtWidgets.QLineEdit()
        self.ed_6 = QtWidgets.QLineEdit()
        self.ed_7 = QtWidgets.QLineEdit()
        self.ed_8 = QtWidgets.QLineEdit()
        self.ed_9 = QtWidgets.QLineEdit()
        self.ed_10 = QtWidgets.QLineEdit()
        self.ed_11 = QtWidgets.QLineEdit()
        self.ed_12 = QtWidgets.QLineEdit()
        self.ed_13 = QtWidgets.QLineEdit()
        self.ed_14 = QtWidgets.QLineEdit()
        self.ed_15 = QtWidgets.QLineEdit()
        self.ed_16 = QtWidgets.QLineEdit()
        self.ed_17 = QtWidgets.QLineEdit()
        self.ed_18 = QtWidgets.QLineEdit()
        self.ed_19 = QtWidgets.QLineEdit()
        self.ed_20 = QtWidgets.QLineEdit()
        self.ed_21 = QtWidgets.QLineEdit()
        self.ed_22 = QtWidgets.QLineEdit()
        self.ed_23 = QtWidgets.QLineEdit()
        self.ed_24 = QtWidgets.QLineEdit()
        self.ed_25 = QtWidgets.QLineEdit()
        self.ed_26 = QtWidgets.QLineEdit()

        self.lables_1 = [
            self.lbl_5, self.lbl_6,
            self.lbl_7, self.lbl_8, self.lbl_9, self.lbl_10, self.lbl_11
        ]

        self.lineedits_1 = [
            self.ed_5, self.ed_6,
            self.ed_7, self.ed_8,  self.ed_9, self.ed_10, self.ed_11
        ]

        self.lables_2 = [
            self.lbl_12, self.lbl_13, self.lbl_14, self.lbl_15, self.lbl_16,
            self.lbl_17, self.lbl_18, self.lbl_19, self.lbl_20
        ]

        self.lineedits_2 = [
            self.ed_12, self.ed_13, self.ed_14, self.ed_15, self.ed_16,
            self.ed_17, self.ed_18, self.ed_19, self.ed_20
        ]

        self.lables_3 = [
            self.lbl_21, self.lbl_22, self.lbl_23
        ]

        self.lineedits_3 = [
            self.ed_21, self.ed_22, self.ed_23
        ]

        self.lables_4 = [
            self.lbl_24, self.lbl_25, self.lbl_26
        ]

        self.lineedits_4 = [
            self.ed_24, self.ed_25, self.ed_26
        ]

        self.h_box_1 = QtWidgets.QHBoxLayout()
        self.h_box_2 = QtWidgets.QHBoxLayout()
        self.g_box = QtWidgets.QGridLayout()
        self.v_box = QtWidgets.QVBoxLayout()

        self.set_up()

    def set_up(self):
        QtWidgets.qApp.setFont(QtGui.QFont("Arial", 12))
        self.setWindowTitle("Hello Word!")
        self.setWindowFlags(
            QtCore.Qt.WindowMaximizeButtonHint |
            QtCore.Qt.WindowMinimizeButtonHint |
            QtCore.Qt.WindowCloseButtonHint
        )

        icons = {
            0: QtGui.QIcon("icon\\chameleon.ico"),
            1: QtGui.QIcon("icon\\aol_mail.ico"),
            2: QtGui.QIcon("icon\\emotion_darth_wader.ico")
        }

        self.setWindowIcon(icons.get((random.randint(0, 9) % 3)))

        for index, lbl in enumerate(self.lables_1):
            self.g_box.addWidget(lbl, index, 0)

        for index, ed in enumerate(self.lineedits_1):
            self.g_box.addWidget(ed, index, 1)

        for index, lbl in enumerate(self.lables_2):
            self.g_box.addWidget(lbl, index, 2)

        for index, ed in enumerate(self.lineedits_2):
            self.g_box.addWidget(ed, index, 3)

        end = index + 2
        for index, lbl in enumerate(self.lables_3):
            self.g_box.addWidget(lbl, (index + end), 0)

        for index, ed in enumerate(self.lineedits_3):
            self.g_box.addWidget(ed, (index + end), 1)

        for index, lbl in enumerate(self.lables_4):
            self.g_box.addWidget(lbl, (index + end), 2)

        for index, ed in enumerate(self.lineedits_4):
            self.g_box.addWidget(ed, (index + end), 3)

        self.h_box_1.addWidget(self.lbl_1)
        self.h_box_1.addWidget(self.lbl_2)

        self.h_box_2.addWidget(self.lbl_3)
        self.h_box_2.addWidget(self.lbl_4)

        self.v_box.addLayout(self.h_box_1)
        self.v_box.addLayout(self.h_box_2)
        self.v_box.addLayout(self.g_box)

        self.setLayout(self.v_box)

        for index, ed in enumerate(self.findChildren(QtWidgets.QLineEdit)):
            ed.setReadOnly(True)

            palette = ed.palette()
            palette.setColor(QtGui.QPalette.Base, QtCore.Qt.lightGray)
            palette.setColor(QtGui.QPalette.Text, QtCore.Qt.black)
            ed.setPalette(palette)

    def moveEvent(self, event):
        self.set_value()

    def resizeEvent(self, event):
        self.set_value()

    def showEvent(self, event):
        self.resize(800, 600)
        center = QtWidgets.QApplication.desktop().availableGeometry()
        # center = QtWidgets.qApp.desktop().availableGeometry()
        x = (center.width() - self.width()) / 2
        y = (center.height() - self.height()) / 2

        # x = (QtWidgets.QApplication.desktop().width() - self.width()) / 2
        # y = (QtWidgets.QApplication.desktop().height() - self.height()) / 2
        self.move(x, y)

    def set_value(self):
        self.ed_5.setText(str(self.frameGeometry()))
        self.ed_6.setText(str(self.pos()))
        self.ed_7.setText(str(self.x()))
        self.ed_8.setText(str(self.y()))
        self.ed_9.setText(str(self.frameSize()))
        self.ed_10.setText(str(self.frameGeometry().width()))
        self.ed_11.setText(str(self.frameGeometry().height()))
        self.ed_12.setText(str(self.geometry()))
        self.ed_13.setText(str(self.geometry().x()))
        self.ed_14.setText(str(self.geometry().y()))
        self.ed_15.setText(str(self.rect()))
        self.ed_16.setText(str(self.size()))
        self.ed_17.setText(str(self.width()))
        self.ed_18.setText(str(self.geometry().width()))
        self.ed_19.setText(str(self.height()))
        self.ed_20.setText(str(self.geometry().height()))
        self.ed_21.setText(str(self.minimumSize()))
        self.ed_22.setText(str(self.minimumWidth()))
        self.ed_23.setText(str(self.minimumHeight()))
        self.ed_24.setText(str(self.maximumSize()))
        self.ed_25.setText(str(self.maximumWidth()))
        self.ed_26.setText(str(self.maximumHeight()))

        for index, ed in enumerate(self.findChildren(QtWidgets.QLineEdit)):
            ed.setCursorPosition(0)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    window.set_value()
    sys.exit(app.exec_())