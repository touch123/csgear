# -*- coding: utf-8 -*-

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import Configuration


# Configuration.db_path

engine = create_engine('sqlite:///aa.db?check_same_thread=False', echo=True)


Base = declarative_base()

from sqlalchemy import Column, Integer, String

class Postran(Base):
    __tablename__ = 'T_postran'
    
    rowid = Column(Integer, primary_key=True)
    pid = Column(String(10))
    filedate = Column(String(8))
    path = Column(String(40))
    rrn = Column(String(12))
    respcode = Column(String(2))
    countno = Column(String(27))
    termid = Column(String(8))
    mrchid = Column(String(15))
    traceno = Column(String(6))
    amount = Column(String(13))

    def __repr__(self):
        return "<Postran (pid='%s', path='%s', respcode='%s')>" % (
                   self.pid, self.path, self.respcode)

class Ictran(Base):
    __tablename__ = 'T_ictran'
    
    rowid = Column(Integer, primary_key=True)
    pid = Column(String(10))
    filedate = Column(String(8))
    path = Column(String(40))
    rrn = Column(String(12))
    respcode = Column(String(2))
    countno = Column(String(27))
    termid = Column(String(8))
    mrchid = Column(String(15))
    traceno = Column(String(6))
    amount = Column(String(13))

    def __repr__(self):
        return "<Ictran (pid='%s', path='%s', respcode='%s')>" % (
                   self.pid, self.path, self.respcode)

class Sign(Base):
    __tablename__ = 'T_sign'
    
    rowid = Column(Integer, primary_key=True)
    logtype = Column(String(10))
    filedate = Column(String(8))
    status = Column(String(40))

class Mis_clt(Base):
    __tablename__ = 'T_mis_clt'
    
    rowid = Column(Integer, primary_key=True)
    pid = Column(String(10))
    filedate = Column(String(8))
    path = Column(String(40))
    traceno = Column(String(6))
    amount = Column(String(13))
    termid = Column(String(8))

class QrCodetran(Base):
    __tablename__ = 'T_qrcodetran'
    
    rowid = Column(Integer, primary_key=True)
    pid = Column(String(10))
    filedate = Column(String(8))
    path = Column(String(40))
    rrn = Column(String(12))
    respcode = Column(String(2))
    countno = Column(String(27))
    termid = Column(String(8))
    mrchid = Column(String(15))
    traceno = Column(String(6))
    amount = Column(String(13))
    auth_code = Column(String(40))
    orderid = Column(String(50))

    def __repr__(self):
        return "<Postran (pid='%s', path='%s', respcode='%s')>" % (
                   self.pid, self.path, self.respcode)

class Qr_clt(Base):
    __tablename__ = 'qr_clt'
    
    rowid = Column(Integer, primary_key=True)
    pid = Column(String(10))
    filedate = Column(String(8))
    path = Column(String(40))
    traceno = Column(String(6))
    amount = Column(String(13))
    termid = Column(String(8))

Base.metadata.create_all(engine)

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


Session = sessionmaker(bind=engine)
session = Session()

"""
ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
session.add(ed_user)
session.commit()

mod_user = session.query(User).filter_by(name='ed').first()

# 将ed用户的密码修改为modify_paswd
mod_user.password = 'modify_passwd'


# 要删除需要先将记录查出来
del_user = session.query(User).filter_by(name='ed').first()

# 将ed用户记录删除
session.delete(del_user)


# 遍历查看，已无ed用户记录
for user in session.query(User):
    print(user)

our_user = session.query(User).filter_by(name='ed').first()
"""




def insert_dict_into_sql(logtype, dicts):
    print dicts
    for d in dicts:
        keys, values = zip(*d.items())
        insert_str = "INSERT INTO %s (%s) values (%s)" % (logtype, ",".join(keys), ",".join(['?'] * len(keys)))
        session.execute(insert_str, values)
    print "NOTICE: for total " + str(len(dicts)) + " files values has been added into table " + logtype + " in database."


def sign(fileDate, logType):
    session.execute('INSERT sign VALUES ("%s","%s","%s")' % (logType, fileDate, "1"))


def skip(logType, FileDate):
    aa = session.execute('SELECT * FROM sign WHERE logType= "%s" and FileDate = "%s"' % (logType, FileDate))
    return aa.fetchall()


def search(command):
    aa = session.execute(command)
    result = []
    for item in aa.fetchall():
        result.append(item[1])
    return result


def logout():
    session.close()


def getTable(logType):
    aa = session.execute('PRAGMA table_info([%s])' % logType)
    return aa.fetchall()


if __name__ == '__main__':
    # init()
    # logout()
