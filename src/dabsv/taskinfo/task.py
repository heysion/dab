#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-08-30
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''

import yaml
import json
from dabsv import HandlerBase
from dabdb.dbconn import dbinit
from dabdb import taskinfo

import pdb


class TaskHandler(HandlerBase):
    def get(self):
        self.http_buffer_loading()
        if not (hasattr(self,"channelname") and hasattr(self,"hostname")) :
            self.write(self.ret_404_msg("404 error"))
            return
        self.db,self.session = dbinit("postgres")
        k = ['taskid','state','createtime',
             'buildname','srcname','srcversion',
             'srcdsc_file']
        task_data = taskinfo.get_list_daemoncli(self.session,self.channelname,self.hostname)
        ret_task_data = []
        for v in task_data:
            ret_task_data.append(dict(zip(k,v)))
        ret_data = {'retcode':0,'retmsg':None,'list':ret_task_data}
        self.write(json.dumps(ret_data))
        pass
    def post(self):
        self.write("hello post")
        pass


class TaskUpdateHandler(HandlerBase):
    def get(self,taskid):
        self.write(self.ret_404_msg("404 error"))

    def post(self,taskid):
        """
        request={channelname,hostname,taskid,state,starttime,completiontime}
        """
        self.http_buffer_loading()
        if not (hasattr(self,"channelname") 
                and hasattr(self,"hostname") 
                and hasattr(self,"taskid") 
                and hasattr(self,"state")):
            self.write(self.ret_404_msg("404 error"))
            return

        self.db,self.session = dbinit("postgres")

        req_key = ['taskid','state','createtime',
             'completiontime','starttime']

        for k in req_key:
            if not getattr(self, k, None):
                setattr(self, k, None)
        update_rc = taskinfo.update_daemoncli(session=self.session,
                                             channelname=self.channelname,
                                             hostname=self.hostname,
                                             state=self.state,
                                             taskid=self.taskid)
        ret_data = {'retcode':0,'retmsg':None,'list':None}
        if not update_rc:
            ret_data['retcode']=1001
            ret_data['retmsg']='db error or not found task'
        self.write(json.dumps(ret_data))

        # task_data = taskinfo.get_list_daemoncli(self.session,self.channelname,self.hostname)
        # ret_task_data = []
        # for v in task_data:
        #     ret_task_data.append(dict(zip(k,v)))
        # ret_data = {'retcode':0,'retmsg':None,'list':ret_task_data}
        # self.write(json.dumps(ret_data))
        pass
