# -*- coding: utf-8 -*-
# @Time : 2019/7/24 16:28
# @Author : Max
# @FileName: Finder.py
# @IDE: PyCharm
import json


def Finder(dicationary):
    d = dicationary

    # 构造的命令由两部分组成：
    # 1.有占位符的sql查询语句
    # 2.括号内占位符所代表的变量名
    head = 'SELECT * FROM ' + d['logType']
    tail = ""
    keys = list(d)
    data = list(d.values())
    for i in range(0, len(keys)):

        # 跳过名字
        if not i:
            continue

        # 第一个出现的特殊条件用where作为前缀

        if i == 1:
            head += ' WHERE ' + keys[i] + "= '%s'"
            tail += " % (" + data[i]
            continue

        # 其他所有出现的特殊条件都用and作为前缀
        head += ' AND ' + keys[i] + ' = "%s"'
        tail += ', ' + data[i]

    command = head + tail + ')'
    print command


if __name__ == '__main__':
    Finder({'logType': 'mis_clt', 'rrn': '151515151', 'trans': '12122121212', 'qr': '131313313131313'})
