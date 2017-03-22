#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-08-14
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''

from peewee import CharField, BooleanField, IntegerField
from peewee import ForeignKeyField

from dab.db import Base

class User(Base):
    class Meta:
        db_table = 'userinfo'
    name = CharField(unique=True)
    password = CharField()
    ssalt = CharField()
    status = IntegerField(null=True)
    usertype = IntegerField(null=True)
    is_admin = BooleanField(default=False)

def run_test():
    pass
    # session = dainit(True)
    # new_obj = User(name="test",password="qwe123")
    # session.add(new_obj)
    # session.commit()

if __name__ == "__main__":
    run_test()
    pass    
