# -*- coding: utf-8 -*-
# @Time : 2019/7/23 9:10
# @Author : Max
# @FileName: Configuration.py
# @IDE: PyCharm

import sys
import yaml
import codecs
import os

doc = None
logType = None
postran_key_words = None
qrcodetran_key_words = None
log_path = None
classified_path = None
db_path = None
finder = None
filters = None
translation = None
mis_clt_key_words = None

def WriteMsg(str):
    sys.stderr.write(str+'\n')

# 初始化关键词列表
def load(fileName ='LogSpider.yml'):
    if not fileName: return False
    WriteMsg("NOTICE: Initialize Configuration")
    global doc, logType, postran_key_words, qrcodetran_key_words, mis_clt_key_words, log_path, classified_path, db_path, finder, filters, translation
    try:
        with codecs.open(fileName, 'r', errors='ignore') as file:
            doc = yaml.safe_load(file)
            logType = doc['input']['logtype']
            postran_key_words = doc['input']['postran']['re']
            qrcodetran_key_words = doc['input']['qrcodetran']['re']
            mis_clt_key_words = doc['input']['mis_clt']['re']
            log_path = doc['input']['path']
            classified_path = doc['output']['path']
            db_path = doc['output']['dbpath']
            finder = doc['output']['finder']
            filters = doc['output']['filter']['re']
            translation = doc['output']['translation']['re']

    except IOError:
        WriteMsg("ERROR: Configuration file not found.")
        return False

    return self_check()


# 获取指定值的正则表达式
def get_re(type):
    if not type: return ''
    if doc['input'].get(type,None):
        return doc['input'][type]['re']
    else:
        return {}


# 配置文件自检
def self_check():
    if not os.path.isdir(log_path):
        WriteMsg("ERROR: log path's " + log_path + " doesn't exist.")
        return False
    if not os.path.isdir(classified_path):
        WriteMsg("WARNING: classified log's path " + classified_path + " doesn't exist.")
    if not os.path.isfile(db_path):
        WriteMsg('ERROR: database path ' + db_path + "doesn't exist.")
        return False

    return True


