#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-08-22
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
from peewee import CharField, BooleanField ,IntegerField
from peewee import ForeignKeyField

from dab.db import Base
from target import Target
from package import Package

class Source(Base):
    class Meta:
        db_table = "dscinfo"
    target_name = ForeignKeyField(Target, to_field="name", db_column='target_name')
    package_name = ForeignKeyField(Package, to_field="name", db_column="package_name")
    name = CharField()

    version = CharField()
    epoch = IntegerField(null=True)
    dsc_file = CharField()
    sha1sum = CharField(null=True)
    md5sum = CharField(64, null=True)
    filesize = IntegerField(null=True)
    description = CharField(null=True)

def run_test():
    Source.create_table()
    pkg = Source(target_name="deepin",package_name="deepin-auto-build",name="deepin-auto-build",version="0.1.1",dsc_file="deepin-auto-build.dsc")
    pkg.save(force_insert=True)

    pass
if __name__ == "__main__":
    run_test()
    pass    
