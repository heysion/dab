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

from dab import deb822

import sys
import os.path

import pdb

def get_dsc_info(dscfile):
    dsc_info = deb822.Dsc(file(dscfile))
    return dsc_info

def _add_buildpkg(session,e,pkgname,pkgversion,pkgdsc,hostname=None):
    target = session.query(Target).filter(Target.name=="deepinmips64el").first()
    if target is  None:
        print("not found target")
        return
    
    build = session.query(Build).filter(Build.name==pkgname).first()
    if build is None:
        new_build = Build(target_name=target.name,name=pkgname,
                      arches="mips64el",enabled=True)
        session.add(new_build)
        build = new_build

    new_source = Source(build_name=build.name, target_name=build.target_name,
                        name=pkgname, version=pkgversion,
                        dsc_file=pkgdsc)
    session.add(new_source)
    if hostname is None:
        channelinfo = session.query(Channel).filter(Channel.target_name=="deepinmips64el",
                                                    Channel.arches==build.arches).order_by(
                                                        desc(Channel.curr_job)).first()
    else:
        channelinfo = session.query(Channel).filter(Channel.target_name=="deepinmips64el",
                                                    Channel.arches==build.arches,
                                                    Channel.host_name==hostname).order_by(
                                                        desc(Channel.curr_job)).first()

    new_task = Task(host_name=channelinfo.host_name)
    new_task.channel = channelinfo
    new_task.build = build
    new_task.source = new_source
    session.add(new_task)

    session.commit()

    pass

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print(sys.argv)
        if sys.argv[1] == "newtask":
            dsc_absolute_path = sys.argv[2]
            dsc_file = os.path.basename(dsc_absolute_path)
            
            if (dsc_file.split(".")[-1]).upper() in "DSC" and os.path.isfile(dsc_absolute_path) :
                dsc_info = get_dsc_info(dsc_absolute_path)
                dbase,session = dbinit()
                e = dbase.getconn()
                if len(sys.argv) == 4:
                    _add_buildpkg(session,e,
                                  dsc_info['Source'],dsc_info['Version'],
                                  dsc_file,hostname=sys.argv[3])
                else:
                    _add_buildpkg(session,e,
                                  dsc_info['Source'],dsc_info['Version'],
                                  dsc_file)

            else:
                print("input dsc file")
    else:
        print("run /path/xx.dsc")
    
