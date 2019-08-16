# -*- coding: utf-8 -*-
# @Time : 2019/7/24 15:59
# @Author : Max
# @FileName: Sensor.py
# @IDE: PyCharm

import os
import Configuration
import DBMS


def sensor(file_date=None):
    """
    根据fileDate 检测系统中指定配置目录下的日志文件
    如fileDate 为None,则检测所有文件
    """
    if not DBMS.connect(Configuration.db_path):
        return False
    for item in file_names(Configuration.log_path):
        portion = os.path.splitext(item)

        # 检测到配置目录下指定日期的文件
        if file_date:
            if portion[1] == '.' + file_date:
                if DBMS.skip(portion[0], portion[1].replace('.', "")):
                    continue
                DBMS.insert_dict_into_sql('sign', [{'logType': portion[0], 'FileDate': portion[1].replace('.', ""), 'Status': False}])
        # 日期为缺省默认处理所有文件
        else:
            if DBMS.skip(portion[0], portion[1].replace('.', "")):
                continue
            DBMS.insert_dict_into_sql('sign', [{'logType': portion[0], 'FileDate': portion[1].replace('.', ""), 'Status': False}])

    DBMS.disconnect()
    return True


# 遍历文件下下的文件名
def file_names(user_dir=Configuration.log_path):
    if not user_dir : return []
    file_list = list()
    for root, dirs, files in os.walk(user_dir):
        for log_file in files:
            file_list.append(log_file)
            # file_list.append(os.path.join(root, file))
    return file_list


if __name__ == '__main__':
    Configuration.load('debug.yml')
    sensor()
