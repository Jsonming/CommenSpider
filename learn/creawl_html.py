#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/7 10:41
# @Author  : yangmingming
# @Site    : 
# @File    : creawl_html.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebKitWidgets import *
from lxml.html import etree


class WebRender(QWebPage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.__loadFinished)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def __loadFinished(self, result):
        self.frame = self.mainFrame()
        self.app.quit()


url = "https://www.baidu.com"
r = WebRender(url)
html = r.frame.toHtml()
print(html)
page = etree.HTML(html.encode('utf-8'))
