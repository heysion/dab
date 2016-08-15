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
from users import Users
from channels import Channel

# CREATE TABLE task (
# 	id SERIAL NOT NULL PRIMARY KEY,
# 	state INTEGER,
# 	create_time TIMESTAMP NOT NULL DEFAULT NOW(),
# 	start_time TIMESTAMP,
# 	completion_time TIMESTAMP,
# 	channel_id INTEGER NOT NULL REFERENCES channels(id),
# 	host_id INTEGER REFERENCES host (id),
# 	parent INTEGER REFERENCES task (id),
# 	label VARCHAR(255),
# 	waiting BOOLEAN,
# 	awaited BOOLEAN,
# 	owner INTEGER REFERENCES users(id) NOT NULL,
# 	method TEXT,
# 	request TEXT,
# 	result TEXT,
# 	eta INTEGER,
# 	arch VARCHAR(16) NOT NULL,
# 	priority INTEGER,
# 	weight FLOAT CHECK (NOT weight < 0) NOT NULL DEFAULT 1.0,
# 	CONSTRAINT parent_label_sane CHECK (
# 		parent IS NOT NULL OR label IS NULL),
# 	UNIQUE (parent,label)
# ) WITHOUT OIDS;

class Task(Base):
    __tablename__ = 'taskinfo'
    id = Column(Integer, primary_key=True)
    state = Column(Integer)
    create_time = Column(DateTime)
    start_time = Column(DateTime)
    completion_time = Column(DateTime)
    channel_id = Column(Integer,ForeignKey("channelinfo.id"))
    host_id = Column(Integer,ForeignKey("hostinfo.id"))
    parent = Column(Integer,ForeignKey("task.id"))
    label = Column(String(256))
    waiting = Column(Boolean))
    awaited = Column(Boolean))
    owner = Column(Integer,ForeignKey("userinfo.id"))
    method = Column(String(256))
    request = Column(String(256))
    result = Column(String(256))
    eta = Column(Integer)
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
