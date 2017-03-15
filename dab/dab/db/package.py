#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-08-13
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
from peewee import CharField, BooleanField
from peewee import ForeignKeyField

from dab.db import Base
from dab.db.target import Target

class Package(Base):
    class Meta:
        db_table = "pkginfo"
    name = CharField()
    target_name = ForeignKeyField(Target,to_field='name',db_column="target_name")
    enabled = BooleanField()


class Depends(Base):
    class Meta:
        db_table = "pkgdependsinfo"
    pkg_name = ForeignKeyField(Package,to_field="name",db_column="pkg_name")
    dep_name = CharField(null=False)


def run_test():
    Package.create_table()
    pkg = Package(name="test",target_name="deepin",enabled=False)
    pkg.save(force_insert=True)
    Depends.create_table()
    dep = Depends(pkg_name=pkg.name,dep_name=pkg.name)
    dep.save()

if __name__ == "__main__":
    run_test()
    pass    
