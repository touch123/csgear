# -*- coding: utf-8 -*-
# @Time : 2019/7/24 15:59
# @Author : Max
# @FileName: Sensor.py
# @IDE: PyCharm
import Configuration
import os

def Sensor(fileDate=None, logType=Configuration.logType):
    fileList = []
    if fileDate:
        for item in file_names():
            portion = os.path.splitext(item)

            # 将文件名拆成名字和后缀
            if portion[0] in logType and portion[1] == '.' + fileDate:
                fileList.append(portion)
                print Configuration.log_path + item

    else:
        pass
        # 没有日期
    return fileList


# 遍历文件下下的文件名
def file_names(user_dir=Configuration.log_path):
    file_list = list()
    for root, dirs, files in os.walk(user_dir):
        for file in files:
            file_list.append(file)
            # file_list.append(os.path.join(root, file))
    return file_list

if __name__ == '__main__':
    pass