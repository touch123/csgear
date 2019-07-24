# -*- coding: utf-8 -*-
# @Time : 2019/7/18 10:57
# @Author : Max
# @FileName: head.py
# @IDE: PyCharm
import iso8583
import json


def unpacking(txt):
    respose = iso8583.iso_8583("my_head", "pos", txt)
    fields = respose.unpack()
    # respose.ISO8583_testOutput()
    return fields[11],fields[41]

if __name__ == '__main__':
    # 测试8583
    qiandao="003C600450000060310031000008000020000000C00012000008363030303030303138373431313031343531313236313300110000005300400003303031"
    a="008A60000000046022000000000210703A04810ED0801B186229093369942011102000000000000001000000091348480126012602200008100000013638353233323132393330353939383031323132363030303030303138373431313031343531313236313306796565706179313536000823000053001200058300000700034355504532453836443442"

    lz="00F230303030303030323030B220048000C10010000000000000004133303030303030303030303030303030303130333130313635313035353537383331303132303032323232303437303434373632303135393432303030313036327765636861742020202031373033313031363531303532323232303437303133303436373835363130373032303830342020202020202020202020202020303433383043313420202020202020202020202020202020203139322E3136382E36352E313035203333333334343033303030303030363030303330303030303030303030303030303130303030303245393936463044"
    lz_xf="01f360000300000030323030f23c46c1a0e09a100000000000000041313936323134393638323130343530303032363638303030303030303030303030303030303033313232343030333433363030303634333030333433363132323433303132353934323035313030303030303630383034343738323130303830343437383231303337363231343936383231303435303030323636383d33303132323230383438303030303030303232323230343730343437363230313539343230303031b2e2cad4202020202020202020202020202020202020202020202020202020202020202020202020313536bb0fbd15d0467c3d323630303030303030303030303030303134399f3303e0e1c8950500800470009f1e0833443936393736349f101307000103a02002010a0100000055508b38f8e09f26087475fc9bd7816af59f3602033d82027c009c01009f1a0201569a031612249f02060000000000035f2a0201569f03060000000000009f3501229f34030203009f3704c0798ac69f2701809f4104000006439f6310000000000000000000000000000000003034333830303131202020202020202020202020202020202035382e31322e312e323238202020203030303030343033303030303030353030303330303030303030303030303031323130303030303145433533443232"

    test="011b600013000002007024068020c1821519000000000000000000000000000000000896905700120000007200015037000000000000000000000000000000002000003132313136383434313033343231313830363230313331000831324d495331313831353601199f3303e0e0c8950500000000009f1a0201569a031901169f3704cca9de3482027c009f360200189f260814cc255839d84d979c01009f02060000000896905f2a0201569f03060000000000009f101307010103a00000010a010000000000828bf5e69f34030200009f2701809f1e0838373839383138350037a00200d00001f03ec530d2f85bffe1827beb8f1f3a93747ea36b7a9a13eddbef8b14aa3de900123033333436373136303333342898755cd8599f0b"

    test="0055600013000005202020008000c10015980000550002143132313136383235313033343231313830363230313331000831324d49533131380006413030313030001230333334353531363033333490394db124850c40"
    b=iso8583.iso_8583("my_head","pos",test)
    dd = b.unpack()
    #b.set_bit(39,"00")
    b.ISO8583_testOutput()
    print dd[11]