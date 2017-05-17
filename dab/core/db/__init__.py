#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-08-13
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
import os
import sys

from peewee import *

#db = SqliteDatabase('dabdb.db')
database_proxy = Proxy()  # Create a proxy for our db.
# print("#FIXME")
# pysettings_path="/home/ndk/deepin-work/src-code-repo/deepin-auto-build/etc/dbconfig.py"
# if os.path.exists(pysettings_path):
#     print("load "+os.path.basename(pysettings_path)+" found")
#     sys.path.append(os.path.dirname(pysettings_path))
#     from settings import EnvDabsv

class Base(Model):
    class Meta:
        database = database_proxy


