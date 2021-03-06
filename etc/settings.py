#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2017-03-27
@author: Heysion Yuan
@copyright: 2017, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
from playhouse.pool import PooledSqliteDatabase

database_config = {
    "DBTYPE":"PG",
    "DBINSTNCE":"dabdb",
    "DBHOST":"127.0.0.1",
    "DBPORT":6379,
    "DBNMAE":"postgres",
    "DBPASSWD":"qwe123",
}

class EnvBase(object):
    def __new__(cls,*args,**kw):
        if not hasattr(cls,"_instance"):
            orig = super(EnvBase, cls)
            cls._instace = orig.__new__(cls, *args, **kw)
        return cls._instace
    def __init__(self,config):
        return None
        pass

database = EnvBase(database_config)
# class EnvBase(object):
#     def __new__(cls,*args,**kw):
#         if not hasattr(cls,"_instance"):
#             orig = super(EnvBase, cls)
#             cls._instace = orig.__new__(cls, *args, **kw)
#         return cls._instace

#     @classmethod
#     def getdatabase(cls,dbname="dabdb.db"):
#         if not hasattr(cls,"_database"):
#             cls._database = PooledSqliteDatabase(dbname)
#         return cls._database

#     @classmethod
#     def setdatabase(cls,dbname="dabdb.db"):
#         if not hasattr(cls,"_instance"):
#             orig = super(EnvBase, cls)
#             cls._instace = orig.__new__(cls, *args, **kw)

#         if not hasattr(cls,"_database"):
#             cls._database = PooledSqliteDatabase(dbname)
#         return cls._database 
            
#     pass

# class EnvDabsv(EnvBase):
#     pass
