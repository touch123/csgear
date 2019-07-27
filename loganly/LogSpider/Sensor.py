# -*- coding: utf-8 -*-
# @Time : 2019/7/24 15:59
# @Author : Max
# @FileName: Sensor.py
# @IDE: PyCharm
import Configuration
import os
import DBMS


def Sensor(fileDate=None):
    for item in file_names(Configuration.log_path):
        portion = os.path.splitext(item)

        # 检测到配置目录下指定日期的文件
        if fileDate:
            if portion[1] == '.' + fileDate:
                if DBMS.skip(portion[0], portion[1].replace('.', "")):
                    continue
                DBMS.insert_dict_into_sql('sign', [{'logType': portion[0], 'FileDate': portion[1].replace('.', ""), 'Status': False}])
        # 日期为缺省默认处理所有文件
        else:
            if DBMS.skip(portion[0], portion[1].replace('.', "")):
                continue
            DBMS.insert_dict_into_sql('sign', [{'logType': portion[0], 'FileDate': portion[1].replace('.', ""), 'Status': False}])


# 遍历文件下下的文件名
def file_names(user_dir=Configuration.log_path):
    file_list = list()
    for root, dirs, files in os.walk(user_dir):
        for file in files:
            file_list.append(file)
            # file_list.append(os.path.join(root, file))
    return file_list


if __name__ == '__main__':
    Configuration.init()
    Sensor()
    DBMS.logout()
