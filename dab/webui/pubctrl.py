#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2017-04-21
@author: Heysion Yuan
@copyright: 2017, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''

import pdb
import os
import shutil
import time
import json
import subprocess
import functools
import tornado.gen
from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor
from peewee import SqliteDatabase

from dab.webui import WebBase
from dab.core.db.models import MkisoInfo
from dab import settings

#FIXME
#print("#FIXME")
# db = SqliteDatabase("../peewee.db")
# MkisoInfo._meta.database = db

class PubIndex(WebBase):
    def get(self):
        req_data = { k: self.get_argument(k) for k in self.request.arguments }
        #tasklist = self.get_task_for_all()
        #print(tasklist)
        self.render("pubindex.html")
    
    def filter_task_for_name(self,taskname):
        task_data = MkisoInfo.select(MkisoInfo.id,
                                     MkisoInfo.isoname,
                                     MkisoInfo.create_time,
                                     MkisoInfo.status).where(MkisoInfo.isoname %"*{}*".format(taskname))
        print(task_data)
        taskinfo = []
        if task_data :
            for task in task_data:
                taskinfo.append({"id":task.id,"name":task.isoname,
                                 "createtime":task.create_time,"state":task.status})
        return taskinfo

    def post(self):
        req_data = { k: self.get_argument(k) for k in self.request.arguments }
        if "name" in req_data  and req_data["name"] :
            tasklist = self.filter_task_for_name(req_data["name"])
            self.render("publist.html",tasklist=tasklist)
