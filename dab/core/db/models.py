#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2017-03-22
@author: Heysion Yuan
@copyright: 2017, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
from datetime import datetime

from peewee import CharField, BooleanField ,IntegerField, DateTimeField
from peewee import ForeignKeyField, PrimaryKeyField, CompositeKey

from dab.core.db import Base

class User(Base):
    """
    User db model:
        uid - user id
        name - user name
        password - user password
        ssalt - password salt
        status - user status
        usertype - user type
        is_admin - admin flag
    """
    class Meta:
        db_table = 'userinfo'
    
    uid = PrimaryKeyField(unique=True,index=True,db_column="uid")
    name = CharField(unique=True)
    password = CharField()
    ssalt = CharField()
    status = IntegerField(null=True)
    usertype = IntegerField(null=True)
    is_admin = BooleanField(default=False)

class Target(Base):
    class Meta:
        db_table = 'targetinfo'

    name = CharField(primary_key=True)
    suite = CharField(32,null=True)
    codename = CharField(32)
    architectures = CharField(null=True)
    workdir = CharField(null=True)
    description = CharField(null=True)

class Package(Base):
    class Meta:
        db_table = "pkginfo"

    target_name = ForeignKeyField(
        Target,
        to_field='name',
        db_column="target_name")

    name = CharField(index=True,unique=True) 
    enabled = BooleanField()
    workdir = CharField(null=True)

class Depends(Base):
    class Meta:
        db_table = "pkgdependsinfo"

    pkg_name = ForeignKeyField(
        Package,
        to_field="name",
        related_name="pkg_name_depends",
        db_column="pkg_name",
        null=True)
    dep_name = CharField()

class Task(Base):
    class Meta:
        db_table = "taskinfo"

    """0 init 100 submit 200 start 300 build  400 failed 500 success """
    build_id = IntegerField(unique=True)
    state = IntegerField(default=0)
    create_time = DateTimeField(default=datetime.now())
    start_time = DateTimeField(null=True)
    completion_time = DateTimeField(null=True)

    target_name = ForeignKeyField(
        Target,
        to_field='name',
        db_column="target_name",
        related_name="tag_name_task")

    pkg_name = ForeignKeyField(
        Package,
        to_field="name",
        related_name="pkg_name_task",
        db_column="pkg_name")

    dsc_file = CharField(null=True)
    version = CharField(null=True)
    epoch = IntegerField(null=True)
    arch = CharField(32,null=True)
    chs_file = CharField(null=True)
    sha1sum = CharField(128, null=True)
    md5sum = CharField(64, null=True)
    filesize = IntegerField(null=True)
    description = CharField(null=True)

    parent = IntegerField(null=True)
    label = CharField(null=True)
    waiting = BooleanField(null=True)
    awaited = BooleanField(null=True)
    owner = ForeignKeyField(
        User,
        to_field="uid",
        related_name="uid_task",
        db_column="ower_id")

    owner_name = ForeignKeyField(
        User,
        to_field="name",
        db_column="ower_name",
        related_name="user_name_task",
        null=True)
    priority = IntegerField(default=-1)
    cycle_count = IntegerField(default=0)

class Repo(Base):
    class Meta:
        db_table = "repoinfo"

    name = CharField(primary_key=True,unique=True)
    update_time = DateTimeField(default=datetime.now())
    repo_config = CharField()
    enabled = BooleanField()

class RepoCtl(Base):
    class Meta:
        db_table = "repoctl"

    name = ForeignKeyField(
        Repo,
        to_field="name",
        db_column="repo_name",
        related_name="repo_name_repoctl",
        unique=True,
        index=True)

    package_name = ForeignKeyField(
        Package,
        to_field="name",
        db_column="pkg_name",
        related_name="pkg_name_repoctl",
        null=True)
    version = CharField()

class MkisoInfo(Base):
    class Meta:
        db_table = "mkisoinfo"
    
    isoname = CharField(unique=True)
    create_time = DateTimeField(default=datetime.now())
    update_time = DateTimeField(default=datetime.now())
    preseed_config = CharField()
    status = IntegerField(null=True)
    includelist = CharField(null=True)
    excludelist = CharField(null=True)

def run_test():
    Target.create_table()
    tt = Target(name="abc",suite="abc",codename="a1")
    tt.save(force_insert=True)

if __name__ == "__main__":
    run_test()
    pass    
