#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-08-14
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''

from sqlalchemy import Column, ForeignKey, Integer, String

from __init__ import Base,da_session,da_create_engine
from __init__ import da_init_test as dainit
from users import User

class Host(Base):
    __tablename__ = 'hostinfo'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('usersinfo.id'))
    name = Column(String(128))
    arches = Column(String(256))
    capacity = Column(Integer)
    description = Column(String(256))
    comment = Column(String(256))
    ready = Column(Integer)
    enabled = Column(Integer)

def run_test():
    session = dainit(True)
    new_obj = Host(name="test")
    session.add(new_obj)
    session.commit()

if __name__ == "__main__":
    run_test()
    pass    
