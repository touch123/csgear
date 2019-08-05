# -*- coding: utf-8 -*-
# @Time : 2019/7/18 10:57
# @Author : Max
# @FileName: head.py
# @IDE: PyCharm
import Library
import os
import codecs
import Configuration


# 读取log的pid并拆分
def classification(file_path):
    catalog = []
    # old_present = 0 打印进度条
    with codecs.open(file_path, 'r', encoding='gb2312', errors='ignore') as log:
        name = os.path.basename(log.name)
        path = Configuration.classified_path + name
        mk_dir(path)
        lines = log.readlines()
        current_pid = 0
        file = None
        for line in lines:
            pid = Library.ID(line)
            if pid:
                if pid not in catalog:  # 不在源目录里面的新pid
                    file = codecs.open(path + "/" + pid, 'a+', encoding='gb2312', errors='ignore')  # 创建新文件
                    catalog.append(pid)

                if pid != current_pid:  # 当前的pid和连续的pid不一样
                    file.close()
                    file = codecs.open(path + "/" + pid, 'a+', encoding='gb2312', errors='ignore')
                    file.write(line)
                else:  # 连续的pid
                    file.write(line)
                current_pid = pid  # 当前pid设置为和目录不一样的pid
            else:  # 数字开头的十六进制报文
                if file:
                    file.write(line)
                    # 打印进度条，python 2.7炸了不知道为啥
                    # if round(count / len(lines) * 100) != old_present*1.0:
                    #    print("Classifing: " + str(log.name) + "...... " + str(round(count / len(lines) * 100)) + "%")
                    #    old_present = round(count / len(lines) * 100)
        print "NOTICE: distributed " + str(os.path.split(file_path)[1]) + ' into ' + str(
            len(catalog)) + ' file base on the PID in path ' + str(path)
        return catalog


# 生成以日志文件名为名称的文件夹用来存放以pid来进行拆分的单独文件
def mk_dir(dir_path):
    is_exist = os.path.exists(dir_path)
    if not is_exist:
        os.makedirs(dir_path)
        print("NOTICE: folder " + dir_path + " was created.")
        return True
    else:
        return False


def file_name(user_dir):
    file_list = list()
    for root, dirs, files in os.walk(user_dir):
        for file in files:
            file_list.append(file)
            # file_list.append(os.path.join(root, file))
    return file_list


if __name__ == '__main__':
    pass
    # main()

    # 拆分成以pid为文件名
    classification("log\\qrcodetran.20190420")
    classification("log\\postran.20190116")
    classification("log\\mis_clt.20190116")
    classification("log\\qrcodetran.20190107")
    classification("log\\qr_clt.20190107")

    # 遍历刚刚生成的文件夹下面的文件
    # *可选：多进程同时处理*
    # 运行unpacking程序进行解析的提取
    # 抽取的结果在unpacking里面直接入库
