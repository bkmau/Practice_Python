import sys
import random
from PyQt5 import QtWidgets, QtGui


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.file = self.menuBar().addMenu("File")
        self.edit = self.menuBar().addMenu("Edit")
        self.find = self.edit.addMenu("Find")

        self.new_action = QtWidgets.QAction("&New", self)
        self.save_action = QtWidgets.QAction("&Save", self)
        self.quit_action = QtWidgets.QAction("&Quit", self)

        self.find_action = QtWidgets.QAction("&Find", self)
        self.replace_action = QtWidgets.QAction(" &Replace", self)

        self.set_up()
        self.show()

    def set_up(self):
        self.setFont(QtGui.QFont("Arial", 12))
        self.setWindowTitle("Hello Word!")
        self.setGeometry(100, 100, 300, 200)

        self.new_action.setShortcut("Ctrl+N")
        self.save_action.setShortcut("Ctrl+S")
        self.quit_action.setShortcut("Ctrl+Q")
        self.quit_action.triggered.connect(self.quit_trigger)

        self.file.addAction(self.new_action)
        self.file.addAction(self.save_action)
        self.file.addAction(self.quit_action)
        self.file.triggered.connect(self.selected_trigger)

        self.find_action.setShortcut("Ctrl+F")
        self.replace_action.setShortcut("Ctrl+R")

        self.find.addAction(self.find_action)
        self.find.addAction(self.replace_action)
        self.edit.addMenu(self.find)
        self.edit.triggered.connect(self.selected_trigger)

    def quit_trigger(self):
        QtWidgets.qApp.quit()

    def selected_trigger(self, q):
        print("{} selected".format(q.text()))


app = QtWidgets.QApplication(sys.argv)
window = MyApp()
sys.exit(app.exec_())