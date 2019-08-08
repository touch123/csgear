# -*- coding: utf-8 -*-
# @Time : 2019/7/24 16:28
# @Author : Max
# @FileName: Filter.py
# @IDE: PyCharm
import codecs
import re
import sys
import Configuration
import DBMS


def WriteMsg(str):
    sys.stderr.write(str + '\n')


def IsExclude(line):
    for rule in Configuration.filters:
        if re.search(rule, line):
            return True
    return False


def Translate(line):
    for key, value in Configuration.translation.items():
        output = re.sub(key, value, line)
        if output != line:
            return output
    return line


def DoFilter(filename):
    with codecs.open(filename, 'r', encoding='gb2312', errors='ignore') as log:
        lines = log.readlines()
        out_lines = []
        for line in lines:
            if not IsExclude(line):
                outline = Translate(line)
                print(outline.strip())
                out_lines.append(outline)

        file = codecs.open(Configuration.finder, 'a+', encoding='gb2312', errors='ignore')
        file.writelines(out_lines)

    file.write("\n\n")
    file.close()


def FilterByPipe():
    '''
    cmd运行,从标准输入获取文件列表
    '''
    lines = sys.stdin.readlines()
    for item in lines:
        WriteMsg(item.strip() + ' doing...')
        DoFilter(item.strip())


def Filter(d):
    '''
    程序调用   
    '''
    for item in d:
        file_path = item["path"]
        DoFilter(file_path)


if __name__ == '__main__':
    Configuration.init()
    FilterByPipe()
