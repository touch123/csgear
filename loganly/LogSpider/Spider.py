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

parser = OptionParser(usage="usage: %prog [options] filename",
                      version="%prog 1.0")
parser.add_option("-c", "--comfig",
                  action="store",
                  dest="config",
                  default="LogSpider.yml",
                  help=u"指定配置文件名", )
parser.add_option("-d", "--date",
                  action="store_true",
                  dest="FileDate",
                  default=False,
                  help=u"指定Spider处理的日志的日期范围")
parser.add_option("-t", "--type",
                  action="store_true",  # optional because action defaults to "store"
                  dest="LogType",
                  default=False,
                  help=u"指定Spider处理的日志的类型", )
(options, args) = parser.parse_args()


def Spider(fileDate=None, logType=Configuration.logType):
    # 将文件名拆成名字和后缀
    fileList = []

    for type in logType:
        if fileDate:
            if os.path.isfile(Configuration.log_path + '/' + type + '/' + type + '.' + fileDate):
                Dealer.classification(Configuration.log_path + '/' + type + '/' + type + '.' + fileDate)
                fileList.append((type, fileDate))
            else:
                print "ERROR: file" + Configuration.log_path + '/' + type + '/' + type + '.' + fileDate + " don't exist."
        else:
            for item in Configuration.log_path + '/' + type:
                print item


    # 关键字提取
    for name in fileList:
        if name[0] in Configuration.doc['input'] and 'type' in Configuration.doc['input'][name[0]]:
            if name[0] == 'mis_clt':
                result = unpacking.classifying_mis("".join(tuple(name)))
                # print result
        else:
            result = unpacking.classifying("".join(tuple(name)))
            # print result

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


if __name__ == '__main__':
    Configuration.init(options.config)
    DBMS.init()
    Spider(fileDate='20190116', logType=Configuration.logType)
    DBMS.logout()
