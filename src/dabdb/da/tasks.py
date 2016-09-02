#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-08-15
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''

from sqlalchemy import Column, ForeignKey, Integer, String ,DateTime ,Time , Boolean
from sqlalchemy.orm import relationship
from sqlalchemy import UniqueConstraint
from datetime import datetime

from __init__ import Base,da_session,da_create_engine
from __init__ import da_init_test as dainit
from users import User
from channels import Channel
from host import Host
from source import Source
from build import Build


class Task(Base):
    __tablename__ = 'taskinfo'
    id = Column(Integer, primary_key=True)
    state = Column(Integer)
    # 0 init 100 submit 200 start 300 build 400 failed 500 success 
    create_time = Column(DateTime, nullable=False, default=datetime.now())
    start_time = Column(DateTime)
    completion_time = Column(DateTime)
    channel_id = Column(Integer,ForeignKey("channelinfo.id"))
    host_id = Column(Integer,ForeignKey("hostinfo.id"))
    src_id = Column(Integer,ForeignKey("srcinfo.id"))
    build_id = Column(Integer,ForeignKey("buildinfo.id"))
    parent = Column(Integer,nullable=True)
    label = Column(String(256))
    waiting = Column(Boolean)
    awaited = Column(Boolean)
    owner = Column(Integer,ForeignKey("userinfo.id"))
    arch = Column(String(32))
    priority = Column(Integer)
    
    user = relationship("User",backref="taskinfo")
    channel = relationship("Channel",backref="taskinfo")
    host = relationship("Host",backref="taskinfo")
    source = relationship("Source",backref="taskinfo")
    build = relationship("Build",backref="taskinfo")
    
    def __init__(self,state=0,channel_id=None,host_id=None,src_id=None):
        self.state = state
        self.channel_id = channel_id
        self.host_id = host_id
        self.src_id = src_id
        pass
    @classmethod
    def get_task_info_daemon(cls,session,channel_id,host_id):
        task_list = session.query(Task).filter(Task.channel_id==channel_id,Task.host_id==host_id).all()
        return task_list
    def update_task_info(self):
        pass

def run_test():
    session = dainit(True)
    new_obj = Host(name="test")
    session.add(new_obj)
    session.commit()

if __name__ == "__main__":
    run_test()
    pass    
