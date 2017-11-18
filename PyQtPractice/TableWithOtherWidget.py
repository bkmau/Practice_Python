import sys
import random
import datetime
from PyQt5 import QtWidgets, QtGui, QtCore

class MyApp(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.table = QtWidgets.QTableWidget()

        self.data = [
            ["F", "Angel", "19911022", "Actress", "20000"],
            ["M", "Tom", "19890121", "Worker", "21000"],
            ["M", "Johnson", "19910915", "Chef", "29000"],
            ["F", "Jane", "19900812", "Doctor", "32000"]
        ]

        self.jobs = ["Worker", "Famer", "Doctor", "Lawyer", "Soldier", "Actress", "Chef"]

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

        self.table.setColumnCount(5)
        self.table.setRowCount(1)
        self.table.horizontalHeader().setDefaultSectionSize(120)
        self.table.verticalHeader().setDefaultSectionSize(36)

        self.table.setItem(0, 0, QtWidgets.QTableWidgetItem("Gender"))
        self.table.setItem(0, 1, QtWidgets.QTableWidgetItem("Name"))
        self.table.setItem(0, 2, QtWidgets.QTableWidgetItem("Birthday"))
        self.table.setItem(0, 3, QtWidgets.QTableWidgetItem("Work"))
        self.table.setItem(0, 4, QtWidgets.QTableWidgetItem("Salary"))

        for info in self.data:
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setCellWidget(row, 0, self.set_gender(info[0]))
            self.table.setItem(row, 1, QtWidgets.QTableWidgetItem(info[1]))
            self.table.setCellWidget(row, 2, self.set_birthday(info[2]))
            self.table.setCellWidget(row, 3, self.set_job(info[3]))
            self.table.setCellWidget(row, 4, self.set_salary(info[4]))

        self.v_box.addWidget(self.table)

        self.setLayout(self.v_box)

    def showEvent(self, event):
        self.resize(800, 600)
        center = QtWidgets.qApp.desktop().availableGeometry()
        x = (center.width() - self.width()) / 2
        y = (center.height() - self.height()) / 2
        self.move(x, y)

    def set_gender(self, value):
        widget = QtWidgets.QWidget()
        h_box = QtWidgets.QHBoxLayout()
        pic = {
            "F": QtGui.QPixmap("icon\\male.ico"),
            "M": QtGui.QPixmap("icon\\female.ico")
        }.get(value)

        lbl = QtWidgets.QLabel()
        lbl.setPixmap(pic)
        h_box.addWidget(lbl)
        h_box.setAlignment(QtCore.Qt.AlignCenter)
        h_box.setContentsMargins(0, 0, 0, 0) # (left, top, right, bottom)
        widget.setLayout(h_box)
        return widget

    def set_birthday(self, value):
        ed = QtWidgets.QDateEdit()
        ed.setDate(datetime.datetime.strptime(value, "%Y%m%d").date())
        ed.setCalendarPopup(True)
        ed.resize(100, 24)
        return ed

    def set_job(self, vale):
        cbo = QtWidgets.QComboBox()
        cbo.addItems(self.jobs)
        cbo.setCurrentIndex(cbo.findText(vale))
        return cbo

    def set_salary(self, value):
        sb = QtWidgets.QSpinBox()
        sb.setPrefix("$ ")
        sb.setRange(0, 999999)
        sb.setValue(int(value))
        return sb


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())