# -*- coding: utf-8 -*-
import re

# 预处理关键词

postran_key_words = {'MrchId': 'MrchId = \\[(.*?)\\]', 'TermId': 'TermId = \\[(.*?)\\]',
                     'RespCode': 'RespCode = \\[(.*?)\\]', 'Amount': ' Amount =\\[(.*?)\\]',
                     'szRrn': " szRrn=\\[(.*?)\\]"}


# 添加关键词
def add_key_words(string):
    postran_key_words.append(string)


# 识别程序PID
def ID(txt):
    re1 = '.*?'  # Non-greedy match on filler
    re2 = '\\d+'  # Uninteresting: int
    re3 = '.*?'  # Non-greedy match on filler
    re4 = '\\d+'  # Uninteresting: int
    re5 = '.*?'  # Non-greedy match on filler
    re6 = '\\d+'  # Uninteresting: int
    re7 = '.*?'  # Non-greedy match on filler
    re8 = '(\\d+)'  # Integer Number 1

    # rg = re.compile(re1 + re2 + re3 + re4 + re5 + re6 + re7 + re8, re.IGNORECASE | re.DOTALL)
    rg = re.compile('^\[.*?- (.*?)\]', re.IGNORECASE | re.DOTALL)
    m = rg.search(txt)
    if m:
        return m.group(1)
    else:
        return None


# 识别十六进制报文
def message_head(txt):
    # txt = '01: 33 c6 95 e4 e3 e5 da 22                            [3......"]'

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
    # txt = '01: 00 55 60 00 13 00 00 05 20 20 20 00 80 00 c1 00    [.U`.....   .....]'

    re1 = '.*?'  # Non-greedy match on filler
    re2 = '(\\[.*?\\])'  # Square Braces 1

    rg = re.compile(re1 + re2, re.IGNORECASE | re.DOTALL)
    m = rg.search(txt)
    if m:
        sbraces1 = m.group(1)
        return sbraces1
    else:
        return False


# def message_write(txt):
#     if 'write' in txt:
#         return True
#     else:
#         return False
#
#
# def message_read(txt):
#     if 'read' in txt:
#         return True
#     else:
#         return False


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
    for item in postran_key_words:
        if item in txt:
            pass


def MrchId(txt):
    reMrchId = ' MrchId = \\[(.*?)\\]'

    rg = re.compile(reMrchId, re.IGNORECASE | re.DOTALL)
    m = rg.search(txt)
    if m:
        sbraces1 = m.group(1)
        return sbraces1
    else:
        return None


def DIYSearch(rule, txt):
    rg = re.compile(rule, re.IGNORECASE | re.DOTALL)
    m = rg.search(txt)
    if m:
        result = m.group(1)
        return result
    else:
        return None


if __name__ == '__main__':
    txt1 = "[03:10:01 - 35546] : begin pack DE 4"  # postran格式测试
    txt2 = "[03:10:01 - 32551] : connect MISP[172.18.18.3.5555] OK"  # mis格式测试
    txt3 = "[04:00:26 - 19524] [MoveRecord.cp   - 4428]: moveRecord start at[20190420]"  # QRcode格式测试
    txt4 = "01: 00 55 60 00 13 00 00 05 20 20 20 00 80 00 c1 00    [.U`.....   .....]"  # 报文头格式测试
    txt5 = "06: 56 37 01 c1 84 89 f1                               [V7.....]"  # 报文尾格式测试
    txt6 = "MrchId-[09:19:19 - 5893] : MrchId = [103421180620131]"  # MrchId格式测试
    txt7 = 'MrchId-[09:19:19 - 5893] : AbcMrchId=[]'
    txt8 = 'TermId-[09:19:19 - 5893] : AbcTermId=[]'
    print(MrchId(txt6))
    print(MrchId(txt7))
    print(MrchId(txt8))
    print(get_num(txt6))
    print(get_num(txt7))
    print(get_num(txt8))
