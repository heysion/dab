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


class Target(Base):
    __tablename__ = 'targetinfo'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    suite = Column(String(32))
    codename = Column(String(32))
    architectures = Column(String(256))
    description = Column(String(256))


def run_test():
    session = dainit(True)
    new_obj = Target(name="test")
    session.add(new_obj)
    session.commit()

if __name__ == "__main__":
    run_test()
    pass    
