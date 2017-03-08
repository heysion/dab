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
#from build import Build

class Source(Base):
    __tablename__ = 'dscinfo'
    id = Column(Integer, primary_key=True)
    target_name = Column(String(256), ForeignKey('targetinfo.name'))
    package_name = Column(String(256), ForeignKey('pkginfo.name'))
    name = Column(String(256), nullable=False)

    version = Column(String(256), nullable=False)
    epoch = Column(Integer)
    dsc_file = Column(String(256), nullable=False)
    sha1sum = Column(String(256))
    md5sum = Column(String(64))
    filesize = Column(Integer)
    description = Column(String(256))


def run_test():
    session = dainit(True)
    new_obj = Target(name="test")
    session.add(new_obj)
    session.commit()

if __name__ == "__main__":
    run_test()
    pass    
