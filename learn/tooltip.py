#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/6 18:46
# @Author  : yangmingming
# @Site    : 
# @File    : tooltip.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication
from PyQt5.QtGui import QFont


class Example(QWidget):
    def __init__(self):
        super().__init__()
        # self.initUI()  # 继承过来一个框

    # def initUI(self):
    #     QToolTip.setFont(QFont("SansSerif", 10))  # 工具提示框并设置字体
    #     self.setToolTip('This is a <b>QWidget</b> widget')  # 创建工具提示框并用富文本的方式设置提示内容
    #
    #     btn = QPushButton('Button', self)  # 创建一个提交按钮
    #     btn.setToolTip('This is a <b>QPushButton</b> widget')
    #     btn.resize(btn.sizeHint())
    #
    #     self.setGeometry(300, 300, 300, 200)
    #     self.setWindowTitle('Tooltips')
    #     self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
