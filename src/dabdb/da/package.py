#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-08-13
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
from sqlalchemy import Column, ForeignKey, Integer, String

from __init__ import Base,da_session,da_create_engine
from __init__ import da_init_test as dainit

class Package(Base):
    __tablename__ = 'pkginfo'
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    version = Column(String(256))
    build_ver = Column(String(256))
    build_freq = Column(Integer)


def run_test():
    session = dainit(True)
    new_package = Package(name="test",version="xx.xx.xx")
    session.add(new_package)
    session.commit()

if __name__ == "__main__":
    run_test()
    pass    
