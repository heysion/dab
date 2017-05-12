#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-08-30
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import *
# from sqlalchemy.engine.url import URL
# from sqlalchemy.orm import sessionmaker

class SQLBase(object):
    def __new__(cls,*args,**kw):
        if not hasattr(cls,'_instace'):
            orig = super(SQLBase,cls)
            cls._instace = orig.__new__(cls,*args,**kw)
        return cls._instace

    def __init__(self,dbsetting):
        if not hasattr(self,"conn"):
            SQLBase.conn = create_engine(URL(**dbsetting))

    def getconn(self):
        if hasattr(self,"conn"):
            return SQLBase.conn
        else:
            return None
    pass

class PgConn(SQLBase):
    pass

class SqliteConn(SQLBase):
    pass
# engine = create_engine('sqlite:///dabdb.db')
# Base.metadata.bind = engine
# DBSession = sessionmaker(bind=engine)
"""
postgresql 0
sqlite3 1
"""
DATABASE = {
    'drivername': 'postgres',
    'host': '192.168.122.10',
    'port': '5432',
    'username': 'postgres',
    'password': 'qwe123',
    'database': 'dabdb'
}

def dbinit(dbtype="postgres",dbsetting=DATABASE):
    if dbtype == "postgres":
        db = PgConn(dbsetting)
        e = db.getconn()
        DBSession = sessionmaker(bind=e)
        session = DBSession()
        return (db,session)
    elif dbtype == "sqlite3":
        db = SqliteConn(dbsetting)
        e = db.getconn()
        DBSession = sessionmaker(bind=e)
        session = DBSession()
        return (db,session)
    else:
        return None

import pdb

from da.users import User
from da.host import Host
import da
    
def test_fill_data(session,e):
    User.metadata.create_all(e)
    Host.metadata.create_all(e)
    new_obj = User(name="test2",password="qwe123")
    session.add(new_obj)
    session.flush()
    new_host = Host(name=new_obj.name)
    new_host.user = new_obj
    # new_host = Host(name="host2",user_id=new_obj.id)
    session.add(new_host)
    session.commit()
    

if __name__ == "__main__":
    dbase = dbinit()
    e = dbase.getconn()
    DBSession = da.da_session(bind=e)
    session = DBSession()
    #test_fill_data(session,e)
    new_obj = User(name="test5",password="qwe123")
    # session.add(new_obj)
    # session.flush()
    # session.commit()
    new_host = Host(name=new_obj.name) 
    new_host.user = new_obj
    new_host.add_host(session)
    session.commit()
    #session.add(new_host)
    #session.commit()
    #test_fill_data(session,e)
    h,u = session.query(Host,User).filter(Host.user_id==User.id).first()
    print(h.__dict__)
    print(u.__dict__)
    print(dbase)
