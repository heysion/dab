#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-08-15
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''

from sqlalchemy import Column, ForeignKey, Integer, String ,DateTime ,Time , Boolean

from __init__ import Base,da_session,da_create_engine
from __init__ import da_init_test as dainit
from users import User
from channels import Channel
from  host import Host
from source import Source

class Task(Base):
    __tablename__ = 'taskinfo'
    id = Column(Integer, primary_key=True)
    state = Column(Integer)
    create_time = Column(DateTime, nullable=False, default=datetime.now())
    start_time = Column(DateTime)
    completion_time = Column(DateTime)
    channel_id = Column(Integer,ForeignKey("channelinfo.id"))
    host_id = Column(Integer,ForeignKey("hostinfo.id"))
    parent = Column(Integer,ForeignKey("task.id"))
    src_id = Column(Integer,ForeignKey("srcinfo.id"))
    label = Column(String(256))
    waiting = Column(Boolean)
    awaited = Column(Boolean)
    owner = Column(Integer,ForeignKey("userinfo.id"))
    arch = Column(String(32))
    priority = Column(Integer)

def run_test():
    session = dainit(True)
    new_obj = Host(name="test")
    session.add(new_obj)
    session.commit()

if __name__ == "__main__":
    run_test()
    pass    
