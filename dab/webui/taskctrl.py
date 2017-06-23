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
        # task_items = [
        #     {"id":1,"name":"deepin-auto-build","createtime":"2017","state":"success","resultinfo":"info"},
        #     {"id":2,"name":"deepin-auto-build","createtime":"2017","state":"success","resultinfo":"info"}
        # ]
        # self.render("task.html", tasklist=task_items)
        # pass

    def get_task_top_all(self):
        dataset = Task.select(Task.id,Task.src_name,
                              Task.create_time,Task.state,
                              Task.owner_name)
        datalist = []
        if dataset :
            for data in dataset:
                datalist.append({"id":data.id,"name":data.name,
                                 "ceatetime":data.createtime,"state":data.state,
                                 "resultinfo":data.ower_name})
        return datalist

class TaskInfo(WebBase):
    pass

class TaskNew(WebBase):
    def get(self):
        self.render("tasknew.html")
        pass
    
    def post(self):
        req_data = { k: self.get_argument(k) for k in self.request.arguments }
        if not ("arches" in req_data.keys()):
            self.render("404.html")
        if not ("name" in req_data  and req_data["name"] is not None) :
            self.render("404.html")
        self.save_new_task(req_data)
        self.render("/taskindex")

    def save_new_task(self,data):
        new_task = Task.select(Task.name).where(Task.name==data["name"])
        if not new_task :
            new_task = Task.create(name=data["name"],
                                       suite=data["suite"],
                                       codename=data["codename"],
                                       architectures=data["arches"],
                                       workdir=data["workbase"],
                                       description=data["description"])
            new_task.save()
        else:
            return None

        return new_task
