# -*- coding: utf-8 -*-
# @Time : 2019/7/18 10:57
# @Author : Max
# @FileName: head.py
# @IDE: PyCharm
import ptn
import delete_str
import reader
import codecs
import unpacking_8583


def unpacking_mis(file_path):
    with codecs.open(file_path, 'r', encoding='gb2312', errors='ignore') as log:
        # 在读取完read和write之后用jion()方法合并字符串，然后去空格
        reads = []  # 空read报文容器
        writes = []  # 空write报文容器

        # 记录读写状态
        read = False
        write = False
        for line in log.readlines():
            pid = ptn.ID(line)
            message_head = ptn.message_head(line)
            if pid:
                # 如果开头是pid文
                # 1.报文头
                # 2.连续的报文尾

                # 如果检测到报文类型关键词且是第一次出现
                if 'write2 .....' in line and write is False:
                    write = True
                    if read is True:
                        read = False # 释放read开关节省时间
                elif 'read .....' in line and read is False:
                    read = True
                    if write is True:
                        write = False
                elif 'read from MISP len' in line and read != 0:
                    str_write = "".join(writes).replace("\n", "")
                    str_reads = "".join(reads).replace("\n", "")
                    return str_write, str_reads

            else:
                # 如果不是pid头
                if message_head:  # 只有可能是报文的头部被检测到了
                    if write:
                        # print("W:" + line)
                        writes += str(delete_str.get_pure_8583(ptn.message_head(line) + ": ", ptn.message_tail(line),
                                                               line)).split(" ")
                    if read:
                        # print("R:" + line)
                        reads += str(delete_str.get_pure_8583(ptn.message_head(line) + ": ", ptn.message_tail(line),
                                                              line)).split(" ")
    # return str_write, str_reads


# 添加自定义关键词进返回的字典中
def classifying_mis(file_name):
    results = []
    FileDate = ptn.FileDate(file_name)
    path = 'log//classified_log//'
    lists = reader.file_name(path + file_name)
    for item in lists:
        result = []
        temp = unpacking_mis(path + file_name + "//" + item)
        couple = unpacking_8583.unpacking(temp[0])
        result.append(('TraceNo', couple[0]))
        result.append(('TermID', couple[1]))
        result.append(('PID', item))
        result.append(('FileDate', FileDate))
        result.append(('path', path + file_name + "//" + item))
        results.append(dict(result))
    return results


if __name__ == '__main__':
    # 测试unpacking_mis函数
    # print(unpacking("5897"))
    # for item in reader.file_name("log//classified_log//mis_clt.20190116"):
    #    temp = unpacking_mis("log//classified_log//mis_clt.20190116//" + item)
    #    print(item + " : " + str(temp[1]))
    #    print (item + " : " + str(unpacking_8583.unpacking(temp[0])))
    #    print (item + " : " + unpacking_8583.unpacking("0000" + temp[1]))
    print classifying_mis('mis_clt.20190116')

