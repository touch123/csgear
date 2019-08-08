# -*- coding: utf-8 -*-
# @Time : 2019/7/18 10:57
# @Author : Max
# @FileName: head.py
# @IDE: PyCharm

import sys
import sqlite3
import Configuration
import os

conn = None
c = None


def WriteMsg(str):
    sys.stderr.write(str + '\n')


# 初始化数据库，创建并检查表
def init():
    if not os.path.isfile(str(Configuration.db_path)):
        WriteMsg("ERROR: datebase " + str(Configuration.db_path) + " not found.")
        exit()
    global conn, c
    conn = sqlite3.connect(str(Configuration.db_path))
    c = conn.cursor()
    WriteMsg("NOTICE: Initialize database " + str(Configuration.db_path))

    # 创建表
    c.execute('CREATE TABLE IF NOT EXISTS postran (pid TEXT, FileDate TEXT, path TEXT,Rrn TEXT, '
              'RespCode TEXT, CountNo TEXT, TermId TEXT, MrchId TEXT, TraceNo TEXT, Amount TEXT, SendToHost TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS ictran (pid TEXT, FileDate TEXT, path TEXT,Rrn TEXT, '
              'RespCode TEXT, CountNo TEXT, TermId TEXT, MrchId TEXT, TraceNo TEXT, Amount TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS sign (logType TEXT, FileDate TEXT, Status BOOLEAN)')
    c.execute(
        'CREATE TABLE IF NOT EXISTS mis_clt (pid TEXT, FileDate TEXT, path TEXT, TraceNo TEXT, TermID TEXT, Rrn TEXT, ProcessCode TEXT, MsgType TEXT, recv TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS qrcodetran (pid TEXT, FileDate TEXT, path TEXT,rrn TEXT, '
              'respcode TEXT, countno TEXT, TermId TEXT, MrchId TEXT, traceno TEXT, amount TEXT, '
              'auth_code TEXT, orderid TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS qr_clt (pid TEXT, FileDate TEXT, path TEXT, TraceNo TEXT)')


def drop_table():
    tables = ['postran', 'mis_clt']
    for item in tables:
        c.execute('DROP TABLE  ' + item)


def delete_table(logtype, fileDate=None):
    if fileDate:
        c.execute('DELETE FROM %s WHERE FileDate = "%s"' % (logtype, fileDate))
    else:
        c.execute('DELETE FROM %s' % logtype)


def delet_old_sign(logType, fileDate=None):
    c.execute('DELETE FROM sign WHERE logType = "%s" and FileDate = "%s"' % (logType, fileDate))


def delet_old_data(logType, fileDate=None):
    c.execute('DELETE FROM %s WHERE FileDate = "%s"' % (logType, fileDate))


def insert_dict_into_sql(logtype, dicts):
    delet_old_data(logtype, dicts[1]["FileDate"])
    for d in dicts:
        keys, values = zip(*d.items())
        insert_str = "INSERT INTO %s (%s) values (%s)" % (logtype, ",".join(keys), ",".join(['?'] * len(keys)))

        c.execute(insert_str, values)
    WriteMsg("NOTICE: for total " + str(
        len(dicts)) + " files values has been added into table " + logtype + " in database.")


def sign(fileDate, logType):
    c.execute('INSERT sign VALUES ("%s","%s","%s")' % (logType, fileDate, "1"))


def skip(logType, FileDate):
    c.execute('SELECT * FROM sign WHERE logType= "%s" and FileDate = "%s"' % (logType, FileDate))
    return c.fetchall()


def related_mis_pos(path):
    c.execute(
        'SELECT b.path from postran a, mis_clt b where 1=1 and a.FileDate = b.FileDate and a.TermId = b.TermId and a.path="%s"' % (
            path))
    return c.ferchall()


def search_mis_clt(time, pid):
    c.execute('select * from mis_clt where recv like  "%s" and pid > "%s" order by pid' % (time, pid))
    print c.ferchall()
    return c.ferchall()


def search(command):
    c.execute(command)
    result = []
    for item in c.fetchall():
        result.append(item)
    return result


def logout():
    conn.commit()
    c.close()
    conn.close()
    WriteMsg("NOTICE: logout database")


def getTable(logType):
    c.execute('PRAGMA table_info([%s])' % logType)
    return c.fetchall()


if __name__ == '__main__':
    init()
    logout()
