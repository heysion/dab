#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-08-19
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
from sqlalchemy import Column, ForeignKey, Integer, String

from __init__ import Base,da_session,da_create_engine
from __init__ import da_init_test as dainit

from host import Host
from target import Target

class Channel(Base):
    __tablename__ = 'channelinfo'
    id = Column(Integer, primary_key=True)
    host_id = Column(Integer, ForeignKey('hostinfo.id'))
    target_id = Column(Integer, ForeignKey('targetinfo.id'))
    name = Column(String(256))
    arches = Column(String(256))
    enabled = Column(Integer)
    max_job = Column(Integer)
    curr_job = Column(Integer)

def run_test():
    session = dainit(True)
    new_obj = Chananel(name="test")
    session.add(new_obj)
    session.commit()

if __name__ == "__main__":
    run_test()
    pass    
