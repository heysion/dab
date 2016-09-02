#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-09-02
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
from sqlalchemy import desc

from dabdb.dbconn import dbinit
from dabdb.da.target import Target
from dabdb.da.users import User
from dabdb.da.host import Host
from dabdb.da.channels import Channel
from dabdb.da.build import Build
from dabdb.da.source import Source
from dabdb.da.tasks import Task

def test_fill_data_target(session,e):
    Target.metadata.create_all(e)
    new_obj = Target(name="deepinmips64el",suite="unstable",
                     codename="raccoon",architectures="mips64el",
                     workdir="/mnt/deepinmips64el")
    session.add(new_obj)
    session.commit()

def test_fill_data_user(session,e):
    User.metadata.create_all(e)
    new_obj = User(name="dptest",password="qwe123")
    session.add(new_obj)
    session.commit()
    
def test_fill_data_host(session,e):
    Host.metadata.create_all(e)
    user = session.query(User).filter(User.name=="dptest").first()
    new_obj = Host(name="dptest",user_id=user.id,arches="mips64el",capacity=10,ready=True,enabled=True)
    session.add(new_obj)
    session.commit()

def test_fill_data_channel(session,e):
    Channel.metadata.create_all(e)
    target = session.query(Target).filter(Target.name=="deepinmips64el").first()
    host = session.query(Host).filter(Host.name=="dptest").first()
    new_obj = Channel(host_id=host.id,target_id=target.id,
                      arches="mips64el",enabled=True,
                      max_job=10,curr_job=0,
                      name=host.name)
    session.add(new_obj)
    session.commit()
    
def test_fill_base_data(session,e):
    test_fill_data_target(session,e)
    test_fill_data_user(session,e)
    test_fill_data_host(session,e)
    test_fill_data_channel(session,e)

def test_add_build(session,e):
    Build.metadata.create_all(e)
    target = session.query(Target).filter(Target.name=="deepinmips64el").first()
    new_obj = Build(target_id=target.id,name="mbr",
                    arches="mips64el",enabled=True)
    session.add(new_obj)
    session.commit()

def test_add_source(session,e):
    Source.metadata.create_all(e)
    build = session.query(Build).filter(Build.name=="mbr").first()
    print(build.__dict__)
    new_obj = Source(build_id=build.id, target_id=build.target_id,
                     name="mbr", version="1.1.11-5",
                     dsc_file="mbr_1.1.11-5.dsc")
    session.add(new_obj)
    session.commit()

def test_data_init(session,e):
    test_add_build(session,e)
    test_add_source(session,e)

def test_add_task(session,e):
    Task.metadata.create_all(e)
    srcinfo = session.query(Source).filter(Source.name=="mbr",
                                           Source.version=="1.1.11-5").first()
    buildinfo = session.query(Build).filter(Build.name=="mbr",
                                            Build.target_id==srcinfo.target_id).first()
    channelinfo = session.query(Channel).filter(Channel.target_id==srcinfo.target_id,
                                                Channel.arches==buildinfo.arches).order_by(desc(Channel.curr_job)).first()
    print(channelinfo.__dict__)
    print(srcinfo.__dict__)
    print(buildinfo.__dict__)
    new_obj = Task(channel_id=channelinfo.id,host_id=channelinfo.host_id,src_id=srcinfo.id)
    session.add(new_obj)
    session.commit()
    pass

if __name__ == "__main__":
    dbase,session = dbinit()
    e = dbase.getconn()
    test_add_task(session,e)
    #test_data_init(session,e)
    
