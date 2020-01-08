#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/7 16:56
# @Author  : yangmingming
# @Site    : 
# @File    : QWidget_help.py
# @Software: PyCharm
import sys

out = sys.stdout
sys.stdout = open("aaa.txt", "a", encoding="utf8")
print("张欣羽")
sys.stdout.close()
sys.stdout = out
