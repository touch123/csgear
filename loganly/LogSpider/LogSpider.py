# -*- coding: utf-8 -*-
# @Time : 2019/7/24 9:04
# @Author : Max
# @FileName: LogSpider.py
# @IDE: PyCharm
import os
import Configuration
import unpacking
import Dealer
import sys


def LogSpider(fileDate=None, logType=Configuration.logType):
    fileList = []
    if fileDate:
        for item in file_names():
            portion = os.path.splitext(item)

            # 将文件名拆成名字和后缀
            if portion[0] in logType and portion[1] == '.' + fileDate:
                fileList.append(portion)
                # print Configuration.log_path + item
                Dealer.classification(Configuration.log_path + '/' + item)

    # 关键字提取
    for name in fileList:
        if name[0] in Configuration.doc['input'] and 'type' in Configuration.doc['input'][name[0]]:
            if name[0] == 'mis_clt':
                result = unpacking.classifying_mis("".join(tuple(name)))
                print result
        else:
            result = unpacking.classifying("".join(tuple(name)))
            print result

        # 可以返回json或则入库


# 遍历文件下下的文件名
def file_names(user_dir=Configuration.log_path):
    file_list = list()
    for root, dirs, files in os.walk(user_dir):
        for file in files:
            file_list.append(file)
            # file_list.append(os.path.join(root, file))
    return file_list


if __name__ == '__main__':
    argv = sys.argv


    argv.index(2)
    LogSpider('20190116', Configuration.logType)
