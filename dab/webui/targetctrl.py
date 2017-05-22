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
#from peewee import SqliteDatabase

from dab.webui import WebBase
from dab.core.db.models import Target
from dab import settings


class TargetIndex(WebBase):
    def get(self):
        self.render("targetindex.html",targetlist=[])

class TargetNew(WebBase):
    _thread_pool = ThreadPoolExecutor(5)
    def prepare(self):
        pass
    def on_finish(self):
        super(TargetNew, self).on_finish()

    def get(self):
        self.render("targetnew.html")
        pass
    
    # @tornado.web.asynchronous
    # @tornado.gen.coroutine
    def post(self):
        req_data = { k: self.get_argument(k) for k in self.request.arguments }
        if not ("arches" in req_data.keys()):
            self.render("404.html")
        if not ("name" in req_data  and req_data["name"] is not None) :
            self.render("404.html")
        #tornado.ioloop.IOLoop.instance().add_callback(functools.partial(self.save_new_target,req_data))
        self.save_new_target(req_data)
        # print(req_data)
        # self.write(req_data)
        # self.write(self.request.body)
        self.render("targetindex.html",targetlist=[])

    #@tornado.concurrent.run_on_executor(executor='_thread_pool')
    def save_new_target(self,data):
        new_target = Target.select(Target.name).where(Target.name==data["name"])
        if not new_target :
            new_target = Target.create(name=data["name"],
                                       suite=data["suite"],
                                       codename=data["codename"],
                                       architectures=data["arches"],
                                       workdir=data["workbase"],
                                       description=data["description"])
            new_target.save()
        else:
            return None

        return new_target
    # def new_target(self,data):
    #     task_instance = self.save_task(data)
    #     if task_instance :
    #         self.init_task_work(task_instance)
    #     # cmd = "{} -c {}/config.json".format(settings.DMD_TOOLS_BIN,self.task_work_base)
    #     # print(cmd)
    #     # #subprocess.call(cmd)
    #     # time.sleep(5)

    # def init_task_work(self,task):
    #     self.task_work_base = "{}/{}".format(settings.DMD_TASK_PATH,task.id)
    #     if not os.path.exists(self.task_work_base):
    #         os.mkdir(self.task_work_base)
    #     if task.includelist:
    #         with open('{}/include.list'.format(self.task_work_base), 'a') as the_file:
    #             the_file.write(task.includelist)
    #     if task.excludelist:
    #         with open('{}/exclude.list'.format(self.task_work_base), 'a') as the_file:
    #             the_file.write(task.excludelist)
    #     with open('{}/config.json'.format(self.task_work_base), 'a') as the_file:
    #         self.config_data = {"name":task.isoname,
    #                             "tag":"15.1",
    #                             "arch":"mips64el",
    #                             "task":task.id,
    #                             "workbase":self.task_work_base,
    #                             "preseed":"preseed.cfg",
    #                             "include":"include.list",
    #                             "exclude":"exclude.list",
    #                             "output":settings.DMD_OUTPUT,
    #                             "cache":settings.DMD_CACHE,
    #                             "repo":"{}/{}".format(settings.DMD_REPO_PRE,"mips64el"),
    #                             "debian_cd":settings.DMD_DEBIAN_CD_PATH}
    #         the_file.write(json.dumps(self.config_data))
    #     self.preseed_orig = "{}/{}".format(settings.DMD_UPLOAD,task.preseed_config)
    #     if os.path.exists(self.preseed_orig):
    #         shutil.move(self.preseed_orig,"{}/preseed.cfg".format(self.task_work_base))



# class DiscInfo(WebBase):
#     pass

# class DiscList(WebBase):
#     def get(self):
#         req_data = { k: self.get_argument(k) for k in self.request.arguments }
#         tasklist = self.get_task_for_all()
#         #print(tasklist)
#         self.render("tasklist.html",tasklist=tasklist)

#     def get_task_for_all(self):
#         task_data = MkisoInfo.select(MkisoInfo.id,MkisoInfo.isoname,
#                                      MkisoInfo.create_time,MkisoInfo.status)
#         taskinfo = []
#         if task_data :
#             for task in task_data:
#                 taskinfo.append({"id":task.id,"name":task.isoname,
#                                  "createtime":task.create_time,"state":task.status})
#         return taskinfo

#     def get_task_for_name(self,name):
#         task = MkisoInfo.select(MkisoInfo.isoname).where(MkisoInfo.isoname==name)
#         if not task :
#             pass
#         return task

#     pass
