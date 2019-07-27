# -*- coding: utf-8 -*-
# @Time : 2019/7/24 16:28
# @Author : Max
# @FileName: Finder.py
# @IDE: PyCharm
import DBMS
import sys
import pprint
import json


def Finder(dicationary):

    d = dicationary
    result = []
    types = DBMS.getTable(d['logType'])
    # 构造的命令由两部分组成：
    # 1.有占位符的sql查询语句
    # 2.括号内占位符所代表的变量名
    command = 'SELECT * FROM ' + d['logType']
    keys = list(d)
    data = list(d.values())
    for i in range(0, len(keys)):

        # 跳过名字
        if not i:
            continue

        # 第一个出现的特殊条件用where作为前缀

        if i == 1:
            command += ' WHERE ' + keys[i] + " = '" + data[i] + "'"
            continue

        # 其他所有出现的特殊条件都用and作为前缀
        command += ' AND ' + keys[i] + " = '" + data[i] + "'"
    print command

    for item in DBMS.sreach(command):
        result.append(json.dumps(dict(zip(types, list(item)))))

    pprint.pprint(result)


def deal():
    print len(sys.argv)
    print u'参数个数为:', len(sys.argv), u'个参数。'
    print u'参数列表:', str(sys.argv)
    for item in sys.argv:
        pass

if __name__ == '__main__':

    Finder({'logType': 'mis_clt', 'FileDate': '20190116', 'TraceNo': '540002'})
