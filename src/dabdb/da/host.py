#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-08-14
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
# CREATE TABLE host (
# 	id SERIAL NOT NULL PRIMARY KEY,
# 	user_id INbTEGER NOT NULL REFERENCES users (id),
# 	name VARCHAR(128) UNIQUE NOT NULL,
# 	arches TEXT,
# 	task_load FLOAT CHECK (NOT task_load < 0) NOT NULL DEFAULT 0.0,
# 	capacity FLOAT CHECK (capacity > 1) NOT NULL DEFAULT 2.0,
# 	description TEXT,
# 	comment TEXT,
# 	ready BOOLEAN NOT NULL DEFAULT 'false',
# 	enabled BOOLEAN NOT NULL DEFAULT 'true'
# ) WITHOUT OIDS;

from sqlalchemy import Column, ForeignKey, Integer, String

from __init__ import Base,da_session,da_create_engine
from __init__ import da_init_test as dainit
from users import Users

class Host(Base):
    __tablename__ = 'hostinfo'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(256), ForeignKey('usersinfo.id'))
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
