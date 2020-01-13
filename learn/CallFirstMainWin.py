#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/10 17:04
# @Author  : yangmingming
# @Site    : 
# @File    : CallFirstMainWin.py
# @Software: PyCharm
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from learn.firstMainWin import *


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)

 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
