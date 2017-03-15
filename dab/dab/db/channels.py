#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-08-19
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy import UniqueConstraint

from __init__ import Base,da_session,da_create_engine
from __init__ import da_init_test as dainit

from host import Host
from target import Target

class Channel(Base):
    __tablename__ = 'channelinfo'
#    id = Column(Integer, primary_key=True)
    host_name = Column(String(256), ForeignKey('hostinfo.name'))
    target_name = Column(String(256), ForeignKey('targetinfo.name'))
    name = Column(String(256), primary_key=True, nullable=False)
    arches = Column(String(256))
    enabled = Column(Boolean)
    max_job = Column(Integer)
    curr_job = Column(Integer)
    
    host = relationship("Host",backref="channelinfo")
    target = relationship("Target",backref="channelinfo")

    @classmethod
    def update_channel_info(cls,session,channel_name,host_name,max_job,curr_job,state):
        channelinfo = session.query(Channel).filter(Channel.name==channel_name,
                                                    Channel.host_name==host_name).first()
        if channelinfo:
            channelinfo.max_job = max_job
            channel_id.curr_job = curr_job
            channel_id.enabled = state
            session.flush()
            session.commit()
            return True
        else:
            return False

def run_test():
    session = dainit(True)
    new_obj = Chananel(name="test")
    session.add(new_obj)
    session.commit()

if __name__ == "__main__":
    run_test()
    pass    