# -*- coding: utf-8 -*-
# @Time : 2019/7/18 10:57
# @Author : Max
# @FileName: head.py
# @IDE: PyCharm
import sqlite3
import Configuration

# Configuration.init()
conn = sqlite3.connect(str(Configuration.db_path))
c = conn.cursor()


def init():
    c.execute('CREATE TABLE IF NOT EXISTS postran (pid TEXT, FileDate TEXT, path TEXT,Rrn TEXT, '
              'RespCode TEXT, CountNo TEXT, TermId TEXT, MrchId TEXT, TraceNo TEXT, Amount TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS ictran (pid TEXT, FileDate TEXT, path TEXT,Rrn TEXT, '
              'RespCode TEXT, CountNo TEXT, TermId TEXT, MrchId TEXT, TraceNo TEXT, Amount TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS sign (logType TEXT, FileDate TEXT, Status BOOLEAN)')
    c.execute('CREATE TABLE IF NOT EXISTS mis_clt (pid TEXT, FileDate TEXT, path TEXT, TraceNo TEXT, TermID TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS qrcodetran (pid TEXT, FileDate TEXT, path TEXT,rrn TEXT, '
              'respcode TEXT, countno TEXT, TermId TEXT, MrchId TEXT, traceno TEXT, amount TEXT, '
              'auth_code TEXT, orderid TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS qr_clt (pid TEXT, FileDate TEXT, path TEXT, TraceNo TEXT)')


def drop_table():
    tables = ['postran', 'mis_clt']
    for item in tables:
        c.execute('DROP TABLE  ' + item)
    conn.commit()


def delete_table(logtype, fileDate=None):
    if fileDate:
        c.execute('DELETE FROM %s WHERE FileDate = "%s"' % (logtype, fileDate))
    else:
        c.execute('DELETE FROM %s' % logtype)
    conn.commit()


def delet_old_sign(logType, fileDate=None):
    c.execute('DELETE FROM sign WHERE logType = "%s" and FileDate = "%s"' % (logType, fileDate))
    conn.commit()


def insert_dict_into_sql(logtype, dicts):

    for d in dicts:
        keys, values = zip(*d.items())
        insert_str = "INSERT INTO %s (%s) values (%s)" % (logtype, ",".join(keys), ",".join(['?'] * len(keys)))
        c.execute(insert_str, values)
    print "NOTICE: for total " + str(len(dicts)) + " files' values has been added into table " + logtype + " in database."


def sign(fileDate, logType):
    c.execute('INSERT sign VALUES ("%s","%s","%s")' % (logType, fileDate, "1"))


def skip(logType, FileDate):
    c.execute('SELECT * FROM sign WHERE logType= "%s" and FileDate = "%s"' % (logType, FileDate))
    return c.fetchall()


def sreach(command):
    c.execute(command)
    result = []
    for item in c.fetchall():
        result.append(item[1])
    return result


def logout():
    conn.commit()
    c.close()
    conn.close()


def getTable(logType):
    c.execute('PRAGMA table_info([%s])' % logType)
    return c.fetchall()


if __name__ == '__main__':
    init()
    # Configuration.init()
    # delete_table("qrcodetran")
    # insert_dict_into_sql('postran', unpacking.classifying('postran.20190116'))
    # insert_dict_into_sql('mis_clt', unpacking.classifying_mis('mis_clt.20190116'))
    # insert_dict_into_sql('qrcodetran', unpacking.classifying('qrcodetran.20190116'))
    logout()