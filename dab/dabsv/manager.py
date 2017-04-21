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

def initdb():
    from dab.db import models
    for mod in models.Base.__subclasses__():
        if mod.table_exists():
            mod.drop_table()
        mod.create_table()
        print("create %s"%mod._meta.db_table)

def opt_parse():
    """process options from command line and config file"""
    parser = argparse.ArgumentParser("[option]",description="options from command line and config file")
    parser.add_argument("--dbfile", dest="dbfile",
                        help="db file use in test in sqlite3", metavar="FILE",
                        default="dab.db")
    parser.add_argument("--initdb",dest="initdb",action="store_true",
                                help="init db")
    return parser.parse_args()

    

if __name__ == "__main__":
    opt = opt_parse()
    if opt.initdb:
        initdb()
