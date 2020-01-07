#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/2 16:21
# @Author  : yangmingming
# @Site    : 
# @File    : frame.py
# @Software: PyCharm
import sys

from PyQt5.QtWidgets import QApplication, QWidget
from CommenSpider.settings import BASE_FRAME_WIDTH, BASE_FRAME_HEIGHT, PAGE_MOVE_HEIGHT, PAGE_MOVE_WIDTH
from CommenSpider.settings import FRAME_NAME


class Frame(object):
    def __init__(self):
        self.height = BASE_FRAME_HEIGHT
        self.width = BASE_FRAME_WIDTH

        self.move_width = PAGE_MOVE_WIDTH
        self.move_heigth = PAGE_MOVE_HEIGHT

        self.name = FRAME_NAME

    def show(self):
        app = QApplication(sys.argv)
        w = QWidget()
        w.resize(self.width, self.height)
        w.move(self.move_width, self.move_heigth)
        w.setWindowTitle(self.name)

        w.setWindowTitle(self.name)
        w.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    f = Frame()
    f.show()
