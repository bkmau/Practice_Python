import sys
import os
import random
from PyQt5 import QtWidgets, QtGui, QtCore

class MyApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.file_name = ""

        self.menu_bar = QtWidgets.QMenuBar()
        self.mnu_file = QtWidgets.QMenu("File")
        self.mnu_act_new = QtWidgets.QAction("&New", self)
        self.mnu_act_open = QtWidgets.QAction("&Open", self)
        self.mnu_act_save = QtWidgets.QAction("&Save", self)
        self.mnu_act_save_as = QtWidgets.QAction("&Save As", self)
        self.mnu_act_quit = QtWidgets.QAction("&Quit", self)

        self.tool_bar = QtWidgets.QToolBar()

        self.tool_act_search = QtWidgets.QAction("Search", self)
        self.tool_act_add = QtWidgets.QAction("Add", self)
        self.tool_act_modify = QtWidgets.QAction("Modify", self)
        self.tool_act_delete = QtWidgets.QAction("Delete", self)
        self.tool_act_accept = QtWidgets.QAction("Accept", self)
        self.tool_act_cancel = QtWidgets.QAction("Cancel", self)
        self.tool_act_first = QtWidgets.QAction("First", self)
        self.tool_act_previous = QtWidgets.QAction("Previous", self)
        self.tool_act_next = QtWidgets.QAction("Next", self)
        self.tool_act_last = QtWidgets.QAction("Last", self)

        self.main_frame = QtWidgets.QFrame()

        self.v_box = QtWidgets.QVBoxLayout()
        self.grid = QtWidgets.QGridLayout()

        self.btn_1 = QtWidgets.QPushButton("hello")
        self.btn_2 = QtWidgets.QPushButton("word")

        self.set_up()
        self.show()

    def set_up(self):
        self.setFont(QtGui.QFont("Arial", 12))
        self.setWindowTitle("Hello Word!")
        self.setGeometry(100, 100, 600, 300)

        icons = {
            0: QtGui.QIcon("icon\\chameleon.ico"),
            1: QtGui.QIcon("icon\\aol_mail.ico"),
            2: QtGui.QIcon("icon\\emotion_darth_wader.ico")
        }

        self.setWindowIcon(icons.get((random.randint(0, 9) % 3)))

        self.set_up_menu_bar()

        self.set_up_tool_bar()

        self.main_frame.setLineWidth(2)
        self.main_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.grid.addWidget(self.btn_1, 2, 0)
        self.grid.addWidget(self.btn_2, 2, 1)

        self.v_box.setMenuBar(self.menu_bar)
        self.v_box.addWidget(self.tool_bar)
        self.v_box.addWidget(self.main_frame)
        self.v_box.addLayout(self.grid)
        self.setLayout(self.v_box)

    def set_up_menu_bar(self):
        self.menu_bar.addMenu(self.mnu_file)

        self.mnu_file.addActions([
            self.mnu_act_new,
            self.mnu_act_open,
            self.mnu_act_save,
            self.mnu_act_save_as,
            self.mnu_act_quit
        ])

        self.mnu_file.triggered.connect(self.selected_trigger)

        self.mnu_act_new.setIcon(QtGui.QIcon("icon\\page.ico"))
        self.mnu_act_new.setShortcut("Ctrl+N")
        self.mnu_act_new.triggered.connect(self.mnu_act_new_trigger)

        self.mnu_act_open.setIcon(QtGui.QIcon("icon\\folder.ico"))
        self.mnu_act_open.setShortcut("Ctrl+O")
        self.mnu_act_open.triggered.connect(self.mnu_act_open_trigger)

        self.mnu_act_save.setIcon(QtGui.QIcon("icon\\disk.ico"))
        self.mnu_act_save.setShortcut("Ctrl+S")
        self.mnu_act_save.triggered.connect(self.mnu_act_save_trigger)

        self.mnu_act_save_as.setIcon(QtGui.QIcon("icon\\file_save_as.ico"))
        self.mnu_act_save_as.setShortcut("Ctrl+Shift+S")
        self.mnu_act_save_as.triggered.connect(self.mnu_act_save_as_trigger)

        self.mnu_act_quit.setIcon(QtGui.QIcon("icon\\exclamation.ico"))
        self.mnu_act_quit.setShortcut("Ctrl+Q")
        self.mnu_act_quit.triggered.connect(lambda: QtWidgets.qApp.quit())

    def set_up_tool_bar(self):
        self.tool_bar.addActions([
            self.tool_act_search,
            self.tool_act_add,
            self.tool_act_modify,
            self.tool_act_delete,
            self.tool_act_accept,
            self.tool_act_cancel,
        ])

        self.tool_bar.addSeparator()

        self.tool_bar.addActions([
            self.tool_act_first,
            self.tool_act_previous,
            self.tool_act_next,
            self.tool_act_last
        ])

        self.tool_act_search.setIcon(QtGui.QIcon("icon\\magnifier.ico"))
        self.tool_act_add.setIcon(QtGui.QIcon("icon\\add.ico"))
        self.tool_act_modify.setIcon(QtGui.QIcon("icon\\pencil.ico"))
        self.tool_act_delete.setIcon(QtGui.QIcon("icon\\delete.ico"))
        self.tool_act_accept.setIcon(QtGui.QIcon("icon\\accept_button.ico"))
        self.tool_act_cancel.setIcon(QtGui.QIcon("icon\\cancel.ico"))
        self.tool_act_first.setIcon(QtGui.QIcon("icon\\first.ico"))
        self.tool_act_previous.setIcon(QtGui.QIcon("icon\\previous.ico"))
        self.tool_act_next.setIcon(QtGui.QIcon("icon\\next.ico"))
        self.tool_act_last.setIcon(QtGui.QIcon("icon\\last.ico"))

    def mnu_act_new_trigger(self):
        self.file_name = "" if self.file_name else ""

    def mnu_act_open_trigger(self):
        pass

    def mnu_act_save_trigger(self):
        pass

    def mnu_act_save_as_trigger(self):
        pass

    def open_trigger(self):
        # name = QtWidgets.QFileDialog.getOpenFileName(
        #     self, "Open File", os.getenv("HOME"), "CSV(*.csv)")
        # if name[0]:
        #     self.file_name = name[0]
        #     self.table.load_from_csv(self.file_name)
        pass

    def save_trigger(self):
        # try:
        #     if self.file_name:
        #         self.table.save_to_csv(self.file_name)
        #     else:
        #         self.save_as_action.trigger()
        # except Exception as e:
        #     print(e)
        pass

    def save_as_trigger(self):
        # name = QtWidgets.QFileDialog.getSaveFileName(
        #     self, "Save File", os.getenv("HOME"), "CSV(*.csv)")
        # if name[0]:
        #     self.file_name = name[0]
        #     self.table.save_to_csv(self.file_name)
        pass

    def selected_trigger(self, q):
        print("{} selected".format(q.text()))


app = QtWidgets.QApplication(sys.argv)
window = MyApp()
sys.exit(app.exec_())