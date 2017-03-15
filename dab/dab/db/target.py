#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-08-19
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
from peewee import CharField
from dab.db import Base
import pdb

class Target(Base):
    class Meta:
        db_table = 'targetinfo'
    name = CharField(primary_key=True)
    suite = CharField(32)
    codename = CharField(32, unique=True)
    architectures = CharField(null=True)
    workdir = CharField(null=True)
    description = CharField(null=True)

def run_test():
    Target.create_table()
    tt = Target(name="abc",suite="abc",codename="a1")
    tt.save(force_insert=True)

if __name__ == "__main__":
    run_test()
    pass    
