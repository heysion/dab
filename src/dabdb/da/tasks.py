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
    state = Column(Integer,default=0)
    # 0 init 100 submit 200 start 300 build 400 failed 500 success 
    create_time = Column(DateTime, nullable=False, default=datetime.now())
    start_time = Column(DateTime)
    completion_time = Column(DateTime)
    channel_name= Column(String(256),ForeignKey("channelinfo.name"))
    host_name = Column(String(256),ForeignKey("hostinfo.name"))
    src_id = Column(Integer,ForeignKey("srcinfo.id"))
    build_name = Column(String(256),ForeignKey("buildinfo.name"))
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
    
    # def __init__(self,state=0,channel_name=None,host_name=None,src_id=None,):
    #     self.state = state
    #     self.channel_name = channel_name
    #     self.host_name = host_name
    #     self.src_id = src_id

    @classmethod
    def get_task_info_daemon(cls,session,channel_name,host_name):
        task_list = session.query(Task).filter(Task.channel_name==channel_name,
                                               Task.host_name==host_name).all()
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
