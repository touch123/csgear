# -*- coding: utf-8 -*-
# @Time : 2019/7/18 10:57
# @Author : Max
# @FileName: head.py
# @IDE: PyCharm
import Library
import iso8583
import codecs
import Configuration
import os


def unpacking_mis(file_path):
    str_reads = None
    str_write = None
    if not os.path.isfile(file_path):
        print "WARNING: file " + file_path + " don't exist."
    with codecs.open(file_path, 'r', encoding='gb2312', errors='ignore') as log:
        # 在读取完read和write之后用jion()方法合并字符串，然后去空格
        reads = []  # 空read报文容器
        writes = []  # 空write报文容器

        # 记录读写状态
        read = False
        write = False
        rev_buf = None
        for line in log.readlines():
            pid = Library.ID(line)
            if rev_buf is None:
                rev_buf = Library.DIYSearch(Configuration.mis_clt_key_words['recv buf'], line)

            message_head = Library.message_head(line)
            if pid:

                # 如果开头是pid文
                # 1.报文头
                # 2.连续的报文尾

                # 如果检测到报文类型关键词且是第一次出现
                if 'write2 .....' in line and write is False:
                    write = True
                    if read is True:
                        read = False  # 释放read开关节省时间
                elif 'read .....' in line and read is False:
                    read = True
                    if write is True:
                        write = False
                elif 'read from MISP len' in line and read != 0:
                    str_write = "".join(writes).replace("\n", "")
                    str_reads = "".join(reads).replace("\n", "")

                    return str_write, str_reads, rev_buf

            else:
                # 如果不是pid头
                if message_head:  # 只有可能是报文的头部被检测到了
                    if write:
                        # print("W:" + line)
                        writes += str(get_pure_8583(Library.message_head(line) + ": ", Library.message_tail(line),
                                                    line)).split(" ")
                    if read:
                        # print("R:" + line)
                        reads += str(get_pure_8583(Library.message_head(line) + ": ", Library.message_tail(line),
                                                   line)).split(" ")
    return str_write, str_reads, rev_buf


# 添加自定义关键词进返回的字典中
def classifying_mis(file_name):
    results = []
    FileDate = Library.FileDate(file_name)
    path = Configuration.classified_path
    # path + file_name
    lists = Library.file_name(path + file_name)
    for item in lists:
        result = []
        temp = unpacking_mis(path + file_name + "/" + item)
        couple = decode_8583(temp[0])
        result.append(('TraceNo', couple[0]))
        result.append(('TermID', couple[1]))
        result.append(('Rrn', couple[2]))
        result.append(('ProcessCode', couple[3]))
        result.append(('MsgType', couple[4]))
        result.append(('recv', temp[2]))
        result.append(('PID', item))
        result.append(('FileDate', FileDate))
        result.append(('path', path + file_name + "/" + item))
        results.append(dict(result))
    return results


def decode_8583(txt):
    respose = iso8583.iso_8583("my_head", "pos", txt)
    fields = respose.unpack()
    for i in [11, 41, 37, 3, -3]:
        if i not in fields:
            fields.update({i: None})
    # respose.ISO8583_testOutput()

    return fields[11], fields[41], fields[37], fields[3], fields[-3]


# 字符串删除算法一：通过列表
def delete_substr_method1(in_str, in_substr):
    start_loc = in_str.find(in_substr)
    in_str, in_substr = list(in_str), list(in_substr)
    [len_str, len_substr] = len(in_str), len(in_substr)
    res_str = in_str[:start_loc]
    for i in range(start_loc + len_substr, len_str):
        res_str.append(in_str[i])
    res = ''.join(res_str)
    return res


# 字符串删除算法二：通过切片
def delete_substr_method2(in_str, in_substr):
    start_loc = in_str.find(in_substr)
    len_substr = len(in_substr)
    res_str = in_str[:start_loc] + in_str[start_loc + len_substr:]
    return res_str


def get_pure_8583(head, tail, line):
    return delete_substr_method2(delete_substr_method2(line, head), tail)
