import sys
import random
from PyQt5 import QtWidgets, QtGui, QtCore


class MyApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.spinbox = QtWidgets.QSpinBox(self)
        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)

        self.h_box = QtWidgets.QHBoxLayout()

        self.set_up()

    def set_up(self):
        self.setFont(QtGui.QFont("Arial", 12))
        self.setWindowTitle("Hello Word!")

        icons = {
            0: QtGui.QIcon("icon\\chameleon.ico"),
            1: QtGui.QIcon("icon\\aol_mail.ico"),
            2: QtGui.QIcon("icon\\emotion_darth_wader.ico")
        }
        self.setWindowIcon(icons.get(random.randint(0, 9) % 3))

        self.spinbox.setRange(0, 999)
        self.slider.setRange(0, 999)

        self.slider.valueChanged.connect(self.spinbox.setValue)

        self.spinbox.valueChanged.connect(self.slider.setValue)

        self.spinbox.setValue(35)

        self.h_box.addWidget(self.spinbox)
        self.h_box.addWidget(self.slider)

        self.setLayout(self.h_box)

    def showEvent(self, event):
        self.resize(600, 100)
        center = QtWidgets.QApplication.desktop().availableGeometry()
        x = (center.width() - self.width()) / 2
        y = (center.height() - self.height()) / 2
        self.move(x, y)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
