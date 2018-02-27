import sys
import random
import datetime
from PyQt5 import QtWidgets, QtGui, QtCore

class MyApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ed_1 = QtWidgets.QDateEdit()

        self.lcd = QtWidgets.QLCDNumber()

        self.btn_date_dialog = QtWidgets.QPushButton("Date Dialog")

        self.h_box = QtWidgets.QHBoxLayout()
        self.v_box = QtWidgets.QVBoxLayout()

        self.cal = QtWidgets.QCalendarWidget()

        self.timer = QtCore.QTimer(self)

        self.set_up()

        self.timer.start()

    def set_up(self):
        QtWidgets.qApp.setFont(QtGui.QFont("Arial", 12))
        self.setWindowTitle("Hello Word!")

        icons = {
            0: QtGui.QIcon("icon\\chameleon.ico"),
            1: QtGui.QIcon("icon\\aol_mail.ico"),
            2: QtGui.QIcon("icon\\emotion_darth_wader.ico")
        }

        self.setWindowIcon(icons.get((random.randint(0, 9) % 3)))

        my_date_time = datetime.datetime.now()
        self.ed_1.setDate(my_date_time.date())

        self.lcd.setDigitCount(8)
        self.lcd.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd.setStyleSheet("border: 1px solid green; black: green; background: silver;")
        self.lcd.display(my_date_time.time().strftime("%H:%M:%S"))

        self.btn_date_dialog.clicked.connect(self.btn_date_dialog_click)

        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_lcd)

        self.h_box.addWidget(self.ed_1)
        self.v_box.addLayout(self.h_box)
        self.v_box.addWidget(self.lcd)
        self.v_box.addWidget(self.btn_date_dialog)
        # self.v_box.addWidget(self.cal)

        self.setLayout(self.v_box)

    def showEvent(self, event):
        self.resize(400, 300)
        center = QtWidgets.QApplication.desktop().availableGeometry()
        # center = QtWidgets.qApp.desktop().availableGeometry()
        x = (center.width() - self.width()) / 2
        y = (center.height() - self.height()) / 2

        # x = (QtWidgets.QApplication.desktop().width() - self.width()) / 2
        # y = (QtWidgets.QApplication.desktop().height() - self.height()) / 2
        self.move(x, y)

    def update_lcd(self):
        self.lcd.display(datetime.datetime.now().time().strftime("%H:%M:%S"))

    def btn_date_dialog_click(self):
        CalendarDialog.getDate(self)

class CalendarDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.btn_ok = QtWidgets.QPushButton("OK")
        self.btn_cancel = QtWidgets.QPushButton("Cancel")
        self.cal = QtWidgets.QCalendarWidget()

        self.h_box = QtWidgets.QHBoxLayout()
        self.v_box = QtWidgets.QVBoxLayout()

    def set_up(self):
        self.setWindowTitle("Choice date")

        self.h_box.addWidget(self.btn_cancel)
        self.h_box.addWidget(self.btn_ok)

        self.v_box.addWidget(self.cal)
        self.v_box.addLayout(self.h_box)

        self.setLayout(self.v_box)

    def showEvent(self, event):
        center = QtWidgets.QApplication.desktop().availableGeometry()
        x = (center.width() - self.width()) / 2
        y = (center.height() - self.height()) / 2

        self.move(x, y)

    @staticmethod
    def getDate(parent, today=""):
        QtWidgets.QInputDialog
        dialog = CalendarDialog(parent)
        dialog.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())