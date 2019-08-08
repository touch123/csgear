# -*- coding: utf-8 -*-
# @Time : 2019/7/23 15:31
# @Author : Max
# @FileName: unpacking_general.py
# @IDE: PyCharm

import Library
import Dealer
import codecs
import Configuration
import pprint
import os


# 解析关键词列表
def unpacking(file_path, type):
    result = []  # 空结果列表，采集完了再把列表变成字典
    if not os.path.isfile(file_path):
        print "WARNING: file " + file_path + " don't exist."
    with codecs.open(file_path, 'r', encoding='gb2312', errors='ignore') as log:
        words = list(Configuration.get_re(type))
        rules = list(Configuration.get_re(type).values())
        for line in log.readlines():
            # 一次性匹配多个关键词
            for i in range(0, len(words)):
                if words[i] in line:
                    # if words[i] == 'SendToHost':
                    #     print words[i] + ": " +line
                    if rules[i]:
                        data = Library.DIYSearch(rules[i], line)
                        if data:
                            result.append((words[i], data))
                            rules[i] = None
    return result


# 对预处理的关键词列表进行二次加工,加入FileDate, TransTime, PID
def classifying(file_name):
    results = []
    FileDate = Library.FileDate(file_name)
    FileName = Library.FileName(file_name)
    path = Configuration.classified_path
    lists = Library.file_name(path + file_name)
    for item in lists:
        result = unpacking(path + file_name + "/" + item, FileName)
        # 和文件名相关的自定义部分
        result.append(('PID', item))
        result.append(('FileDate', FileDate))
        result.append(('path', path + file_name + "/" + item))
        results.append(dict(result))

    return results


