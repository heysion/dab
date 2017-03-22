#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-08-15
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
from peewee import CharField, BooleanField ,IntegerField
from peewee import ForeignKeyField, PrimaryKeyField

from dab.db import Base
from target import Target
from package import Package

class Build(Base):
    class Meta:
        db_table = "debinfo"
    build_id = PrimaryKeyField(db_column="build_id")
    target_name = ForeignKeyField(Target, to_field="name", db_column='target_name')
    package_name = ForeignKeyField(Package, to_field="name", db_column="package_name")
    name = CharField(unique=True)

    arches = CharField()
    version = CharField()
    epoch = IntegerField(null=True)
    chs_file = CharField()
    sha1sum = CharField(128, null=True)
    md5sum = CharField(64, null=True)
    filesize = IntegerField(null=True)
    description = CharField(null=True)


def run_test():
    Build.create_table()
    pkg = Build(target_name="deepin",package_name="deepin-auto-build",name="deepin-auto-build",version="0.1.1",chs_file="deepin-auto-build.changes",arches="amd64")
    pkg.save(force_insert=True)

if __name__ == "__main__":
    run_test()
    pass    
