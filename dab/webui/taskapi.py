#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2017-06-27
@author: Heysion Yuan
@copyright: 2017, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
from dab.webui import APIBase
from dab.core.db.models import Task

class TaskAPI(APIBase):
    def get(self):
        task_id = self.get_argument('taskid', None)
        result_data = []
        if task_id:
            result_data = self.get_task_id(task_id)
        else:
            result_data = self.get_task_top()
        self.write(self.ret_ok_data(data=result_data))
    
    def get_task_id(self,taskid):
        dataset = Task.select(Task.id,Task.pkg_name,
                              Task.target_name,Task.owner_name,
                              Task.create_time,Task.state).where(Task.id == taskid)
        datalist = []
        if dataset :
            for data in dataset:
                datalist.append({"id":data.id,"pkgname":data.pkg_name.name,
                                 "targetname":data.target_name.name,"owername":data.owner_name.name,
                                 "createtime":data.create_time,"state":data.state})
        return datalist

    def get_task_top(self):
        dataset = Task.select(Task.id,Task.pkg_name,
                              Task.target_name,Task.owner_name,
                              Task.create_time,Task.state).limit(10)
        datalist = []
        if dataset :
            for data in dataset:
                datalist.append({"id":data.id,"pkgname":data.pkg_name.name,
                                 "targetname":data.target_name.name,"owername":data.owner_name.name,
                                 "createtime":data.create_time,"state":data.state})
        return datalist
    
    def post(self):
        self.http_buffer_loading()
        ret_data = {}

        if not getattr(self,"arch",None ):
            ret_data = self.ret_404_msg("not found arch")
            self.write(ret_data)
            return

        if not getattr(self,"pkgname", None) :
            ret_data = self.ret_404_msg("not found pkgname")
            self.write(ret_data)
            return
        
        if not getattr(self,"target", None) :
            ret_data = self.ret_404_msg("not found target")
            self.write(ret_data)
            return

        db_ret_data = self.save_new_task()
        print(db_ret_data)

    def save_new_task(self):
        #new_task = Task.select(Task.pkg_name).where(Task.pkg_name==self.pkgname)
        #print(new_task)
        new_task = None
        if not new_task :
            new_task = Task.create(pkg_name=self.pkgname,
                                   target_name=self.target,
                                   arch=self.arch,
                                   ower_id=1,
                                   ower_name="admin")
            new_task.save()
        else:
            return None

        return new_task

    def patch(self):
        self.http_buffer_loading()
        ret_data = {}
        if not getattr(self,"taskid",None ):
            ret_data = self.ret_404_msg("not found taskid")
            self.write(ret_data)
            return
        pass

    def update_task(self):
        old_task = Task.select(Task.pkg_name).where(Task.id==self.taskid)
        print(old_task)
        if old_task :
            old_task = Task.update(start_time=self.starttime,
                                   completion_time=self.completiontime,
                                   chs_file=self.chsfile,
                                   state=self.state,
                                   sha1sum=self.sha1sum,
                                   md5sum=self.md5sum,
                                   filesize=self.filesize).where(task_id == self.taskid)
            old_task.execute()
        else:
            return None

        return old_task
