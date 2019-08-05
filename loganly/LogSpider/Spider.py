# -*- coding: utf-8 -*-
# @Time : 2019/7/24 9:04
# @Author : Max
# @FileName: LogSpider.py
# @IDE: PyCharm
import os
import Configuration
import unpacking
import Dealer
import DBMS
from optparse import OptionParser
import datetime


def Spider(fileDate=None, logType=Configuration.logType):
    # 将文件名拆成名字和后缀
    fileList = []
    if logType is str:
        logType = [logType]

    for type in logType:
        if fileDate:
            if os.path.isfile(Configuration.log_path + type + '/' + type + '.' + fileDate):
                Dealer.classification(Configuration.log_path + type + '/' + type + '.' + fileDate)
                fileList.append((type, '.' + fileDate))
            else:
                print "ERROR: file " + Configuration.log_path + type + '/' + type + '.' + fileDate + " don't exist."

    # 关键字提取
    for name in fileList:
        if name[0] in Configuration.doc['input'] and 'type' in Configuration.doc['input'][name[0]]:
            if name[0] == 'mis_clt':
                result = unpacking.classifying_mis("".join(tuple(name)))
        else:
            result = unpacking.classifying("".join(tuple(name)))

        # 可以返回json或则入库
        DBMS.delete_table(name[0])
        DBMS.insert_dict_into_sql(name[0], result)


# 遍历文件下下的文件名
def file_names(user_dir):
    file_list = list()

    for root, dirs, files in os.walk(user_dir):
        for file in files:
            file_list.append(file)
            # file_list.append(os.path.join(root, file))
    return file_list


# 获取前1天或N天的日期，beforeOfDay=1：前1天；beforeOfDay=N：前N天
def getdate(beforeOfDay):
    today = datetime.datetime.now()
    # 计算偏移量
    offset = datetime.timedelta(days=-beforeOfDay)
    # 获取想要的日期的时间
    re_date = (today + offset).strftime('%Y%m%d')
    return re_date


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
                  default=['postran', 'mis_clt', 'qrcodetran'],
                  help=u"指定Spider处理的日志的类型", )
(options, args) = parser.parse_args()

if __name__ == '__main__':
    Configuration.init(options.config)
    DBMS.init()
    Spider(fileDate=options.FileDate, logType=options.LogType)
    DBMS.logout()
