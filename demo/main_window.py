#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/6 18:14
# @Author  : yangmingming
# @Site    : 
# @File    : mainwindow.py
# @Software: PyCharm
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebKitWidgets import *

from CommenSpider.settings import BASE_FRAME_WIDTH, BASE_FRAME_HEIGHT
from CommenSpider.settings import FRAME_NAME


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle(FRAME_NAME)
        self.setWindowIcon(QIcon('通用爬虫图标.png'))
        self.resize(BASE_FRAME_WIDTH, BASE_FRAME_HEIGHT)
        self.show()

        self.browser = QWebView()
        default_url = 'https://www.baidu.com'
        self.browser.load(QUrl(default_url))
        self.setCentralWidget(self.browser)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
