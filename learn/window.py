#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/19 17:58
# @Author  : yangmingming
# @Site    : 
# @File    : window.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(1300, 900)
    w.move(300, 50)
    w.setWindowTitle("通用爬虫系统")
    w.show()
    sys.exit(app.exec_())