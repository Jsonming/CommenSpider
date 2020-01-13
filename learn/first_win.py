#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/7 17:31
# @Author  : yangmingming
# @Site    : 
# @File    : first_win.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QPushButton, QApplication, QWidget


class WinForm(QWidget):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.setGeometry(300, 300, 350, 350)
        self.setWindowTitle("点击按钮关闭窗口")
        quit = QPushButton("Close", self)
        quit.setStyleSheet("background-color: red")
        quit.clicked.connect(self.close)
        self.close()


if __name__ == '__main__':
    a = sys.argv
    print(a)
    app = QApplication(a)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())
