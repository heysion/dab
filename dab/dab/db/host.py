#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-08-14
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
from peewee import CharField, BooleanField ,IntegerField
from peewee import ForeignKeyField

from dab.db import Base
from users import User
from dab.util.error import DabdbError

class Host(Base):
    class Meta:
        db_table = 'hostinfo'
    user_id = ForeignKeyField(User, to_field='id',db_column="user_id")
    name = CharField(primary_key=True, unique=True)
    user_name = ForeignKeyField(User,to_field="name",db_column="user_name")
    arches = CharField()
    capacity = IntegerField(null=True)
    description = CharField(null=True)
    comment = CharField(null=True)
    ready = BooleanField()
    enabled = BooleanField()

    # def add_host(self,session):
    #     if self.user is None:
    #         u = session.query(User).filter(User.name==self.name).first()
    #         if u is None:
    #             raise DabdbError("not found user name")
    #     session.add(self)
    #     session.flush()
    #     pass

def run_test():
    Host.create_table()
    pkg = Host(user_name="deepin",name="x86build-amd64",arches="amd64",version="0.1.1",dsc_file="deepin-auto-build.dsc")
    pkg.save(force_insert=True)

    # session = dainit(True)
    # new_obj = Host(name="test")
    # new_obj.add_host(session)
    # session.commit()

if __name__ == "__main__":
    run_test()
    pass    
