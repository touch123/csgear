# -*- coding: utf-8 -*-

from unittest import TestCase

from Library import MrchId,get_num


class TestLibrary(TestCase):

    def setUp(self):
        pass

    def test_library(self):
        txt1 = "[03:10:01 - 35546] : begin pack DE 4"  # postran格式测试
        txt2 = "[03:10:01 - 32551] : connect MISP[172.18.18.3.5555] OK"  # mis格式测试
        txt3 = "[04:00:26 - 19524] [MoveRecord.cp   - 4428]: moveRecord start at[20190420]"  # QRcode格式测试
        txt4 = "01: 00 55 60 00 13 00 00 05 20 20 20 00 80 00 c1 00    [.U`.....   .....]"  # 报文头格式测试
        txt5 = "06: 56 37 01 c1 84 89 f1                               [V7.....]"  # 报文尾格式测试
        txt6 = "MrchId-[09:19:19 - 5893] : MrchId = [103421180620131]"  # MrchId格式测试
        txt7 = 'MrchId-[09:19:19 - 5893] : AbcMrchId=[]'
        txt8 = 'TermId-[09:19:19 - 5893] : AbcTermId=[]'
        print(MrchId(txt6))
        print(MrchId(txt7))
        print(MrchId(txt8))
        print(get_num(txt6))
        print(get_num(txt7))
        print(get_num(txt8))

    def test_library2(self):
        txt1 = "[03:10:01 - 35546] : begin pack DE 4"  # postran格式测试
        txt2 = "[03:10:01 - 32551] : connect MISP[172.18.18.3.5555] OK"  # mis格式测试
        txt3 = "[04:00:26 - 19524] [MoveRecord.cp   - 4428]: moveRecord start at[20190420]"  # QRcode格式测试
        txt4 = "01: 00 55 60 00 13 00 00 05 20 20 20 00 80 00 c1 00    [.U`.....   .....]"  # 报文头格式测试
        txt5 = "06: 56 37 01 c1 84 89 f1                               [V7.....]"  # 报文尾格式测试
        txt6 = "MrchId-[09:19:19 - 5893] : MrchId = [103421180620131]"  # MrchId格式测试
        txt7 = 'MrchId-[09:19:19 - 5893] : AbcMrchId=[]'
        txt8 = 'TermId-[09:19:19 - 5893] : AbcTermId=[]'
        print(MrchId(txt6))
        print(MrchId(txt7))
        print(MrchId(txt8))
        print(get_num(txt6))
        print(get_num(txt7))
        print(get_num(txt8))
