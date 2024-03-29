# -*- coding: utf-8 -*-
# @Time : 2019/7/24 9:04
# @Author : Max
# @FileName: LogSpider.py
# @IDE: PyCharm

import os
from optparse import OptionParser
import datetime

import Configuration
import DBMS
import unpacking_general
import Dealer


def spider(file_date=None, log_type=Configuration.logType):
    '''
    TODO: 用Configuration.logType 作参数不合适
    '''

    if not DBMS.connect(Configuration.db_path): return False
    # 将文件名拆成名字和后缀
    file_list = []


    if isinstance(log_type,str) :
        print(log_type,Configuration.logType)
        if log_type not in Configuration.logType:
            return False
        log_type = [log_type]

    for t in log_type:
        if file_date:
            if os.path.isfile(Configuration.log_path + t + '/' + t + '.' + file_date):
                Dealer.classification(Configuration.log_path + t + '/' + t + '.' + file_date)
                file_list.append((t, '.' + file_date))
            else:
                print "ERROR: file " + Configuration.log_path + t + '/' + t + '.' + file_date + " don't exist."

    # 关键字提取
    result = None
    for name in file_list:
        if name[0] in Configuration.doc['input'] and 'type' in Configuration.doc['input'][name[0]]:
            if name[0] == 'mis_clt':
                result = unpacking_general.classifying_mis("".join(tuple(name)))
        else:
            result = unpacking_general.classifying("".join(tuple(name)))

        # 可以返回json或则入库
        DBMS.delete_table(name[0])
        DBMS.insert_dict_into_sql(name[0], result)
    DBMS.disconnect()
    return True


# 遍历文件下下的文件名
def file_names(user_dir):
    file_list = list()

    for root, dirs, files in os.walk(user_dir):
        for logfile in files:
            file_list.append(logfile)
            # file_list.append(os.path.join(root, file))
    return file_list


# 获取前1天或N天的日期，beforeOfDay=1：前1天；beforeOfDay=N：前N天
def getdate(before_of_day=1):
    if not isinstance(before_of_day, int): return datetime.datetime.now().strftime('%Y%m%d')

    today = datetime.datetime.now()
    # 计算偏移量
    offset = datetime.timedelta(days=-before_of_day)
    # 获取想要的日期的时间
    re_date = (today + offset).strftime('%Y%m%d')
    return re_date


# ---------------------------参数处理------------------------------
if __name__ == '__main__':
    parser = OptionParser(usage="usage: %prog [options] filename",
                          version="%prog 1.0")
    parser.add_option("-c", "--config",
                      action="store",
                      dest="config",
                      default="LogSpider.yml",
                      help=u"指定配置文件名", )
    parser.add_option("-d", "--date",
                      action="store",
                      dest="FileDate",
                      default=getdate(1),
                      help=u"指定Spider处理的日志的日期范围")
    parser.add_option("-t", "--type",
                      action="store",  # optional because action defaults to "store"
                      dest="LogType",
                      default=['postran', 'mis_clt'],
                      help=u"指定Spider处理的日志的类型", )
    (options, args) = parser.parse_args()
    Configuration.load(options.config)
    spider(file_date=options.FileDate, log_type=options.LogType)


