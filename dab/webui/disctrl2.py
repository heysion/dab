#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2017-04-06
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

from dmd.dmdweb import WebBase
from dab.db.models import MkisoInfo
from dmd import settings

#FIXME
print("#FIXME")
db = SqliteDatabase("../peewee.db")
MkisoInfo._meta.database = db

class TaskNew2(WebBase):
    _thread_pool = ThreadPoolExecutor(5)
    def prepare(self):
        pass
    def on_finish(self):
        super(TaskNew2, self).on_finish()

    def get(self):
        self.render("task2.html")
        pass
    
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        req_data = { k: self.get_argument(k) for k in self.request.arguments }
        if not ("tag" in req_data.keys()):
            req_data["tag"] = "15.1"
        if not ("isoname" in req_data  and req_data["isoname"] is not None) :
            req_data["isoname"] = "deepin-server"
        tornado.ioloop.IOLoop.instance().add_callback(functools.partial(self.call_mkiso,req_data))
        # print(req_data)
        # self.write(req_data)
        # self.write(self.request.body)
        self.render("task2.html")

    @tornado.concurrent.run_on_executor(executor='_thread_pool')
    def call_mkiso(self,data):
        task_instance = self.save_task(data)
        if task_instance :
            self.init_task_work(task_instance)
        cmd = "{} -c {}/config.json".format(settings.DMD_TOOLS_BIN,self.task_work_base)
        print(cmd)
        #subprocess.call(cmd)
        time.sleep(5)

    def init_task_work(self,task):
        self.task_work_base = "{}/{}".format(settings.DMD_TASK_PATH,task.id)
        if not os.path.exists(self.task_work_base):
            os.mkdir(self.task_work_base)
        if task.includelist:
            with open('{}/include.list'.format(self.task_work_base), 'a') as the_file:
                the_file.write(task.includelist)
        if task.excludelist:
            with open('{}/exclude.list'.format(self.task_work_base), 'a') as the_file:
                the_file.write(task.excludelist)
        with open('{}/config.json'.format(self.task_work_base), 'a') as the_file:
            self.config_data = {"name":task.isoname,
                                "tag":"15.1",
                                "arch":"mips64el",
                                "task":task.id,
                                "workbase":self.task_work_base,
                                "preseed":"preseed.cfg",
                                "include":"include.list",
                                "exclude":"exclude.list",
                                "output":settings.DMD_OUTPUT,
                                "cache":settings.DMD_CACHE,
                                "repo":"{}/{}".format(settings.DMD_REPO_PRE,"mips64el"),
                                "debian_cd":settings.DMD_DEBIAN_CD_PATH}
            the_file.write(json.dumps(self.config_data))
        self.preseed_orig = "{}/{}".format(settings.DMD_UPLOAD,task.preseed_config)
        if os.path.exists(self.preseed_orig):
            shutil.move(self.preseed_orig,"{}/preseed.cfg".format(self.task_work_base))

    def save_task(self,data):
        task = MkisoInfo.select(MkisoInfo.isoname).where(MkisoInfo.isoname==data["isoname"])
        if not task :
            task = MkisoInfo.create(isoname=data["isoname"],
                                        preseed_config=data["preseedfile"],
                                        includelist=data["includelist"],
                                        excludelist=data["excludelist"],
                                        status=100)
            task.save()
        else:
            return None
        return task
