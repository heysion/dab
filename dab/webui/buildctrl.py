#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2017-05-24
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

from dab.webui import WebBase
from dab.core.db.models import Target, Package
from dab import settings

class BuildIndex(WebBase):
    def get(self):

        dataset = self.get_pkg_top_all()

        self.render("buildindex.html",datalist=dataset)

    def get_pkg_top_all(self):
        dataset = Package.select(Package.id , Package.name,
                                  Package.target_name, Package.enabled)
        datalist = []
        if dataset :
            for data in dataset:
                datalist.append({"name":data.name, "id":data.id,
                                 "target_name":data.target_name.name, "enabled":data.enabled})

        return datalist

class BuildNew(WebBase):
    _thread_pool = ThreadPoolExecutor(5)
    def prepare(self):
        pass
    def on_finish(self):
        super(BuildNew, self).on_finish()

    def get(self):
        self.render("buildnew.html")
        pass
    
    # @tornado.web.asynchronous
    # @tornado.gen.coroutine
    def post(self):
        req_data = { k: self.get_argument(k) for k in self.request.arguments }
        if not ("name" in req_data.keys()):
            self.render("404.html")
        if not ("target_name" in req_data  and req_data["target_name"] is not None) :
            self.render("404.html")
        #tornado.ioloop.IOLoop.instance().add_callback(functools.partial(self.save_new_target,req_data))
        self.save_new_instance(req_data)
        # print(req_data)
        # self.write(req_data)
        # self.write(self.request.body)
        self.render("buildindex.html",datalist=[])

    #@tornado.concurrent.run_on_executor(executor='_thread_pool')
    def save_new_instance(self,data):
        new_instance = Package.select(Package.name).where(Package.name==data["name"] and Package.target_name==data["target_name"])
        if not new_instance :
            new_instance = Package.create(name=data["name"],
                                       target_name=data["target_name"],
                                       enabled=data["enabled"])
            new_instance.save()
        else:
            return None

        return new_instance
