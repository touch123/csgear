# -*- coding: utf-8 -*-
# @Time : 2019/7/24 16:28
# @Author : Max
# @FileName: Filter.py
# @IDE: PyCharm
import codecs
import re
import sys
import Configuration


def write_msg(msg):
    sys.stderr.write(msg + '\n')


def is_exclude(line, log_type=None):
    if log_type:
        for rule in Configuration.doc['input'][log_type]['filter']['re']:
            if re.search(rule, line):
                return True
    if log_type is None:
        for rule in Configuration.filters:
            if re.search(rule, line):
                return True
    return False


def translate(line):
    for key, value in Configuration.translation.items():
        output = re.sub(key, value, line)
        if output != line:
            return output
    return line


def do_filter(filename, log_type=None):
    with codecs.open(filename, 'r', encoding='gb2312', errors='ignore') as log:
        lines = log.readlines()
        out_lines = []
        for line in lines:
            if not is_exclude(line, log_type):
                outline = translate(line)
                print(outline.strip())
                out_lines.append(outline)

        logfile = codecs.open(Configuration.finder, 'a+', encoding='gb2312', errors='ignore')
        logfile.writelines(out_lines)

    logfile.write("\n\n")
    logfile.close()


def filter_by_pipe():
    """
    cmd运行,从标准输入获取文件列表
    """
    lines = sys.stdin.readlines()
    for item in lines:
        write_msg(item.strip() + ' doing...')
        do_filter(item.strip())


def filter_by_call(d, log_type=None):
    """
    程序调用
    """
    for item in d:
        file_path = item["path"]
        do_filter(file_path, log_type)


if __name__ == '__main__':
    Configuration.load()
    filter_by_pipe()
