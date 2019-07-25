# -*- coding: utf-8 -*-
# @Time : 2019/7/23 9:10
# @Author : Max
# @FileName: Configuration.py
# @IDE: PyCharm
import yaml
import codecs

doc = None
logType = None
postran_key_words = None
qrcodetran_key_words = None
log_path = None
classified_path = None


# 初始化关键词列表
def init():
    global doc, logType, postran_key_words, qrcodetran_key_words, log_path, classified_path
    with codecs.open('LogSpider.yml', 'r', errors='ignore') as file:
        doc = yaml.safe_load(file)
        logType = doc['input']['logtype']
        postran_key_words = doc['input']['postran']['re']
        qrcodetran_key_words = doc['input']['qrcodetran']['re']
        log_path = doc['input']['path']
        classified_path = doc['output']['path']


#    return doc


# 获取指定值的正则表达式
def get_re(type):
    # if type:
    #     for item in doc['input']:
    #         if item == type:
    #             return doc['input'][item]['re']
    #             # print item + " " + str(doc['input'][item]['re'])
    #             # print list(doc['input'][item]['re'])
    #             # print list(doc['input'][item]['re'].values())
    return doc['input'][type]['re']


if __name__ == '__main__':
    pass
