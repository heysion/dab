#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-08-14
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''

# CREATE TABLE users (
# 	id SERIAL NOT NULL PRIMARY KEY,
# 	name VARCHAR(255) UNIQUE NOT NULL,
# 	password VARCHAR(255),
# 	status INTEGER NOT NULL,
# 	usertype INTEGER NOT NULL,
# 	krb_principal VARCHAR(255) UNIQUE
# ) WITHOUT OIDS;

from sqlalchemy import Column, ForeignKey, Integer, String

from __init__ import Base,da_session,da_create_engine
from __init__ import da_init_test as dainit

class Users(Base):
    __tablename__ = 'usersinfo'
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    password = Column(String(256))
    status = Column(Integer)
    usertype = Column(Integer)


def run_test():
    session = dainit(True)
    new_obj = Users(name="test")
    session.add(new_obj)
    session.commit()

if __name__ == "__main__":
    run_test()
    pass    
