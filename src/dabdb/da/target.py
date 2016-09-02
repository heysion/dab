#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-08-19
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
from sqlalchemy import Column, ForeignKey, Integer, String

from __init__ import Base,da_session,da_create_engine
from __init__ import da_init_test as dainit
from sqlalchemy.orm import relationship
from sqlalchemy import UniqueConstraint

class Target(Base):
    __tablename__ = 'targetinfo'
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    suite = Column(String(32), nullable=False)
    codename = Column(String(32), nullable=False)
    architectures = Column(String(256))
    workdir = Column(String(256))
    description = Column(String(256))

    __table_args__= (UniqueConstraint("name",name="targetname_u_1"),
                     UniqueConstraint("codename",name="targetcodename_u_1"),)


def run_test():
    session = dainit(True)
    new_obj = Target(name="test")
    session.add(new_obj)
    session.commit()

if __name__ == "__main__":
    run_test()
    pass    
