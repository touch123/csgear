# -*- coding: utf-8 -*-
# @Time : 2019/7/18 10:57
# @Author : Max
# @FileName: head.py
# @IDE: PyCharm
import re
import Configuration
import os


# 识别程序PID
def ID(txt):
    rg = re.compile(r'^\[.*?- (.*?)\]', re.IGNORECASE | re.DOTALL)
    m = rg.search(txt)
    if m:
        return m.group(1)
    else:
        return None


# 识别十六进制报文
def message_head(txt):
    ''' 
    TODO: 失败返回值要统一用None 还是False
    '''
    re1 = '^(\\d+): '  # Integer Number 1
    rg = re.compile(re1, re.IGNORECASE | re.DOTALL)
    m = rg.search(txt)
    if m:
        int1 = m.group(1)
        return int1
    else:
        return False


# 识别8583报文尾方括号
def message_tail(txt):
    re1 = '.*?'  # Non-greedy match on filler
    re2 = '(\\[.*\\])'  # Square Braces 1

    rg = re.compile(re1 + re2, re.IGNORECASE | re.DOTALL)
    m = rg.search(txt)
    if m:
        sbraces1 = m.group(1)
        return sbraces1
    else:
        return False



# 在关键字之后提取数值
def get_num(txt):
    re1 = '.*?'  # Non-greedy match on filler
    re2 = '\\d+'  # Uninteresting: int
    re3 = '.*?'  # Non-greedy match on filler
    re4 = '\\d+'  # Uninteresting: int
    re5 = '.*?'  # Non-greedy match on filler
    re6 = '\\d+'  # Uninteresting: int
    re7 = '.*?'  # Non-greedy match on filler
    re8 = '\\d+'  # Uninteresting: int
    re9 = '.*?'  # Non-greedy match on filler
    re10 = '(\\d+)'  # Integer Number 1

    rg = re.compile(re1 + re2 + re3 + re4 + re5 + re6 + re7 + re8 + re9 + re10, re.IGNORECASE | re.DOTALL)
    m = rg.search(txt)
    if m:
        int1 = m.group(1)
        return int1
    else:
        return None


# 预处理，整理好json格式入库
def key_words_marching(txt):  # 识别key_words列表
    for item in Configuration.postran_key_words:
        if item in txt:
            return True
    return False


# 自定义规则的正则搜索
def DIYSearch(rule, txt):
    # 忽略大小写模糊搜索
    rg = re.compile(rule, re.IGNORECASE | re.DOTALL)
    m = rg.search(txt)
    if m and len(m.groups()) > 0:
        result = m.group(1)
        return result
    else:
        return None


def FileDate(txt):
    ''' 
    TODO:  正则不准确
    '''
    re1 = '.*?'  # Non-greedy match on filler
    re2 = '((?:(?:[1]{1}\\d{1}\\d{1}\\d{1})|(?:[2]{1}\\d{3}))(?:[0]?[1-9]|[1][012])(?:(?:[0-2]?\\d{1})|(?:[3][01]{1})))(?![\\d])'  # YYYYMMDD 1

    rg = re.compile(re1 + re2, re.IGNORECASE | re.DOTALL)
    m = rg.search(txt)
    if m:
        yyyymmdd1 = m.group(1)
        return yyyymmdd1
    else:
        return None


def FileName(txt):
    ''' 
    TODO:  正则不准确
    '''
    re1 = '.*?'  # Non-greedy match on filler
    re2 = '((?:[a-z][a-z]+))'  # Word 1
    rg = re.compile(re1 + re2, re.IGNORECASE | re.DOTALL)
    m = rg.search(txt)
    if m and len(m.groups())>0:
        word1 = m.group(1)
        return word1
    else:
        return None


def file_name(user_dir):
    file_list = list()
    for root, dirs, files in os.walk(user_dir):
        for logfile in files:
            file_list.append(logfile)
            # file_list.append(os.path.join(root, file))
    return file_list


