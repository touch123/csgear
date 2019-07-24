# -*- coding: utf-8 -*-
# @Time : 2019/7/18 10:57
# @Author : Max
# @FileName: head.py
# @IDE: PyCharm
import sqlite3
import unpacking

conn = sqlite3.connect("identifier.sqlite")
c = conn.cursor()


def init():
    # 暴力创建postran表(测试用着还行)
    # c.execute(
    #    'INSERT INTO postran (pid, FileDate, path, Rrn, RespCode, CountNo, TermId, MrchID, TraceNo, Amount) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
    #    ('0', '0', '0', '0', '0', '0', '0', '0', '0', '0'))
    # conn.commit()
    c.execute('CREATE TABLE IF NOT EXISTS postran (pid TEXT, FileDate TEXT, path TEXT,Rrn TEXT, '
              'RespCode TEXT, CountNo TEXT, TermId TEXT, MrchId TEXT, TraceNo TEXT, Amount TEXT)')
    # c.execute('CREATE TABLE IF NOT EXISTS sign (logType TEXT, FileDate TEXT, Status TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS mis_clt (pid TEXT, FileDate TEXT, path TEXT, TraceNo TEXT, TermID TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS qrcodetran (pid TEXT, FileDate TEXT, path TEXT,rrn TEXT, '
              'respcode TEXT, countno TEXT, TermId TEXT, MrchId TEXT, traceno TEXT, amount TEXT, '
              'auth_code TEXT, orderid TEXT)')

    # c.execute('CREATE TABLE IF NOT EXISTS qr_clt (pid TEXT, FileDate TEXT, path TEXT, TraceNo TEXT)')


def drop_table():
    tables = ['postran', 'mis_clt']
    for item in tables:
        c.execute('DROP TABLE  ' + item)
    conn.commit()


def delete_table(logtype, fileDate = None):
    if fileDate:
        c.execute('DELETE FROM %s WHERE fileDate = "%s"' % (logtype, fileDate))
    else:
        c.execute('DELETE FROM %s' % logtype)
    conn.commit()


def insert_dict_into_sql(logtype, dicts):
    # INSERT INTO postran (pid, json) VALUES(?, ?)
    for d in dicts:
        keys, values = zip(*d.items())
        insert_str = "INSERT INTO %s (%s) values (%s)" % (logtype, ",".join(keys), ",".join(['?'] * len(keys)))
        # print insert_str
        c.execute(insert_str, values)
        # conn.commit()


def sign(fileDate, logType):
    c.execute('INSERT sign VALUES ("%s","%s","%s")' % (logType, fileDate, "1"))


if __name__ == '__main__':
    init()
    delete_table("qrcodetran")
    # insert_dict_into_sql('postran', unpacking.classifying_postran('postran.20190116'))
    # insert_dict_into_sql('mis_clt', unpacking.classifying_mis('mis_clt.20190116'))
    insert_dict_into_sql('qrcodetran', unpacking.classifying_qrcode('qrcodetran.20190107'))
    insert_dict_into_sql('qrcodetran', unpacking.classifying_qrcode('qrcodetran.20190420'))
    conn.commit()
    c.close()
    conn.close()

