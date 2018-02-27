import sys
import random
from PyQt5 import QtCore, QtWidgets, QtGui

class MyApp(QtWidgets.QMainWindow):
# class MyApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.splitter_h = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        self.splitter_v = QtWidgets.QSplitter(QtCore.Qt.Vertical)

        self.frm_left = QtWidgets.QFrame()
        self.frm_right = QtWidgets.QFrame()

        self.v_box = QtWidgets.QVBoxLayout()

        self.ed_1 = QtWidgets.QTextEdit()
        self.ed_2 = QtWidgets.QTextEdit()
        self.ed_3 = QtWidgets.QTextEdit()
        self.table = QtWidgets.QTableWidget()

        self.btn = QtWidgets.QPushButton()

        self.set_up()

    def set_up(self):
        self.setFont(QtGui.QFont("Arial", 12))
        self.setWindowTitle("Hello Word!")
        icons = {
            0: QtGui.QIcon("icon\\chameleon.ico"),
            1: QtGui.QIcon("icon\\aol_mail.ico"),
            2: QtGui.QIcon("icon\\emotion_darth_wader.ico")
        }

        self.setWindowIcon(icons.get((random.randint(0, 9) % 3)))

        self.splitter_v.setHandleWidth(1)
        self.splitter_v.addWidget(self.ed_1)
        self.splitter_v.addWidget(self.ed_2)

        self.table.setColumnCount(1)
        self.table.setRowCount(1)
        self.splitter_v.addWidget(self.table)

        self.splitter_v.setStretchFactor(self.splitter_v.indexOf(self.ed_2), 1)

        self.v_box.addWidget(self.splitter_v)

        self.frm_right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_right.resize(560, self.height())
        # self.frm_right.setMinimumWidth(200) # 有設MinimumWidth的話一但縮放超過, setStretchFactor會失去效用
        # self.frm_right.setMaximumWidth(600) # 有設MaximumWidth的話一但縮放超過, setStretchFactor會失去效用
        self.frm_right.setLayout(self.v_box)
        self.frm_right.setMouseTracking(True)
        self.frm_right.installEventFilter(self)

        self.frm_left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_left.resize(800 - self.frm_right.width(), self.height())
        # self.frm_left.setMinimumWidth(200)  # 有設MinimumWidth的話一但縮放超過, setStretchFactor會失去效用
        # self.frm_right.setMaximumWidth(600) # 有設MaximumWidth的話一但縮放超過, setStretchFactor會失去效用
        self.frm_left.setMouseTracking(True)
        self.frm_left.installEventFilter(self)

        self.splitter_h.setHandleWidth(1)
        self.splitter_h.setOpaqueResize(False)

        self.splitter_h.addWidget(self.frm_left)
        self.splitter_h.addWidget(self.frm_right)

        # 是哪一個元件為縮放元件, 但是縮放到某一定的程度還是會失效
        # self.splitter_h.setStretchFactor(self.splitter_h.indexOf(self.frm_right), 1)
        self.splitter_h.setStretchFactor(self.splitter_h.indexOf(self.frm_left), 1)
        self.splitter_h.splitterMoved.connect(self.splitter_h_move)

        self.btn.setFixedSize(13, 42)
        self.btn.setIconSize(self.btn.size())
        self.btn.setParent(self.frm_left)
        self.set_btn_icon()
        self.btn.clicked.connect(self.btn_click)

        self.setCentralWidget(self.splitter_h)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.MouseMove:

            mouseMove = QtGui.QMouseEvent(event)

            rect = self.btn.frameGeometry()

            self.show_hide_btn()

            if self.frm_left.width():
                if rect.contains(mouseMove.pos()):
                    self.btn.show()
                else:
                    self.btn.hide()

        return QtCore.QObject.eventFilter(self, obj, event)

    def showEvent(self, event):
        self.resize(800, 600)
        center = QtWidgets.QApplication.desktop().availableGeometry()
        x = (center.width() - self.width()) / 2
        y = (center.height() - self.height()) / 2
        self.move(x, y)
        self.set_btn_pos()

    def set_btn_icon(self):
        self.btn.setIcon({
                0: QtGui.QIcon("icon\\arrow_left_black.ico"),
                1: QtGui.QIcon("icon\\arrow_right_black.ico")
            }.get(1 if self.frm_left.width() == 0 else 0)
        )

    def set_btn_pos(self):
        self.btn.move(
            (0 if not self.frm_left.width() else self.frm_left.width() - self.btn.width()),
            ((self.frm_left.geometry().height() - self.btn.height()) / 2)
        )

    def btn_click(self):
        self.splitter_h.setSizes([560, 240])
        self.set_btn_pos()

    def splitter_h_move(self, pos, index):
        self.set_btn_pos()
        self.set_btn_icon()
        self.show_hide_btn()

    def show_hide_btn(self):
        if self.frm_left.width():
            self.btn.hide()
        else:
            self.btn.show()
        pass

    def resizeEvent(self, *args, **kwargs):
        self.set_btn_pos()
        self.set_btn_icon()
        self.show_hide_btn()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())