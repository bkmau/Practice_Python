import sys
import os
import random
import csv
from PyQt5 import QtWidgets, QtGui, QtCore

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.file_name = ""

        self.table = MyTable(2, 2)

        self.file = self.menuBar().addMenu("File")

        self.new_action = QtWidgets.QAction("&New", self)
        self.new_action.setIcon(QtGui.QIcon("icon\\page.ico"))

        self.open_action = QtWidgets.QAction("&Open", self)
        self.open_action.setIcon(QtGui.QIcon("icon\\folder.ico"))

        self.save_action = QtWidgets.QAction("&Save", self)
        self.save_action.setIcon(QtGui.QIcon("icon\\disk.ico"))

        self.save_as_action = QtWidgets.QAction("&Save As", self)
        self.save_as_action.setIcon(QtGui.QIcon("icon\\file_save_as.ico"))

        self.quit_action = QtWidgets.QAction("&Quit", self)
        self.quit_action.setIcon(QtGui.QIcon("icon\\exclamation.ico"))

        self.set_up()
        self.show()

    def set_up(self):
        self.setFont(QtGui.QFont("Arial", 12))
        self.setWindowTitle("Hello Word!")
        self.setGeometry(100, 100, 600, 300)
        if random.randint(0, 9) % 2 == 0:
            self.setWindowIcon(QtGui.QIcon("icon\\chameleon.ico"))
        else:
            self.setWindowIcon(QtGui.QIcon("icon\\aol_mail.ico"))
        self.setCentralWidget(self.table)

        self.table.set_header_label()
        self.table.setCurrentCell(1, 1)
        self.table.setItem(1, 1, QtWidgets.QTableWidgetItem("80"))

        self.new_action.setShortcut("Ctrl+N")
        self.new_action.triggered.connect(self.new_trigger)

        self.open_action.setShortcut("Ctrl+O")
        self.open_action.triggered.connect(self.open_trigger)

        self.save_action.setShortcut("Ctrl+S")
        self.save_action.triggered.connect(self.save_trigger)

        self.save_as_action.setShortcut("Ctrl+Shift+S")
        self.save_as_action.triggered.connect(self.save_as_trigger)

        self.quit_action.setShortcut("Ctrl+Q")
        self.quit_action.triggered.connect(self.quit_trigger)

        self.file.addAction(self.new_action)
        self.file.addAction(self.open_action)
        self.file.addAction(self.save_action)
        self.file.addAction(self.save_as_action)
        self.file.addAction(self.quit_action)
        self.file.triggered.connect(self.selected_trigger)

    def new_trigger(self):
        self.file_name = "" if self.file_name else ""
        self.table.clear()

    def open_trigger(self):
        name = QtWidgets.QFileDialog.getOpenFileName(
            self, "Open File", os.getenv("HOME"), "CSV(*.csv)")
        if name[0]:
            self.file_name = name[0]
            self.table.load_from_csv(self.file_name)

    def save_trigger(self):
        try:
            if self.file_name:
                self.table.save_to_csv(self.file_name)
            else:
                self.save_as_action.trigger()
        except Exception as e:
            print(e)

    def save_as_trigger(self):
        name = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save File", os.getenv("HOME"), "CSV(*.csv);;Html(*.html)")
        if name[0]:
            self.file_name = name[0]
            if os.path.splitext(self.file_name) == ".csv":
                self.table.save_to_csv(self.file_name)
            else:
                self.table.save_to_html(self.file_name)

    def quit_trigger(self):
        QtWidgets.qApp.quit()

    def selected_trigger(self, q):
        print("{} selected".format(q.text()))

class MyTable(QtWidgets.QTableWidget):
    def __init__(self, row_num, col_num):
        super().__init__(row_num, col_num)

        self.set_up()

    def set_up(self):
        self.cellChanged.connect(self.cell_change)

    def cell_change(self):
        print("Current cell is ({}, {}) Value is {}".format(
            (self.currentRow() + 1), (self.currentColumn() + 1),
            self.item(self.currentRow(), self.currentColumn()).text())
        )

    def load_from_csv(self, path):
        try:
            self.cellChanged.disconnect(self.cell_change)
            self.clear()
            with open(path, "r", encoding="UTF-8") as f:
                # reader = csv.reader(f, delimiter=",", quotedchar="|")
                reader = csv.reader(f)

                self.setRowCount(0)
                self.setColumnCount(0)
                for index, row_data in enumerate(reader):
                    row = self.rowCount()
                    self.insertRow(row)
                    if len(row_data) > self.columnCount():
                        self.setColumnCount(len(row_data))
                    for x, data in enumerate(row_data):
                        self.setItem(row, x, QtWidgets.QTableWidgetItem(data))

            self.set_header_label()
        finally:
            self.cellChanged.connect(self.cell_change)

    def save_to_csv(self, path):
        try:
            self.cellChanged.disconnect(self.cell_change)
            with open(path, "w", encoding="UTF-8", newline="") as f:
                writer = csv.writer(f)

                for row in range(self.rowCount()):
                    data = []

                    for column in range(self.columnCount()):
                        if self.item(row, column):
                            data.append(self.item(row, column).text())
                        else:
                            data.append("")

                    writer.writerow(data)
        finally:
            self.cellChanged.connect(self.cell_change)

    def set_header_label(self):
        header = []
        for col in range(self.columnCount()):
            header.append(chr(col + 65))
        if header:
            self.setHorizontalHeaderLabels(header)

    def save_to_html(self, path):
        try:
            self.cellChanged.disconnect(self.cell_change)
            with open(path, "w", encoding="UTF-8", newline="") as f:
                thead = "<td></td>"
                for index in range(self.columnCount()):
                    thead += "<td>{}</td> ".format(self.horizontalHeaderItem(index).text())

                tbody = ""
                for row in range(self.rowCount()):
                    tbody += "<tr> <td>{}</td> ".format(row + 1)
                    for column in range(self.columnCount()):
                        tbody += "<td>{}</td> ".format(self.item(row, column).text() if self.item(row, column) else "")
                    tbody += "</tr> "

                html_text = r'<!DOCTYPE html> <html lang="en"> ' \
                            r'<head> <meta charset="UTF-8"> <title>{}</title>' \
                            r'<style> table {{ border-collapse: collapse; }}' \
                            r'table, th, td {{ border: 1px solid black; }}' \
                            r'td {{ width: 100px; height: 20px; }}' \
                            r'</style> </head> <body> <table> <thead> <tr>' \
                            r'{} </tr> </thead> <tbody> {} </tbody></table>'\
                            r'</body> </html>'.format("Test", thead, tbody)
                f.write(html_text)
        finally:
            self.cellChanged.connect(self.cell_change)


app = QtWidgets.QApplication(sys.argv)
window = MyApp()
sys.exit(app.exec_())