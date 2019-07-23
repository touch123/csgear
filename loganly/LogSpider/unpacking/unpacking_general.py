# -*- coding: utf-8 -*-
# @Time : 2019/7/23 15:31
# @Author : Max
# @FileName: unpacking_general.py
# @IDE: PyCharm

import ptn
import ReadYmal
import reader
import codecs


# 解析关键词列表
def unpacking(file_path, type):
    result = []  # 空结果列表，采集完了再把列表变成字典
    with codecs.open(file_path, 'r', encoding='gb2312', errors='ignore') as log:
        words = list(ReadYmal.get_re(type))
        rules = list(ReadYmal.get_re(type).values())
        for line in log.readlines():
            # 一次性匹配多个关键词
            for i in range(0, len(words)):
                if words[i] in line:
                    if rules[i]:
                        data = ptn.DIYSearch(rules[i], line)
                        if data:
                            result.append((words[i], data))
                            rules[i] = None
    return result


# 对预处理的关键词列表json进行二次加工,加入FileDate, TransTime, PID
def classifying(file_name):
    results = []
    FileDate = ptn.FileDate(file_name)
    FileName = ptn.FileName(file_name)
    path = 'C:\\Users\\heckn\\Desktop\\LogSpider\\log\\classified_log\\'
    lists = reader.file_name(path + file_name)
    for item in lists:
        result = unpacking(path + file_name + "\\" + item, FileName)
        # 自定义部分
        result.append(('PID', item))
        result.append(('FileDate', FileDate))
        result.append(('path', path + file_name + "\\" + item))
        results.append(dict(result))

    return results


if __name__ == '__main__':
    print classifying('qrcodetran.20190420')
