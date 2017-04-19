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
    
    user_id = PrimaryKeyField(unique=True,index=True,db_column="d")
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
    suite = CharField(32)
    codename = CharField(32, unique=True)
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

    name = CharField() 
    enabled = BooleanField()


class Depends(Base):
    class Meta:
        db_table = "pkgdependsinfo"

    pkg_name = ForeignKeyField(
        Package,
        to_field="name",
        related_name="pkg_name_depends",
        db_column="pkg_name")
    dep_name = CharField(null=False)

class Source(Base):
    class Meta:
        db_table = "dscinfo"

    sid = PrimaryKeyField(unique=True,index=True,db_column="sid")
    target_name = ForeignKeyField(
        Target,
        to_field="name",
        db_column='target_name',
        related_name="target_name_source")

    package_name = ForeignKeyField(
        Package,
        to_field="name",
        db_column="package_name",
        related_name="pkg_name_source")

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

    bid = PrimaryKeyField(unique=True,index=True,db_column="bid")
    target_name = ForeignKeyField(
        Target,
        to_field="name",
        db_column='target_name',
        related_name="target_name_build")

    package_name = ForeignKeyField(
        Package,
        to_field="name",
        db_column="package_name",
        related_name="pkg_name_build")

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

    uid = ForeignKeyField(
        User,
        to_field='uid',
        db_column="uid",
        related_name="uid_host")
    
    user_name = ForeignKeyField(
        User,
        to_field="name",
        db_column="user_name",
        related_name="uname_host")
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

    """0 init 100 submit 200 start 300 build  400 failed 500 success """
    state = IntegerField(default=0)
    create_time = DateTimeField(default=datetime.now())
    start_time = DateTimeField(null=True)
    completion_time = DateTimeField(null=True)

    channel_name = ForeignKeyField(
        Channel,
        to_field='name',
        db_column="channel_name",
        related_name="chnl_name_task",
        null=True)

    host_name = ForeignKeyField(
        Host,
        to_field='name',
        db_column="hosts_name",
        related_name="host_name_task",null=True)

    src_id = ForeignKeyField(
        Source,
        to_field="sid",
        related_name="sid_task",
        db_column="sid",
        null=True)
    src_name = ForeignKeyField(
        Source,
        to_field="name",
        db_column="src_name",
        related_name="src_name_task",
        null=True)
    build_id = ForeignKeyField(
        Build,
        to_field="bid",
        related_name="bid_task",
        null=True)
    build_name = ForeignKeyField(
        Build,
        to_field="name",
        db_column="build_name",
        related_name="build_name_task",
        null=True)

    parent = IntegerField(null=True)
    label = CharField(null=True)
    waiting = BooleanField(null=True)
    awaited = BooleanField(null=True)
    owner = ForeignKeyField(
        User,
        to_field="uid",
        related_name="uid_task",
        db_column="ower_id",
        null=True)
    owner_name = ForeignKeyField(
        User,
        to_field="name",
        db_column="ower_name",
        related_name="user_name_task",
        null=True)
    arch = CharField(32)
    priority = IntegerField(default=-1)

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
        related_name="repo_name_repoctl"
        unique=True,
        index=True)

    package_name = ForeignKeyField(
        Package,
        to_field="name",
        db_column="pkg_name",
        related_name="pkg_name_repoctl")
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
