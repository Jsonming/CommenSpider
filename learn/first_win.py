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