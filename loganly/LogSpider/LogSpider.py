# -*- coding: utf-8 -*-
# @Time : 2019/7/24 16:28
# @Author : Max
# @FileName: Filter.py
# @IDE: PyCharm

from optparse import OptionParser
import Sensor
import Spider
import Finder
import Filter
import Configuration
import DBMS


def init():
    Configuration.load('debug.yml')
    DBMS.create_table(Configuration.db_path)


def parse_search_string(input_string):
    import re
    rules = {
        'result': u'^[\u4e00-\u9fff]+$',
        'rrn': r'^\d{12}$',
        'FileDate': r'^201[1-9]{1}[0-9]{4}$',
        'amount': r'^([1-9]\d{0,9}|0)(\.\d{1,2})$',
        'orderid': r'^\d{32}$',
        'termid': r'^[A-Za-z0-9]{8}$',
        'MrchId': r'^[0-9]{15}$',
        'pan': '^[0-9]{6}\*+[0-9]{4}$',
    }
    conditions = {}
    input_string = input_string.encode('utf8').decode('utf8')
    str_list = input_string.split(' ')
    for input_str in str_list:
        for key, value in rules.items():
            if re.match(value, input_str):
                conditions[key] = input_str

    return conditions

#aa(u"651232*******2234 20180101 123456789012 12345678901234567890123456789012 123456.78 12MIS001 103050512342342 终端未签到")
#exit(0)

if __name__ == '__main__':
    parser = OptionParser(usage="usage: %prog [options] ",
                          version="%prog 1.0")

    parser.add_option("-i", "--init",
                      action="store_true",
                      dest="init",
                      default=False,
                      help=u"初始化数据库")
    parser.add_option("-s", "--string",
                      action="store",
                      dest="search_string",
                      default="",
                      help=u"搜索字符串")

    (options, args) = parser.parse_args()

    if options.init:
        init()
        exit(0)

    Configuration.load('debug.yml')
    DBMS.create_table(Configuration.db_path)
    Sensor.sensor('20140715')
    Spider.spider(file_date='20140715', log_type='postran')

    conditions = parse_search_string(options.search_string)

    conditions["logType"] = 'postran'
    finder_result = Finder.finder(conditions)

    #finder_result = Finder.finder({'logType': 'postran', 'FileDate': '20140715', 'rrn': '141960021923', 'amount': '',
    #                               'MrchId': ''})

    Filter.filter_by_call(finder_result)


