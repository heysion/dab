#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-08-14
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''

from sqlalchemy import Column, ForeignKey, Integer, String ,Boolean
from sqlalchemy.orm import relationship
from sqlalchemy import UniqueConstraint

from __init__ import Base,da_session,da_create_engine
from __init__ import da_init_test as dainit
from users import User
from dab.util.error import DabdbException

class Host(Base):
    __tablename__ = 'hostinfo'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('userinfo.id'))
    name = Column(String(128), nullable=False, unique=True)
    user = relationship("User",backref="hostinfo")
    arches = Column(String(256))
    capacity = Column(Integer)
    description = Column(String(256))
    comment = Column(String(256))
    ready = Column(Boolean)
    enabled = Column(Boolean)
    __table_args__= (UniqueConstraint("name",name="hostname_o_1"),)

    def add_host(self,session):
        if self.user == None:
            u = session.query(User).filter(User.name==self.name).first()
            if u == None:
                raise DabdbException("not found user name")
        session.add(self)
        session.flush()
        pass

def run_test():
    session = dainit(True)
    new_obj = Host(name="test")
    new_obj.add_host(session)
    session.commit()

if __name__ == "__main__":
    run_test()
    pass    
