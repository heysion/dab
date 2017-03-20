#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-08-19
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
from datetime import datetime
from peewee import CharField, BooleanField ,IntegerField, DateTimeField
from peewee import ForeignKeyField

from dab.db import Base
from target import Target
from host import Host

class Channel(Base):
    class Meta:
        db_table = "channelinfo"
    name = CharField(primary_key=True)

    host_name = ForeignKeyField(Host,to_filed='name',db_column="host_name")
    target_name = ForeignKeyField(Target,to_filed='name',db_column="target_name")

    arches = CharField()
    enabled = BooleanField()
    max_job = IntegerField()
    curr_job = IntegerField()
    
    # @classmethod
    # def update_channel_info(cls,session,channel_name,host_name,max_job,curr_job,state):
    #     channelinfo = session.query(Channel).filter(Channel.name==channel_name,
    #                                                 Channel.host_name==host_name).first()
    #     if channelinfo:
    #         channelinfo.max_job = max_job
    #         channel_id.curr_job = curr_job
    #         channel_id.enabled = state
    #         session.flush()
    #         session.commit()
    #         return True
    #     else:
    #         return False

def run_test():
    session = dainit(True)
    new_obj = Chananel(name="test")
    session.add(new_obj)
    session.commit()

if __name__ == "__main__":
    run_test()
    pass    
