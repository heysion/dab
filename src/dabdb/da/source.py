#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-08-22
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
from sqlalchemy import Column, ForeignKey, Integer, String

from __init__ import Base,da_session,da_create_engine
from __init__ import da_init_test as dainit
from build import Build

class Source(Base):
    __tablename__ = 'srcinfo'
    id = Column(Integer, primary_key=True)
    build_id = Column(Integer, ForeignKey('buildinfo.id'))
    name = Column(String(256))
    version = Column(String(256))
    epoch = Column(Integer)
    release = Column(String(256))
    suite = Column(String(32))
    dsc_file = Column(String(256))
    depends = Column(String(1024))
    workdir = Column(String(256))
    description = Column(String(256))


def run_test():
    session = dainit(True)
    new_obj = Target(name="test")
    session.add(new_obj)
    session.commit()

if __name__ == "__main__":
    run_test()
    pass    
