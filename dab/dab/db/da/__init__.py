#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-08-13
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
import os
import sys


from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
Base = declarative_base()
da_create_engine = create_engine
da_session = sessionmaker

def da_init_test(create_all=False):
    engine = da_create_engine('sqlite:///dabdb.db')
    if create_all:
        Base.metadata.create_all(engine)
    Base.metadata.bind = engine
    DBSession =  da_session(bind=engine)
    session = DBSession()
    return session

class Test:
    pass
