import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.main_widget = QtWidgets.QWidget()

        self.lbl_display = QtWidgets.QLabel()

        self.combobox = QtWidgets.QComboBox()

        self.progressbar = QtWidgets.QProgressBar()

        self.btn_run = QtWidgets.QPushButton("Run Run")

        self.v_box = QtWidgets.QVBoxLayout()

        self.set_up()

    def set_up(self):
        self.setCentralWidget(self.main_widget)

        self.lbl_display.setText(self.style().objectName())

        self.combobox.addItems(key for key in QtWidgets.QStyleFactory.keys())

        for index, key in enumerate(QtWidgets.QStyleFactory.keys()):
            if key.upper() == self.style().objectName().upper():
                self.combobox.setCurrentIndex(index)
                break

        self.combobox.activated[str].connect(self.style_choice)

        self.btn_run.clicked.connect(self.btn_run_click)

        self.v_box.addWidget(self.lbl_display)
        self.v_box.addWidget(self.combobox)
        self.v_box.addWidget(self.progressbar)
        self.v_box.addWidget(self.btn_run)

        self.main_widget.setLayout(self.v_box)

    def style_choice(self, text):
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create(text))

    def btn_run_click(self):
        count = 0
        while count < 100:
            count += 0.0001
            self.progressbar.setValue(count)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())