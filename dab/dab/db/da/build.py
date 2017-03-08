#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-08-15
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy import UniqueConstraint

from __init__ import Base,da_session,da_create_engine
from __init__ import da_init_test as dainit
from target import Target

class Build(Base):
    __tablename__ = 'debinfo'
    id = Column(Integer, primary_key=True)
    target_name = Column(String(256), ForeignKey('targetinfo.name'))
    package_name = Column(String(256), ForeignKey('pkginfo.name'))
    name = Column(String(256))

    arches = Column(String(256))
    version = Column(String(256), nullable=False)
    epoch = Column(Integer)
    chs_file = Column(String(256), nullable=False)
    sha1sum = Column(String(256))
    md5sum = Column(String(64))
    filesize = Column(Integer)
    description = Column(String(256))

#    target = relationship("Target",backref="buildinfo")

    __table_args__ = (UniqueConstraint("name",name="buildname_o_1"),)

def run_test():
    session = dainit(True)
    new_obj = Build(name="test")
    session.add(new_obj)
    session.commit()

if __name__ == "__main__":
    run_test()
    pass    
