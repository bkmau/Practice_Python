import sys
import random
from PyQt5 import QtWidgets, QtGui, QtCore

class MyApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.icon_set = {
            "leaf": "icon\\leaf.png",
            "fire": "icon\\fire.png",
            "wind": "icon\\wind.png",
            "water": "icon\\water.png"
        }
        self.keys = ["leaf", "fire", "wind", "water"]

        self.lbl_1 = QtWidgets.QLabel()
        self.lbl_2 = QtWidgets.QLabel()
        self.btn_1 = QtWidgets.QPushButton()
        self.btn_elements = [QtWidgets.QPushButton() for _ in range(4)]

        self.h1_box = QtWidgets.QHBoxLayout()
        self.h2_box = QtWidgets.QHBoxLayout()
        self.v_box = QtWidgets.QVBoxLayout()

        self.set_up()
        self.show()

    def set_up(self):
        self.setFont(QtGui.QFont("Arial", 12))
        self.setWindowTitle("Hello Word!")
        self.setGeometry(100, 100, 300, 200)

        png = self.keys[random.randint(0, (len(self.keys) - 1))]

        self.lbl_1.setText("Here is {}".format(png))

        self.lbl_2.setPixmap(QtGui.QPixmap(self.icon_set.get(png)))

        self.btn_1.setText("Rand Change")
        self.btn_1.clicked.connect(self.btn_1_click)

        for index, button in enumerate(self.btn_elements):
            name = self.keys[index]
            button.setObjectName(name)
            button.setToolTip("Change to {}".format(name))
            button.setIcon(QtGui.QIcon(self.icon_set.get(name)))
            button.setIconSize(QtCore.QSize(50, 50))
            button.clicked.connect(self.btn__click)

        self.h1_box.addStretch()  # 在插入按鈕前增加一個佔位符
        self.h1_box.addWidget(self.lbl_1)
        self.h1_box.addWidget(self.lbl_2)

        self.h2_box.setSpacing(10)  # 設定元件間的距離為5

        for button in self.btn_elements:
            self.h2_box.addWidget(button)

        self.v_box.addLayout(self.h1_box)
        self.v_box.addWidget(self.btn_1)
        self.v_box.addLayout(self.h2_box)

        self.setLayout(self.v_box)

    def btn_1_click(self):
        png = self.keys[random.randint(0, (len(self.keys) - 1))]
        self.lbl_1.setText("Here is {}".format(png))
        self.lbl_2.setPixmap(QtGui.QPixmap(self.icon_set.get(png)))

    def btn__click(self):
        self.lbl_1.setText("Here is {}".format(self.sender().objectName()))
        self.lbl_2.setPixmap(QtGui.QPixmap(self.icon_set.get(self.sender().objectName())))

app = QtWidgets.QApplication(sys.argv)
window = MyApp()
sys.exit(app.exec_())