# -*- coding: utf-8 -*-
# @Time : 2019/7/24 16:28
# @Author : Max
# @FileName: Finder.py
# @IDE: PyCharm

import sys
import DBMS
import Configuration
from pprint import pprint
from optparse import OptionParser
import Filter


def WriteMsg(str):
    sys.stderr.write(str + '\n')
    sys.stderr.flush()


def Finder(d):
    result = []
    logType = Configuration.doc['input'][d['logType']]
    if 'related' in logType:
        pass
    types = DBMS.getTable(d['logType'])
    for i in range(0, len(types)):
        types[i] = types[i][1]

    # 构造的命令由两部分组成：
    # 1.有占位符的sql查询语句
    # 2.括号内占位符所代表的变量名
    command = 'SELECT * FROM ' + d['logType']
    keys = list(d)
    data = list(d.values())

    # 构造查询语句
    # 判断是否为第一个
    first = True
    for i in range(0, len(keys)):

        # 如果当前key上的value为None，跳过
        if data[i] is None or data[i] == "":
            continue

        # 跳过名字
        if not i:
            continue

        # 第一个出现的特殊条件用where作为前缀
        if i != 0 and first is True:
            command += ' WHERE ' + keys[i] + " = '" + data[i] + "'"
            first = False
            continue

        # 其他所有出现的特殊条件都用and作为前缀
        command += ' AND ' + keys[i] + " = '" + data[i] + "'"

    WriteMsg(command)

    lists = DBMS.search(command)
    for item in lists:
        # 字典key和value匹配
        pack = dict(zip(types, item))
        result.append(pack)
        bbb = DBMS.search_mis_clt(pack["pid"], pack["SendToHost"])
        if bbb:
            result.append(dict(zip(types, bbb)))

    WriteMsg("NOTICE: Search complete, " + str(len(result)) + " eligible items")
    return result


# ---------------------------参数处理------------------------------

parser = OptionParser(usage="usage: %prog [options] filename",
                      version="%prog 1.0")
parser.add_option("-t", "--type",
                  action="store",
                  dest="logType",
                  default='postran',
                  help=u"指定要查询日志的类型", )
parser.add_option("-d", "--date",
                  action="store",
                  dest="FileDate",
                  default=None,
                  help=u"指定要查询日志的日期范围")
parser.add_option("-r", "--rrn",
                  action="store",  # optional because action defaults to "store"
                  dest="rrn",
                  default=None,
                  help=u"指定要查询日志的Rrn", )
parser.add_option("-a", "--amount",
                  action="store",  # optional because action defaults to "store"
                  dest="Amount",
                  default=None,
                  help=u"指定要查询日志的金额", )
parser.add_option("-m", "--MrchId",
                  action="store",  # optional because action defaults to "store"
                  dest="MrchId",
                  default=None,
                  help=u"指定要查询日志的MrchId", )
parser.add_option("-c", "--config",
                  action="store",  # optional because action defaults to "store"
                  dest="config",
                  default='LogSpider.yml',
                  help=u"指定调试时的配置文件", )

(options, args) = parser.parse_args()

if __name__ == '__main__':
    Configuration.init(options.config)
    DBMS.init()
    result = Finder(
        {'logType': options.logType, 'FileDate': options.FileDate, 'rrn': options.rrn, 'amount': options.Amount,
         'MrchId': options.MrchId})

    for item in result:
        print(item["path"])

    Filter.Filter(result)