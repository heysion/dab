#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-08-19
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
from datetime import datetime
from peewee import CharField, BooleanField, DateTimeField
from peewee import ForeignKeyField

from dab.db import Base
from dab.db.package import Package

class RepoCtl(Base):
    class Meta:
        db_table = "repoctl"
    name = CharField(primary_key=True) 
    package_name = ForeignKeyField(Package,to_field="name",db_column="package_name")
    version = CharField()

class Repo(Base):
    class Meta:
        db_table = "repoinfo"
    name = ForeignKeyField(RepoCtl,to_field="name",db_column="repctl_name")
    repoctl_name = CharField()
    update_time = DateTimeField(default=datetime.now())
    repo_config = CharField()
    enabled = BooleanField()
    

def run_test():
    pass
    # session = dainit(True)
    # new_obj = Repo(name="test")
    # session.add(new_obj)
    # session.commit()

if __name__ == "__main__":
    run_test()
    pass
