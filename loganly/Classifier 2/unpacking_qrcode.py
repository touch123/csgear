# -*- coding: utf-8 -*-
# @Time : 2019/7/18 11:10
# @Author : Max
# @FileName: unpacking_qrcode.py
# @IDE: PyCharm
import codecs
import ptn
import json
import reader


# 解析关键词列表
def unpacking_qrcode(file_path):
    result = []  # 空结果列表，采集完了再把列表变成字典
    with codecs.open(file_path, 'r', encoding='gb2312', errors='ignore') as log:
        words = list(ptn.qrcodetran_key_words)
        rules = list(ptn.qrcodetran_key_words.values())
        for line in log.readlines():
            # 一次性匹配多个关键词
            for i in range(0, len(words)):
                if words[i] in line:
                    if rules[i]:
                        data = ptn.DIYSearch(rules[i], line)
                        if data:
                            result.append((words[i], data))
                            rules[i] = None
    return json.dumps(dict(result))


if __name__ == '__main__':
    for item in reader.file_name("log//classified_log//qrcodetran.20190107"):
        print(item + " : " + unpacking_qrcode("log//classified_log//qrcodetran.20190107//" + item))

