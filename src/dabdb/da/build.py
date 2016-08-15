#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-08-15
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
from sqlalchemy import Column, ForeignKey, Integer, String

from __init__ import Base,da_session,da_create_engine
from __init__ import da_init_test as dainit
from package import Package
from task import Task


# CREATE TABLE build (
# 	id SERIAL NOT NULL PRIMARY KEY,
#         volume_id INTEGER NOT NULL REFERENCES volume (id),
# 	pkg_id INTEGER NOT NULL REFERENCES package (id) DEFERRABLE,
# 	version TEXT NOT NULL,
# 	release TEXT NOT NULL,
# 	epoch INTEGER,
# 	source TEXT,
# 	create_event INTEGER NOT NULL REFERENCES events(id) DEFAULT get_event(),
# 	start_time TIMESTAMP,
# 	completion_time TIMESTAMP,
# 	state INTEGER NOT NULL,
# 	task_id INTEGER REFERENCES task (id),
# 	owner INTEGER NOT NULL REFERENCES users (id),
# 	extra TEXT,
# 	CONSTRAINT build_pkg_ver_rel UNIQUE (pkg_id, version, release),
# 	CONSTRAINT completion_sane CHECK ((state = 0 AND completion_time IS NULL) OR
#                                           (state != 0 AND completion_time IS NOT NULL))
# ) WITHOUT OIDS;


class Build(Base):
    __tablename__ = 'buildinfo'
    id = Column(Integer, primary_key=True)
    pkg_id = Column(Integer, ForeignKey('pkginfo.id'))
    version = Column(String(256))
    release = Column(String(256))
    epoch = Column(Integer)
    source = Column(String(256))
    release = Column(String(256))
    task_id = Column(Integer, ForeignKey('taskinfo.id'))
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
