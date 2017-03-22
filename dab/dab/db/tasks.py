#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-08-15
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''

from datetime import datetime
from peewee import CharField, BooleanField ,IntegerField, DateTimeField
from peewee import ForeignKeyField

from dab.db import Base
from target import Target
from package import Package
from channels import Channel
from host import Host
from source import Source
from build import Build
from users import User

class Task(Base):
    class Meta:
        db_table = "taskinfo"
#    id = Column(Integer, primary_key=True)
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

    src_id = ForeignKeyField(Source,to_field="source_id",db_column="src_id",null=True)
    src_name = ForeignKeyField(Source,to_field="name",db_column="src_name",null=True)
    build_id = ForeignKeyField(Build,to_field="build_id",null=True)
    build_name = ForeignKeyField(Build,to_field="name",db_column="build_name",null=True)

    parent = IntegerField(null=True)
    label = CharField(null=True)
    waiting = BooleanField(null=True)
    awaited = BooleanField(null=True)
    owner = ForeignKeyField(User,to_field="id",db_column="ower_id",null=True)
    owner_name = ForeignKeyField(User,to_field="name",db_column="ower_name",null=True)
    arch = CharField(32)
    priority = IntegerField(default=-1)
    
    # def __init__(self,state=0,channel_name=None,host_name=None,src_id=None,):
    #     self.state = state
    #     self.channel_name = channel_name
    #     self.host_name = host_name
    #     self.src_id = src_id

    # @classmethod
    # def get_task_info_daemon(cls,session,channel_name,host_name):
    #     task_list = session.query(Task).filter(Task.channel_name==channel_name,
    #                                            Task.host_name==host_name).all()
    #     return task_list
    # def update_task_info(self):
    #     pass

def run_test():
    Task.create_table()
    obj = Task(name="test",target_name="deepin",enabled=False)
    obj.save(force_insert=True)

if __name__ == "__main__":
    run_test()
    pass    
