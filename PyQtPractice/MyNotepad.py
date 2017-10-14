import sys
import os
import random

from PyQt5 import QtWidgets, QtGui, QtCore


class MyNotepad(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ed_1 = QtWidgets.QTextEdit()
        text = """In this text I want to highlight this zzwordyy and only this word.\n""" + \
               """Any other word shouldn't be highlighted"""
        self.ed_1.setText(text)

        self.clear_btn = QtWidgets.QPushButton("Clear")

        self.v_box = QtWidgets.QVBoxLayout()

        self.set_up()

    def set_up(self):
        self.clear_btn.clicked.connect(self.clear_btn_click)

        self.v_box.addWidget(self.ed_1)
        self.v_box.addWidget(self.clear_btn)

        self.setLayout(self.v_box)

    def clear_btn_click(self):
        self.ed_1.clear()


class MySearchBox(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.lbl_1 = QtWidgets.QLabel("Find:")
        self.ed_1 = QtWidgets.QLineEdit()
        self.ed_1.setText("word")

        self.find_btn = QtWidgets.QPushButton("Find")
        self.previous_btn = QtWidgets.QPushButton("Find Previous")

        self.v_box = QtWidgets.QVBoxLayout()
        self.v_box = QtWidgets.QVBoxLayout()
        self.h_box_1 = QtWidgets.QHBoxLayout()
        self.h_box_2 = QtWidgets.QHBoxLayout()

        self.matchs = []

        self.set_up()

    def set_up(self):
        self.h_box_1.addWidget(self.lbl_1)
        self.h_box_1.addWidget(self.ed_1)

        self.find_btn.setObjectName("find_btn")
        self.find_btn.clicked.connect(self.btn_click)

        self.previous_btn.setObjectName("previous_btn")
        self.previous_btn.clicked.connect(self.btn_click)

        self.h_box_2.addWidget(self.find_btn)
        self.h_box_2.addWidget(self.previous_btn)

        self.v_box.addLayout(self.h_box_1)
        self.v_box.addLayout(self.h_box_2)

        self.setLayout(self.v_box)

    def btn_click(self):
        if self.sender().objectName() == "find_btn":
            self.highlight_word(True)
        elif self.sender().objectName() == "previous_btn":
            print("Go Previous")

    def exit_btn_click(self):
        self.highlight_word(False)
        self.hide()
        self.close()

    def highlight_word(self, highlight):
        search_zone = self.parent().edit_area.ed_1
        expression = self.ed_1.text()
        brush = QtGui.QBrush(QtGui.QColor("yellow")) if highlight else QtGui.QBrush(QtCore.Qt.NoBrush)

        if (search_zone.toPlainText() != "") & (expression != ""):
            cursor = search_zone.textCursor()

            font_fmt = QtGui.QTextCharFormat()
            font_fmt.setBackground(brush)

            regex = QtCore.QRegExp(expression)

            pos = 0

            index = regex.indexIn(search_zone.toPlainText(), pos)
            while index != -1:
                self.move_cursor(cursor, index)

                cursor.mergeCharFormat(font_fmt)
                pos = index + regex.matchedLength()
                index = regex.indexIn(search_zone.toPlainText(), pos)

                self.matchs.append((index, pos))

    def move_cursor(self, cursor, position, selected=False):
        cursor.setPosition(position)
        cursor.movePosition(QtGui.QTextCursor.EndOfWord, 1)
        if selected:
            cursor.select(QtGui.QTextCursor.WordUnderCursor)

class MyReplaceBox(MySearchBox):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.lbl_2 = QtWidgets.QLabel("Replace with:")
        self.ed_2 = QtWidgets.QLineEdit()
        self.ed_2.setText("earth")

        self.replace_btn = QtWidgets.QPushButton("Replace")
        self.replace_all_btn = QtWidgets.QPushButton("Replace All")

        self.matchs = []

        self.set_up()

    def set_up(self):
        try:
            self.h_box.addWidget(self.find_btn)
            self.h_box.addWidget(self.previous_btn)
            # self.h_box.addWidget(self.replace_btn)
            # self.h_box.addWidget(self.replace_all_btn)

            self.v_box.addWidget(self.ed_1)
            self.v_box.addWidget(self.ed_2)
            self.v_box.addLayout(self.h_box)

            self.setLayout(self.v_box)
        except Exception as e:
            print(e)

    def highlight_word(self, highlight):
        # search_zone = self.parent().edit_area.ed_1
        # expression = self.ed_1.text()
        # brush = QtGui.QBrush(QtGui.QColor("yellow")) if highlight else QtGui.QBrush(QtCore.Qt.NoBrush)
        #
        # if (search_zone.toPlainText() != "") & (expression != ""):
        #     cursor = search_zone.textCursor()
        #
        #     font_fmt = QtGui.QTextCharFormat()
        #     font_fmt.setBackground(brush)
        #
        #     regex = QtCore.QRegExp(expression)
        #
        #     pos = 0
        #
        #     index = regex.indexIn(search_zone.toPlainText(), pos)
        #     while index != -1:
        #         self.move_cursor(cursor, index)
        #
        #         cursor.mergeCharFormat(font_fmt)
        #         pos = index + regex.matchedLength()
        #         index = regex.indexIn(search_zone.toPlainText(), pos)
        #
        #         self.matchs.append((index, pos))
        pass

    def move_cursor(self, cursor, position, selected=False):
        cursor.setPosition(position)
        cursor.movePosition(QtGui.QTextCursor.EndOfWord, 1)
        if selected:
            cursor.select(QtGui.QTextCursor.WordUnderCursor)

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.file_name = ""

        self.edit_area = MyNotepad()
        self.setCentralWidget(self.edit_area)

        self.file = self.menuBar().addMenu("File")
        self.edit = self.menuBar().addMenu("Edit")

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

        self.find_action = QtWidgets.QAction("&Find", self)
        self.find_action.setIcon(QtGui.QIcon("icon\\find.ico"))

        self.replace_action = QtWidgets.QAction("&Replace", self)

        self.set_up()
        self.show()

    def set_up(self):
        self.setFont(QtGui.QFont("Arial", 12))
        self.setWindowTitle("Hello Word!")

        if random.randint(0, 9) % 2 == 0:
            self.setWindowIcon(QtGui.QIcon("icon\\chameleon.ico"))
        else:
            self.setWindowIcon(QtGui.QIcon("icon\\aol_mail.ico"))
        self.setGeometry(100, 100, 800, 600)

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

        self.find_action.setShortcut("Ctrl+F")
        self.find_action.triggered.connect(self.find_trigger)

        self.replace_action.setShortcut("Ctrl+R")
        self.replace_action.triggered.connect(self.replace_trigger)

        self.edit.addAction(self.find_action)
        self.edit.addAction(self.replace_action)
        self.edit.triggered.connect(self.selected_trigger)

    def new_trigger(self):
        self.edit_area.ed_1.clear()
        self.file_name = "" if self.file_name else ""

    def open_trigger(self):
        name = QtWidgets.QFileDialog.getOpenFileName(
            self, "Open File", os.getenv("HOME"), "Plain text(*.txt);;XML(*.xml);;All(*)")
        if name[0]:
            self.file_name = name[0]
            with open(name[0], "r") as f:
                self.edit_area.ed_1.setText(f.read())

    def save_trigger(self):
        if self.file_name:
            with open(self.file_name, "w", encoding="UTF-8") as f:
                f.write(self.edit_area.ed_1.toPlainText())
        else:
            self.save_as_action.trigger()

    def save_as_trigger(self):
        name = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save File", os.getenv("HOME"), "Plain text(*.txt);;XML(*.xml);;All(*)")
        if name[0]:
            self.file_name = name[0]
            with open(self.file_name, "w", encoding="UTF-8") as f:
                f.write(self.edit_area.ed_1.toPlainText())

    def quit_trigger(self):
        QtWidgets.qApp.quit()

    def find_trigger(self):
        search_box = MySearchBox(self)
        search_box.show()

    def replace_trigger(self):
        replace_box = MyReplaceBox(self)
        replace_box.show()

    def selected_trigger(self, q):
        print("{} selected".format(q.text()))


app = QtWidgets.QApplication(sys.argv)
window = MyApp()
sys.exit(app.exec_())