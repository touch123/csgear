# -*- coding: utf-8 -*-
# @Time : 2019/7/24 16:28
# @Author : Max
# @FileName: Filter.py
# @IDE: PyCharm
import codecs
import Configuration
import re

def Filter(d):
    for item in d:
        file_path = item["path"]
        with codecs.open(file_path, 'r', encoding='gb2312', errors='ignore') as log:

            # 修改&过滤
            lines = log.readlines()
            for line in lines:
                # 过滤规则

                for rule in Configuration.filters:
                    if re.search(rule, line):
                        lines.remove(line)
                # 翻译规则
                # highline 规则

            # 写入
            file = codecs.open(Configuration.finder, 'a+', encoding='gb2312', errors='ignore')
            file.writelines(lines)

        file.write("\n\n")
        file.close()


if __name__ == '__main__':
    pass
