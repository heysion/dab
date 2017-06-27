#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2017-04-06
@author: Heysion Yuan
@copyright: 2017, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
from dab.webui import WebBase
from dab.core.db.models import Task

class TaskIndex(WebBase):
    def get(self):
        dataset = self.get_task_top_all()

        self.render("taskindex.html",tasklist=dataset)

    def get_task_top_all(self):
        dataset = Task.select(Task.id,Task.pkg_name,
                              Task.target_name,Task.owner_name,
                              Task.create_time,Task.state)
        datalist = []
        if dataset :
            for data in dataset:
                datalist.append({"id":data.id,"pkgname":data.pkg_name.name,
                                 "targetname":data.target_name.name,"owername":data.owner_name.name,
                                 "createtime":data.create_time,"state":data.state})
        return datalist

class TaskInfo(WebBase):
    pass

class TaskNew(WebBase):
    def get(self):
        self.render("tasknew.html")
        pass
    
    def post(self):
        req_data = { k: self.get_argument(k) for k in self.request.arguments }
        if not ("arch" in req_data.keys()):
            self.render("404.html")
        if not ("pkgname" in req_data  and req_data["pkgname"] is not None) :
            self.render("404.html")
        self.save_new_task(req_data)
        self.redirect("/taskindex")

    def save_new_task(self,data):
        new_task = Task.select(Task.pkg_name).where(Task.pkg_name==data["pkgname"])
        print(new_task)
        if not new_task :
            new_task = Task.create(pkg_name=data["pkgname"],
                                   target_name=data["target"],
                                   arch=data["arch"],
                                   ower_id=1,
                                   ower_name="admin")
            new_task.save()
        else:
            return None

        return new_task

