#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2017-03-24
@author: Heysion Yuan
@copyright: 2017, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''

import argparse
import sys
import settings
import os

from peewee import PostgresqlDatabase
def _mkdir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        print("create :{} directory".format(dir_path))

def initdir():
    _mkdir(settings.DMD_PATH)
    _mkdir(settings.DMD_OUTPUT)
    _mkdir(settings.DMD_UPLOAD)
    _mkdir(settings.DMD_CACHE)
    _mkdir(settings.DMD_TASK_PATH)
    _mkdir(os.path.dirname(settings.DMD_DEBIAN_CD_PATH))
    pass
           

def initdb():
    from dab.core.db import models
    from dab.core.db import database_proxy
    database = PostgresqlDatabase(
        'dabdb',  # Required by Peewee.
        user='postgres',  # Will be passed directly to psycopg2.
        password='qwe123',  # Ditto.
        host='192.168.122.10',  # Ditto.
    )

    database_proxy.initialize(database)
    database.connect()
    tablist = []
    for mod in models.Base.__subclasses__():
        if mod.table_exists():
            mod.drop_table(cascade=True)
        tablist.append(mod)
        print("create %s"%mod._meta.db_table)
    database.create_tables(tablist,safe=True)
    database.close()

def opt_parse():
    """process options from command line and config file"""
    parser = argparse.ArgumentParser("[option]",description="options from command line and config file")
    parser.add_argument("--dbfile", dest="dbfile",
                        help="db file use in test in sqlite3", metavar="FILE",
                        default="dab.db")
    parser.add_argument("--initdb",dest="initdb",action="store_true",
                                help="init db")

    parser.add_argument("--initdir",dest="initdir",action="store_true",
                                help="init dir")

    return parser.parse_args()

    

if __name__ == "__main__":
    opt = opt_parse()
    if opt.initdb:
        initdb()

    if opt.initdir:
        initdir()
