# -*- coding: utf-8 -*-
# @Time : 2019/7/18 10:57
# @Author : Max
# @FileName: head.py
# @IDE: PyCharm
import iso
import json


def unpacking(txt):
    respose = iso.iso_8583("my_head", "pos", txt)
    fields = respose.unpack()
    # respose.ISO8583_testOutput()
    return fields[11],fields[41]

if __name__ == '__main__':
    print unpacking("0055600013000005202020008000c10015980000550004143132313136383439313033343231313830363230313331000831324d495331313800064130303130300012303632313233313530363231dd9699bda26f27db")