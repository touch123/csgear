# -*- coding: utf-8 -*-
# @Time : 2019/7/24 16:28
# @Author : Max
# @FileName: Finder.py
# @IDE: PyCharm

import sys

import DBMS
import Configuration
from optparse import OptionParser
import Filter


def write_msg(msg):
    sys.stderr.write(msg + '\n')
    sys.stderr.flush()


def finder(conditions):
    DBMS.connect(Configuration.db_path)

    log_type = Configuration.doc['input'][conditions['logType']]
    if 'related' in log_type:
        pass
    types = DBMS.getTable(conditions['logType'])
    for i in range(0, len(types)):
        types[i] = types[i][1]

    # 构造的命令由两部分组成：
    # 1.有占位符的sql查询语句
    # 2.括号内占位符所代表的变量名
    command = 'SELECT * FROM ' + conditions['logType']
    keys = list(conditions)
    data = list(conditions.values())

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

    write_msg(command)

    lists = DBMS.search(command)
    result = []

    for item in lists:
        # 字典key和value匹配
        pack = dict(zip(types, item))
        result.append(pack)
        bbb = DBMS.search_mis_clt(pack["pid"], pack.get("SendToHost",""))
        if bbb:
            result.append(dict(zip(types, bbb)))

    write_msg("NOTICE: Search complete, " + str(len(result)) + " eligible items")
    DBMS.disconnect()


    return result


# ---------------------------参数处理------------------------------


if __name__ == '__main__':
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
    Configuration.load(options.config)
    finder_result = finder(
        {'logType': options.logType, 'FileDate': options.FileDate, 'rrn': options.rrn, 'amount': options.Amount,
         'MrchId': options.MrchId})

    for f_item in finder_result:
        print(f_item["path"])

    Filter.filter_by_call(finder_result)
