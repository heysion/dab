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
from peewee import ForeignKeyField, PrimaryKeyField

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

class Build(Base):
    class Meta:
        db_table = "debinfo"
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

class Host(Base):
    class Meta:
        db_table = 'hostinfo'
    user_id = ForeignKeyField(User, to_field='id', db_column="user_id")
    user_name = CharField()
    #user_name = ForeignKeyField(User, to_field="name", db_column="user_name")
    name = CharField(primary_key=True, unique=True, db_column="name")
    arches = CharField()
    capacity = IntegerField(null=True)
    description = CharField(null=True)
    comment = CharField(null=True)
    ready = BooleanField()
    enabled = BooleanField()

class Channel(Base):
    class Meta:
        db_table = "channelinfo"
    name = CharField(primary_key=True)

    host_name = ForeignKeyField(Host,to_field='name',db_column="host_name")
    target_name = ForeignKeyField(Target,to_field='name',db_column="target_name")

    arches = CharField()
    enabled = BooleanField()
    max_job = IntegerField()
    curr_job = IntegerField()

class Task(Base):
    class Meta:
        db_table = "taskinfo"
    state = IntegerField(default=0)
    # 0 init 
    # 100 submit 
    # 200 start 
    # 300 build 
    # 400 failed 
    # 500 success 
    create_time = DateTimeField(default=datetime.now())
    start_time = DateTimeField(null=True)
    completion_time = DateTimeField(null=True)
    channel_name = ForeignKeyField(Channel,to_field='name',db_column="channel_name",null=True)
    host_name = ForeignKeyField(Host,to_field='name',db_column="hosts_name",null=True)

    src_id = ForeignKeyField(Source,to_field="id",related_name="task_src_id",db_column="src_id",null=True)
    src_name = ForeignKeyField(Source,to_field="name",db_column="src_name",null=True)
    build_id = ForeignKeyField(Build,to_field="id",related_name="task_build_id",null=True)
    build_name = ForeignKeyField(Build,to_field="name",db_column="build_name",null=True)

    parent = IntegerField(null=True)
    label = CharField(null=True)
    waiting = BooleanField(null=True)
    awaited = BooleanField(null=True)
    owner = ForeignKeyField(User,to_field="id",related_name="task_owner_id",db_column="ower_id",null=True)
    owner_name = ForeignKeyField(User,to_field="name",db_column="ower_name",null=True)
    arch = CharField(32)
    priority = IntegerField(default=-1)

class Repo(Base):
    class Meta:
        db_table = "repoinfo"
    name = ForeignKeyField(RepoCtl,to_field="name",db_column="repctl_name")
    repoctl_name = CharField()
    update_time = DateTimeField(default=datetime.now())
    repo_config = CharField()
    enabled = BooleanField()

def run_test():
    Target.create_table()
    tt = Target(name="abc",suite="abc",codename="a1")
    tt.save(force_insert=True)

if __name__ == "__main__":
    run_test()
    pass    
