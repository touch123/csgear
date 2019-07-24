# -*- coding: utf-8 -*-
# @Time : 2019/7/23 9:10
# @Author : Max
# @FileName: Configuration.py
# @IDE: PyCharm
import yaml
import codecs


# 初始化关键词列表
with codecs.open('LogSpider.yml', 'r', errors='ignore') as file:
    doc = yaml.safe_load(file)
    logType = doc['input']['logtype']
    postran_key_words = doc['input']['postran']['re']
    qrcodetran_key_words = doc['input']['qrcodetran']['re']
    log_path = doc['input']['path']
    classified_path = doc['output']['path']


# 获取指定值的正则表达式
def get_re(type):
    with codecs.open('LogSpider.yml', 'r', errors='ignore') as file:
        doc = yaml.safe_load(file)
        if type:
            for item in doc['input']:
                if item == type:
                    return doc['input'][item]['re']
                    # print item + " " + str(doc['input'][item]['re'])
                    # print list(doc['input'][item]['re'])
                    # print list(doc['input'][item]['re'].values())


if __name__ == '__main__':
    pass
