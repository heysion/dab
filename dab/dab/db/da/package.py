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
from build import Build
from source import Source

class Depends(Base):
    __tablename__ = 'pkgdependsinfo'
    id = Column(Integer, primary_key=True)
    pkg_name = Column(String(256), nullable=False, ForeignKey('pkgdependsinfo.name'))
    depend_name = Column(String(256), nullable=False)

class Package(Base):
    __tablename__ = 'pkginfo'
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    target_name = Column(String(256), ForeignKey('target.name'))
    #workdir = Column(String(256))
    enabled = Column(Boolean)
    # build_id = Column(Integer, ForeignKey('buildinfo.id'))
    # version = Column(String(256))
    # release = Column(String(256))
    # epoch = Column(Integer)
    # source = Column(String(256))
    # src_id = Column(Integer, ForeignKey('srcinfo.id'))
    # # depends = Column(String(1024))
    # chs_file = Column(String(256))
    # sha1sum = Column(String(256))
    # md5sum = Column(String(64))
    # filesize = Column(Integer)

def run_test():
    session = dainit(True)
    new_package = Package(name="test",version="xx.xx.xx")
    session.add(new_package)
    session.commit()

if __name__ == "__main__":
    run_test()
    pass    
