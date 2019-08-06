# -*- coding: utf-8 -*-
# @Time : 2019/7/23 9:10
# @Author : Max
# @FileName: Configuration.py
# @IDE: PyCharm
import yaml
import codecs
import os
import pprint

doc = None
logType = None
postran_key_words = None
qrcodetran_key_words = None
log_path = None
classified_path = None
db_path = None
finder = None
filters = None


# 初始化关键词列表
def init(fileName = 'LogSpider.yml'):
    print "NOTICE: Initialize Configuration"
    global doc, logType, postran_key_words, qrcodetran_key_words, log_path, classified_path, db_path, finder, filters
    try:
        with codecs.open(fileName, 'r', errors='ignore') as file:
            doc = yaml.safe_load(file)
            # pprint.pprint(doc)
            logType = doc['input']['logtype']
            postran_key_words = doc['input']['postran']['re']
            qrcodetran_key_words = doc['input']['qrcodetran']['re']
            log_path = doc['input']['path']
            classified_path = doc['output']['path']
            db_path = doc['output']['dbpath']
            finder = doc['output']['finder']
            filters = doc['output']['filter']['re']

    except IOError:
        print "ERROR: Configuration file not found."
        exit()

    self_check()


# 获取指定值的正则表达式
def get_re(type):
    return doc['input'][type]['re']


# 配置文件自检
def self_check():
    if not os.path.isdir(log_path):
        print "ERROR: log path's " + log_path + " doesn't exist."
        exit()
    if not os.path.isdir(classified_path):
        print "WARNING: classified log's path " + classified_path + " doesn't exist."
    if not os.path.isfile(db_path):
        print 'ERROR: database path ' + db_path + "doesn't exist."
        exit()


if __name__ == '__main__':
    init('debug.yml')
    self_check()
