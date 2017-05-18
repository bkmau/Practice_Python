# Python3 + PyQt 5.8 使用.ui(QML)檔案的方法

## 使用pyuic5<a href="#id4" style="vertical-align: super;font-size: 60%" id="id1">[1]</a>將.ui轉成.py
開啟ternimal, 打入指令:
```bash
c:\> pyuic5 [*.ui] -o [*.py]
```
>PS. 
>pyuic5的路徑: python_install_dir\Scripts\pyuic5
>python_install_dir\Scripts 要加入環境變數(我的電腦->進階系統設定->進階->環境變數->系統變數->PATH)


轉好的python檔
```python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 50, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 130, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 220, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.pushButton_2.setText(_translate("Form", "PushButton"))
        self.pushButton_3.setText(_translate("Form", "PushButton"))
```

對轉換出來的.py加工
```python
import sys

class Ui_Form(QtWidgets.QWidget):
    def __init__(self):
        super(QtWidgets.QWidget, self).__init__() # for python 3.x
        # super().__init__()                      # for python 3.x
        # QtWidgets.QWidget.__init__(self)        # for python 2.x
        self.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_Form()
    window.show()
    sys.exit(app.exec_())
```


## 在python中, 透過uic module<a style="vertical-align: super;font-size: 60%" id="id2">[2]</a>, 動態載入.ui
```python
import sys
from PyQt5 import QtWidgets, uic

class MyApp(QtWidgets.QWidget):
    def __init__(self):
        super(QtWidgets.QWidget, self).__init__()
        self.ui = uic.loadUi("first.ui", self)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
```

## 參考
*  [Using Qt Designer — PyQt 5.8.2 Reference Guide](http://pyqt.sourceforge.net/Docs/PyQt5/designer.html)
    *  <a id="id4">[1]</a> pyuic5 [http://pyqt.sourceforge.net/Docs/PyQt5/designer.html#pyuic5](http://pyqt.sourceforge.net/Docs/PyQt5/designer.html#pyuic5)
    *  <a id="id5">[2]</a> The uic Module [http://pyqt.sourceforge.net/Docs/PyQt5/designer.html#the-uic-module](http://pyqt.sourceforge.net/Docs/PyQt5/designer.html#the-uic-module)


