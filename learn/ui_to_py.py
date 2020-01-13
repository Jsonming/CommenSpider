#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/13 10:48
# @Author  : yangmingming
# @Site    : 
# @File    : ui_to_py.py
# @Software: PyCharm
import os


class UItoPy(object):
    def __init__(self):
        pass

    def ui_to_py(self, path):
        """
        将ui文件转化为py文件
        :param path:
        :return:
        """
        cmd = "pyuic5 -o {pyfile} {uifile}".format(pyfile=path.replace("ui", "py"), uifile=path)
        os.system(cmd)

    def run_main(self, ui_path):
        """
        将ui界面转化为代码
        :param ui_path:
        :return:
        """
        if os.path.isfile(ui_path):
            if ui_path.endswith("ui"):
                self.ui_to_py(ui_path)
            else:
                print("非正确的ui文件")
        elif os.path.isdir(ui_path):
            for path in list_file(ui_path):
                self.ui_to_py(path)
        else:
            print("请输入正确的ui文件或者含有ui文件的文件夹")


def list_file(folder):
    """
        get all file
    :param folder:
    :return:
    """
    file_list = []
    files = os.listdir(folder)
    for file in files:
        file_name = os.path.join(folder + "\\" + file)
        if os.path.isdir(file_name):
            file_list.extend(list_file(file_name))
        else:
            file_list.append(file_name)
    return file_list


if __name__ == '__main__':
    ui_path = r"D:\Workspace\CommenSpider\learn"  # ui 文件或者文件夹 将py文件生成在同级目录
    UIP = UItoPy()
    UIP.run_main(ui_path)
