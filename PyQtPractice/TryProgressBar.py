import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.main_widget = QtWidgets.QWidget()

        self.progressbar = QtWidgets.QProgressBar()

        self.btn_run = QtWidgets.QPushButton("Run Run")

        self.v_box = QtWidgets.QVBoxLayout()

        self.set_up()

    def set_up(self):
        self.setCentralWidget(self.main_widget)

        self.progressbar.setMaximum(1000)

        self.btn_run.clicked.connect(self.btn_run_click)

        self.v_box.addWidget(self.progressbar)
        self.v_box.addWidget(self.btn_run)

        self.main_widget.setLayout(self.v_box)

    def btn_run_click(self):
        count = 0
        while count < 1000:
            count += 0.0001
            self.progressbar.setValue(count)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())