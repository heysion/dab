#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2017-03-30
@author: Heysion Yuan
@copyright: 2017, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
from dab.db import models

#from lib.util import find_subclasses
for mod in models.Base.__subclasses__():
    print mod
    if mod.table_exists():
        mod.drop_table()
    mod.create_table()
    print("create %s"%mod._meta.db_table)
