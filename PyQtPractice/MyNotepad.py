import sys
import os
import random
from PyQt5 import QtWidgets, QtGui, QtCore, QtPrintSupport

'''
ref:
  ICONs come from http://www.fatcow.com/free-icons
  Building a text editor with PyQt: Part 1
    http://www.binpress.com/tutorial/building-a-text-editor-with-pyqt-part-one/143
'''

class MySearchBox(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.lbl_1 = QtWidgets.QLabel("Find:")
        self.ed_1 = QtWidgets.QLineEdit()
        self.ed_1.setText("word")

        self.btn_find = QtWidgets.QPushButton("Find")
        self.btn_previous = QtWidgets.QPushButton("Find Previous")

        self.v_box = QtWidgets.QVBoxLayout()
        self.v_box = QtWidgets.QVBoxLayout()
        self.h_box_1 = QtWidgets.QHBoxLayout()
        self.h_box_2 = QtWidgets.QHBoxLayout()

        self.matchs = []

        self.set_up()

    def set_up(self):
        self.h_box_1.addWidget(self.lbl_1)
        self.h_box_1.addWidget(self.ed_1)

        self.btn_find.setObjectName("find_btn")
        self.btn_find.clicked.connect(self.btn_click)

        self.btn_previous.setObjectName("previous_btn")
        self.btn_previous.clicked.connect(self.btn_click)

        self.h_box_2.addWidget(self.btn_find)
        self.h_box_2.addWidget(self.btn_previous)

        self.v_box.addLayout(self.h_box_1)
        self.v_box.addLayout(self.h_box_2)

        self.setLayout(self.v_box)

    def btn_click(self):
        if self.sender().objectName() == "find_btn":
            self.highlight_word(True)
            print(self.matchs)
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

        self.btn_replace = QtWidgets.QPushButton("Replace")
        self.btn_replace_all = QtWidgets.QPushButton("Replace All")

        self.matchs = []

        self.set_up()

    def set_up(self):
        try:
            self.h_box.addWidget(self.btn_find)
            self.h_box.addWidget(self.btn_previous)
            # self.h_box.addWidget(self.btn_replace)
            # self.h_box.addWidget(self.btn_replace_all)

            self.v_box.addWidget(self.ed_1)
            self.v_box.addWidget(self.ed_2)
            self.v_box.addLayout(self.h_box)

            self.setLayout(self.v_box)
        except Exception as e:
            print(e)

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.text = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text)

        self.file_name = ""

        self.status_bar = self.statusBar()

        self.init_action()

        self.init_menu_bar()

        self.init_tool_bar()

        self.init_format_bar()

        self.set_up()

    def init_action(self):
        self.act_new = QtWidgets.QAction(QtGui.QIcon("icon\\page.ico"), "&New", self)
        self.act_new.setStatusTip("Create a new document from scratch.")
        self.act_new.setShortcut("Ctrl+N")
        self.act_new.triggered.connect(self.new_trigger)

        self.act_open = QtWidgets.QAction(QtGui.QIcon("icon\\folder.ico"), "&Open file", self)
        self.act_open.setStatusTip("Open existing document")
        self.act_open.setShortcut("Ctrl+O")
        self.act_open.triggered.connect(self.open_trigger)

        self.act_save = QtWidgets.QAction(QtGui.QIcon("icon\\disk.ico"), "&Save", self)
        self.act_save.setStatusTip("Save document")
        self.act_save.setShortcut("Ctrl+S")
        self.act_save.triggered.connect(self.save_trigger)

        self.act_save_as = QtWidgets.QAction(QtGui.QIcon("icon\\file_save_as.ico"), "Save As", self)
        self.act_save_as.setStatusTip("Save document")
        self.act_save_as.setShortcut("Ctrl+Shift+S")
        self.act_save_as.triggered.connect(self.save_as_trigger)

        self.act_print = QtWidgets.QAction(QtGui.QIcon("icon\\printer.ico"), "&Print document", self)
        self.act_print.setStatusTip("Print document")
        self.act_print.setShortcut("Ctrl+P")
        self.act_print.triggered.connect(self.print_trigger)

        self.act_preview = QtWidgets.QAction(QtGui.QIcon("icon\\preview.ico"), "Page view", self)
        self.act_preview.setStatusTip("Preview page before printing")
        self.act_preview.setShortcut("Ctrl+Shift+P")
        self.act_preview.triggered.connect(self.preview_trigger)

        self.act_quit = QtWidgets.QAction(QtGui.QIcon("icon\\exclamation.ico"), "&Quit", self)
        self.act_preview.setStatusTip("Close Program")
        self.act_quit.setShortcut("Ctrl+Q")
        self.act_quit.triggered.connect(QtCore.QCoreApplication.instance().quit)

        self.act_cut = QtWidgets.QAction(QtGui.QIcon("icon\\cut.ico"), "Cut to clipboard", self)
        self.act_cut.setStatusTip("Delete and copy text to clipboard")
        self.act_cut.setShortcut("Ctrl+X")
        self.act_cut.triggered.connect(self.text.cut)

        self.act_copy = QtWidgets.QAction(QtGui.QIcon("icon\\page_copy.ico"), "Copy to clipboard", self)
        self.act_copy.setStatusTip("Copy text to clipboard")
        self.act_copy.setShortcut("Ctrl+C")
        self.act_copy.triggered.connect(self.text.copy)

        self.act_paste = QtWidgets.QAction(QtGui.QIcon("icon\\page_paste.ico"), "Paste from clipboard", self)
        self.act_paste.setStatusTip("Paste text from clipboard")
        self.act_paste.setShortcut("Ctrl+V")
        self.act_paste.triggered.connect(self.text.paste)

        self.act_undo = QtWidgets.QAction(QtGui.QIcon("icon\\undo.ico"), "&Undo", self)
        self.act_undo.setStatusTip("Undo last action")
        self.act_undo.setShortcut("Ctrl+Z")
        self.act_undo.triggered.connect(self.text.undo)

        self.act_redo = QtWidgets.QAction(QtGui.QIcon("icon\\redo.ico"), "&Redo", self)
        self.act_redo.setStatusTip("Redo last undone thing")
        self.act_redo.setShortcut("Ctrl+Y")
        self.act_redo.triggered.connect(self.text.redo)

        self.act_find = QtWidgets.QAction(QtGui.QIcon("icon\\find.ico"), "&Find", self)
        self.act_find.setStatusTip("Find something in text editor...")
        self.act_find.setShortcut("Ctrl+F")
        self.act_find.triggered.connect(self.find_trigger)

        self.act_replace = QtWidgets.QAction("&Replace", self)
        self.act_preview.setStatusTip("Find and Replace word")
        self.act_replace.setShortcut("Ctrl+R")
        self.act_replace.triggered.connect(self.replace_trigger)

        self.act_font_color = QtWidgets.QAction(QtGui.QIcon("icon\\font_colors.ico"), "Change font color", self)
        self.act_font_color.triggered.connect(self.font_color_trigger)

        self.act_text_highlight = QtWidgets.QAction(QtGui.QIcon("icon\\highlighter_text.ico"), "Change background color", self)
        self.act_text_highlight.triggered.connect(self.text_highlight_trigger)

        self.act_bold = QtWidgets.QAction(QtGui.QIcon("icon\\text_bold.ico"), "Bold", self)
        self.act_bold.triggered.connect(self.bold_trigger)

        self.act_italic = QtWidgets.QAction(QtGui.QIcon("icon\\text_italic.ico"), "Italic", self)
        self.act_italic.triggered.connect(self.italic_trigger)

        self.act_underline = QtWidgets.QAction(QtGui.QIcon("icon\\text_underline.ico"), "Underline", self)
        self.act_underline.triggered.connect(self.underline_trigger)

        self.act_strike = QtWidgets.QAction(QtGui.QIcon("icon\\text_strikethroungh.ico"), "Strike-out", self)
        self.act_strike.triggered.connect(self.strike_trigger)

        self.act_superscript = QtWidgets.QAction(QtGui.QIcon("icon\\font_superscript.ico"), "Superscript", self)
        self.act_superscript.triggered.connect(self.act_superscript_trigger)

        self.act_subscript = QtWidgets.QAction(QtGui.QIcon("icon\\font_subscript.ico"), "Subscript", self)
        self.act_subscript.triggered.connect(self.subscript_trigger)

    def init_menu_bar(self):
        self.mnu_file = self.menuBar().addMenu("File")

        self.mnu_file.addAction(self.act_new)
        self.mnu_file.addAction(self.act_open)
        self.mnu_file.addAction(self.act_save)
        self.mnu_file.addAction(self.act_save_as)
        self.mnu_file.addSeparator()
        self.mnu_file.addAction(self.act_print)
        self.mnu_file.addAction(self.act_preview)
        self.mnu_file.addSeparator()
        self.mnu_file.addAction(self.act_quit)

        self.mnu_edit = self.menuBar().addMenu("Edit")

        self.mnu_edit.addAction(self.act_cut)
        self.mnu_edit.addAction(self.act_copy)
        self.mnu_edit.addAction(self.act_paste)
        self.mnu_edit.addAction(self.act_find)
        self.mnu_edit.addAction(self.act_replace)

        self.mnu_view = self.menuBar().addMenu("View")

        self.mnu_file.triggered.connect(self.selected_trigger)
        self.mnu_edit.triggered.connect(self.selected_trigger)
        self.mnu_view.triggered.connect(self.selected_trigger)

    def init_tool_bar(self):
        self.tool_bar = self.addToolBar("Options")
        self.tool_bar.setMovable(False)
        self.tool_bar.setFloatable(True)

        self.tool_bar.addAction(self.act_new)
        self.tool_bar.addAction(self.act_open)
        self.tool_bar.addAction(self.act_save)
        self.tool_bar.addAction(self.act_save_as)
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(self.act_cut)
        self.tool_bar.addAction(self.act_copy)
        self.tool_bar.addAction(self.act_paste)
        self.tool_bar.addAction(self.act_undo)
        self.tool_bar.addAction(self.act_redo)
        self.tool_bar.addSeparator()
        self.addToolBarBreak()

    def init_format_bar(self):
        self.format_bar = self.addToolBar("Format")
        self.format_bar.setMovable(False)
        self.format_bar.setFloatable(True)

        self.font_box = QtWidgets.QFontComboBox(self)
        self.font_box.currentFontChanged.connect(self.font_change)

        self.font_size_box = QtWidgets.QComboBox(self)
        self.font_size_box.addItems([
            "6", "7", "8", "9", "10", "11", "12", "13", "14", "15",
            "16", "18", "20", "22", "24", "26", "28", "32", "36", "40",
            "44", "48", "54", "60", "66", "72", "80", "88", "96"
        ])
        self.font_size_box.setEditable(True)
        self.font_size_box.activated[str].connect(self.font_size_active)
        self.font_size_box.setMinimumContentsLength(3)
        self.font_size_box.setValidator(QtGui.QIntValidator(1, 120))

        self.format_bar.addWidget(self.font_box)
        self.format_bar.addWidget(self.font_size_box)

        self.format_bar.addSeparator()
        self.format_bar.addAction(self.act_font_color)
        self.format_bar.addAction(self.act_text_highlight)
        self.format_bar.addAction(self.act_bold)
        self.format_bar.addAction(self.act_italic)
        self.format_bar.addAction(self.act_underline)
        self.format_bar.addAction(self.act_strike)
        self.format_bar.addAction(self.act_superscript)
        self.format_bar.addAction(self.act_subscript)

        self.format_bar.addSeparator()

    def set_up(self):
        QtWidgets.qApp.setFont(QtGui.QFont("Arial", 12))
        self.setWindowTitle("Hello Word!")

        icons = {
            0: QtGui.QIcon("icon\\chameleon.ico"),
            1: QtGui.QIcon("icon\\aol_mail.ico"),
            2: QtGui.QIcon("icon\\emotion_darth_wader.ico")
        }
        self.setWindowIcon(icons.get(random.randint(0, 9) % 3))

        self.text.cursorPositionChanged.connect(self.get_current_line_num)

    def new_trigger(self):
        self.text.clear()
        self.file_name = ""

    def open_trigger(self):
        name = QtWidgets.QFileDialog.getOpenFileName(
            self, "Open File", os.getenv("HOME"), "Plain text(*.txt)")

        if name[0]:
            self.file_name = name[0]
            with open(name[0], "r") as f:
                self.text.setText(f.read())

    def save_trigger(self):
        if self.file_name:
            with open(self.file_name, "w", encoding="UTF-8") as f:
                f.write(self.text.toPlainText())
        else:
            self.act_save_as.trigger()

    def save_as_trigger(self):
        name = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save File", os.getenv("HOME"), "Plain text(*.txt)")
        if name[0]:
            self.file_name = name[0]
            with open(self.file_name, "w", encoding="UTF-8") as f:
                f.write(self.edit_area.ed_1.toPlainText())

    def print_trigger(self):
        dialog = QtPrintSupport.QPrintDialog()

        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.text.document().print_(dialog.printer())

    def preview_trigger(self):
        preview = QtPrintSupport.QPrintPreviewDialog()
        preview.paintRequested.connect(lambda p: self.text.print_(p))

        preview.exec_()

    def find_trigger(self):
        search_box = MySearchBox(self)
        search_box.show()

    def replace_trigger(self):
        replace_box = MyReplaceBox(self)
        replace_box.show()

    def selected_trigger(self, q):
        print("{} selected".format(q.text()))

    def get_current_line_num(self):
        cursor = self.text.textCursor()

        self.status_bar.showMessage("Line: {} Column: {}".format(
            (cursor.blockNumber() + 1), cursor.columnNumber()
        ))

    def font_change(self, font):
        self.text.setCurrentFont(font)

    def font_size_active(self, size):
        self.text.setFontPointSize(int(size))

    def font_color_trigger(self):
        color = QtWidgets.QColorDialog.getColor()
        self.text.setTextColor(color)

    def text_highlight_trigger(self):
        color = QtWidgets.QColorDialog.getColor()
        self.text.setTextBackgroundColor(color)

    def bold_trigger(self):
        pass

    def italic_trigger(self):
        pass

    def underline_trigger(self):
        pass

    def strike_trigger(self):
        pass

    def act_superscript_trigger(self):
        pass

    def subscript_trigger(self):
        pass

    def showEvent(self, event):
        font = QtWidgets.qApp.font()
        self.font_box.setCurrentFont(font)
        self.font_size_box.setCurrentIndex(self.font_size_box.findText(str(font.pointSize())))

        self.resize(800, 600)
        center = QtWidgets.QApplication.desktop().availableGeometry()
        x = (center.width() - self.width()) / 2
        y = (center.height() - self.height()) / 2
        self.move(x, y)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
