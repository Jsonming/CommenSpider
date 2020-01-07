#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/6 18:03
# @Author  : yangmingming
# @Site    : 
# @File    : webkit_learn.py
# @Software: PyCharm
# coding: utf-8

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebKitWidgets import *


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("client")
        self.setWindowIcon(QIcon('icons/icon.png'))
        self.resize(900, 600)
        self.show()

        self.browser = QWebView()
        url = 'https://www.baidu.com'
        self.browser.load(QUrl(url))
        self.setCentralWidget(self.browser)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
