import re

# 预处理关键词
key_words = ["szRrn", "RespCode", "MrchId", "TermId"]


def add_key_words(string):
    key_words.append(string)


def ID(txt):  # 识别程序ID
    re1 = '.*?'  # Non-greedy match on filler
    re2 = '\\d+'  # Uninteresting: int
    re3 = '.*?'  # Non-greedy match on filler
    re4 = '\\d+'  # Uninteresting: int
    re5 = '.*?'  # Non-greedy match on filler
    re6 = '\\d+'  # Uninteresting: int
    re7 = '.*?'  # Non-greedy match on filler
    re8 = '(\\d+)'  # Integer Number 1

    rg = re.compile(re1 + re2 + re3 + re4 + re5 + re6 + re7 + re8, re.IGNORECASE | re.DOTALL)
    m = rg.search(txt)
    if m and int(m.group(1)) >= 100:
        return m.group(1)
    else:
        return None


def message(txt):  # 识别十六进制报文
    # txt = '01: 33 c6 95 e4 e3 e5 da 22                            [3......"]'

    re1 = '(\\d+)'  # Integer Number 1

    rg = re.compile(re1, re.IGNORECASE | re.DOTALL)
    m = rg.search(txt)
    if m:
        int1 = m.group(1)
        return True
    else:
        return False


# 预处理，整理好json格式入库
def key_words_marching(txt):  # 识别key_words列表
    for item in key_words:
        if item in txt:
            pass


if __name__ == '__main__':
    txt1 = "[03:10:01 - 3546] : begin pack DE 4"  # postran格式测试
    txt2 = "[03:10:01 - 3551] : connect MISP[172.18.18.3.5555] OK"  # mis格式测试
    print(ID(txt1))
    print(ID(txt2))
