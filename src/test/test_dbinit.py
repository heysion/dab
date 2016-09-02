#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-09-02
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
from dabdb.dbconn import dbinit
from dabdb.da.target import Target



def test_fill_data_target(session,e):
    Target.metadata.create_all(e)
    new_obj = Target(name="deepinmips64el",suite="unstable",
                     codename="raccoon",architectures="mips64el",
                     workdir="/mnt/deepinmips64el")
    session.add(new_obj)
    session.commit()

if __name__ == "__main__":
    dbase,session = dbinit()
    e = dbase.getconn()
    test_fill_data_target(session,e)
                     
