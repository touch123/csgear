# -*- coding: utf-8 -*-
# @Time : 2019/7/18 10:57
# @Author : Max
# @FileName: head.py
# @IDE: PyCharm
import ptn
import json
import reader
import codecs


# 解析关键词列表
def unpacking_postran(file_path):
    result = []  # 空结果列表，采集完了再把列表变成字典
    with codecs.open(file_path, 'r', encoding='gb2312', errors='ignore') as log:
        words = list(ptn.postran_key_words)
        rules = list(ptn.postran_key_words.values())
        for line in log.readlines():
            # 一次性匹配多个关键词
            for i in range(0, len(words)):
                if words[i] in line:
                    if rules[i]:
                        data = ptn.DIYSearch(rules[i], line)
                        if data:
                            result.append((words[i], data))
                            rules[i] = None

    # return json.dumps(dict(result))
    return result


# 对预处理的关键词列表json进行二次加工,加入FileDate, TransTime, PID
def classifying_postran(file_name):
    results = []
    FileDate = ptn.FileDate(file_name)
    path = 'log//classified_log//'
    lists = reader.file_name(path + file_name)
    for item in lists:
        result = unpacking_postran(path + file_name + "//" +item)
        # 自定义部分
        result.append(('PID', item))
        result.append(('FileDate', FileDate))
        result.append(('path', path + file_name + "//" + item))
        results.append(dict(result))

    return results


if __name__ == '__main__':
    # unpacking_postran测试
    # print(unpacking_postran("5893"))
    # for item in reader.file_name("log//classified_log//postran.20190116"):
    #     print(item + " : " + unpacking_postran("log//classified_log//postran.20190116//" + item))
    print classifying_postran('postran.20190116')