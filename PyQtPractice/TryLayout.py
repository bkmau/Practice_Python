import sys
from PyQt5 import QtCore, QtWidgets


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.menuBar = QtWidgets.QMenuBar()
        self.mainToolBar = QtWidgets.QToolBar()
        self.statusBar = QtWidgets.QStatusBar()

        self.win_left = QtWidgets.QWidget()
        self.init_left_win()
        self.set_up_left_win()

        self.win_right = QtWidgets.QWidget()
        self.init_right_win()
        self.set_up_right_win()

        self.splitter = QtWidgets.QSplitter()

        self.set_up_main_win()

    def init_left_win(self):
        self.lbl_company = QtWidgets.QLabel("Company:")
        self.ed_company = QtWidgets.QLineEdit("Softrument")

        self.lbl_product = QtWidgets.QLabel("Product:")
        self.ed_product = QtWidgets.QLineEdit("WIFI Instrument")

        self.lbl_sn = QtWidgets.QLabel("SerialNumber:")
        self.ed_sn = QtWidgets.QLineEdit("0123456789")

        self.lbl_privilege = QtWidgets.QLabel("Privilege:")
        self.ed_privilege = QtWidgets.QLineEdit("0")

        self.lbl_modules = QtWidgets.QLabel("Modules:")
        self.ed_modules = QtWidgets.QLineEdit("3")

        self.lbl_start_date = QtWidgets.QLabel("StartDate:")
        self.ed_start_date = QtWidgets.QLineEdit()

        self.lbl_due_date = QtWidgets.QLabel("DueDate:")
        self.ed_due_date = QtWidgets.QLineEdit()

        self.lbl_current_date = QtWidgets.QLabel("CurrentDate:")
        self.ed_current_date = QtWidgets.QLineEdit()

        self.h_box_1 = QtWidgets.QHBoxLayout()
        self.h_box_2 = QtWidgets.QHBoxLayout()
        self.h_box_3 = QtWidgets.QHBoxLayout()
        self.h_box_4 = QtWidgets.QHBoxLayout()
        self.h_box_5 = QtWidgets.QHBoxLayout()
        self.h_box_6 = QtWidgets.QHBoxLayout()
        self.h_box_7 = QtWidgets.QHBoxLayout()
        self.h_box_8 = QtWidgets.QHBoxLayout()

        self.v_box_1 = QtWidgets.QVBoxLayout()

    def set_up_left_win(self):
        self.lbl_company.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_company.setMinimumSize(QtCore.QSize(80, 0))
        self.ed_company.setMinimumSize(QtCore.QSize(200, 0))

        self.lbl_product.setMinimumSize(QtCore.QSize(80, 0))
        self.lbl_product.setAlignment(QtCore.Qt.AlignCenter)
        self.ed_product.setMinimumSize(QtCore.QSize(200, 0))

        self.lbl_sn.setMinimumSize(QtCore.QSize(80, 0))
        self.lbl_sn.setAlignment(QtCore.Qt.AlignCenter)
        self.ed_sn.setMinimumSize(QtCore.QSize(200, 0))

        self.lbl_privilege.setMinimumSize(QtCore.QSize(80, 0))
        self.lbl_privilege.setAlignment(QtCore.Qt.AlignCenter)
        self.ed_privilege.setMinimumSize(QtCore.QSize(200, 0))

        self.lbl_modules.setMinimumSize(QtCore.QSize(80, 0))
        self.lbl_modules.setAlignment(QtCore.Qt.AlignCenter)
        self.ed_modules.setMinimumSize(QtCore.QSize(200, 0))

        self.lbl_start_date.setMinimumSize(QtCore.QSize(80, 0))
        self.lbl_start_date.setAlignment(QtCore.Qt.AlignCenter)
        self.ed_start_date.setMinimumSize(QtCore.QSize(200, 0))

        self.lbl_due_date.setMinimumSize(QtCore.QSize(80, 0))
        self.lbl_due_date.setAlignment(QtCore.Qt.AlignCenter)
        self.ed_due_date.setMinimumSize(QtCore.QSize(200, 0))

        self.lbl_current_date.setMinimumSize(QtCore.QSize(80, 0))
        self.lbl_current_date.setAlignment(QtCore.Qt.AlignCenter)
        self.ed_current_date.setMinimumSize(QtCore.QSize(200, 0))

        self.h_box_1.setContentsMargins(11, 11, 11, 11)
        self.h_box_1.setSpacing(6)
        self.h_box_1.addWidget(self.lbl_company)
        self.h_box_1.addWidget(self.ed_company)

        self.h_box_2.setContentsMargins(11, 11, 11, 11)
        self.h_box_2.setSpacing(6)
        self.h_box_2.addWidget(self.lbl_product)
        self.h_box_2.addWidget(self.ed_product)

        self.h_box_3.setContentsMargins(11, 11, 11, 11)
        self.h_box_3.setSpacing(6)
        self.h_box_3.addWidget(self.lbl_sn)
        self.h_box_3.addWidget(self.ed_sn)

        self.h_box_4.setContentsMargins(11, 11, 11, 11)
        self.h_box_4.setSpacing(6)
        self.h_box_4.addWidget(self.lbl_privilege)
        self.h_box_4.addWidget(self.ed_privilege)

        self.h_box_5.setContentsMargins(11, 11, 11, 11)
        self.h_box_5.setSpacing(6)
        self.h_box_5.addWidget(self.lbl_modules)
        self.h_box_5.addWidget(self.ed_modules)

        self.h_box_6.setContentsMargins(11, 11, 11, 11)
        self.h_box_6.setSpacing(6)
        self.h_box_6.addWidget(self.lbl_start_date)
        self.h_box_6.addWidget(self.ed_start_date)

        self.h_box_7.setContentsMargins(11, 11, 11, 11)
        self.h_box_7.setSpacing(6)
        self.h_box_7.addWidget(self.lbl_due_date)
        self.h_box_7.addWidget(self.ed_due_date)

        self.h_box_8.setContentsMargins(11, 11, 11, 11)
        self.h_box_8.setSpacing(6)
        self.h_box_8.addWidget(self.lbl_current_date)
        self.h_box_8.addWidget(self.ed_current_date)

        self.v_box_1.setContentsMargins(11, 11, 11, 11)
        self.v_box_1.setSpacing(6)
        self.v_box_1.addLayout(self.h_box_1)
        self.v_box_1.addLayout(self.h_box_2)
        self.v_box_1.addLayout(self.h_box_3)
        self.v_box_1.addLayout(self.h_box_4)
        self.v_box_1.addLayout(self.h_box_5)
        self.v_box_1.addLayout(self.h_box_6)
        self.v_box_1.addLayout(self.h_box_7)
        self.v_box_1.addLayout(self.h_box_8)

    def init_right_win(self):
        self.btn_preview = QtWidgets.QPushButton("Preview")
        self.ed_preview = QtWidgets.QTextBrowser()

        self.btn_encrypt = QtWidgets.QPushButton("Encrypt")
        self.ed_ciphertext = QtWidgets.QTextBrowser()

        self.btn_decrypt = QtWidgets.QPushButton("Decrypt")
        self.ed_recovertext = QtWidgets.QTextBrowser()

        self.h_box_9 = QtWidgets.QHBoxLayout()
        self.h_box_10 = QtWidgets.QHBoxLayout()
        self.h_box_11 = QtWidgets.QHBoxLayout()

        self.v_box_2 = QtWidgets.QVBoxLayout()

    def set_up_right_win(self):
        self.h_box_9.setContentsMargins(11, 11, 11, 11)
        self.h_box_9.setSpacing(6)
        self.h_box_9.addWidget(self.btn_preview)
        self.h_box_9.addItem(QtWidgets.QSpacerItem(
            308, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        
        self.h_box_10.setContentsMargins(11, 11, 11, 11)
        self.h_box_10.setSpacing(6)
        self.h_box_10.addWidget(self.btn_encrypt)
        self.h_box_10.addItem(QtWidgets.QSpacerItem(
            308, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        
        self.h_box_11.setContentsMargins(11, 11, 11, 11)
        self.h_box_11.setSpacing(6)
        self.h_box_11.addWidget(self.btn_decrypt)
        self.h_box_11.addItem(QtWidgets.QSpacerItem(
            308, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))

        self.v_box_2.setContentsMargins(11, 11, 11, 11)
        self.v_box_2.setSpacing(6)
        self.v_box_2.addLayout(self.h_box_9)
        self.v_box_2.addWidget(self.ed_preview)
        self.v_box_2.addLayout(self.h_box_10)
        self.v_box_2.addWidget(self.ed_ciphertext)
        self.v_box_2.addLayout(self.h_box_11)
        self.v_box_2.addWidget(self.ed_recovertext)

    def set_up_main_win(self):
        self.setWindowTitle("LicenseSystem")
        self.resize(890, 614)
        self.setMinimumSize(QtCore.QSize(800, 600))
        self.setMenuBar(self.menuBar)
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.setStatusBar(self.statusBar)

        self.menuBar.setGeometry(QtCore.QRect(0, 0, 890, 23))

        self.win_left.setLayout(self.v_box_1)
        self.win_right.setLayout(self.v_box_2)
        
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setStyleSheet("QSplitter::handle{background:black}")
        self.splitter.setHandleWidth(4)
        self.splitter.addWidget(self.win_left)
        self.splitter.addWidget(self.win_right)
        self.setCentralWidget(self.splitter)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
