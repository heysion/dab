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
#        pdb.set_trace()
        self.write(json.dumps(ret_data))
        pass
    def post(self):
        self.write("hello post")
        pass

class TaskUpdateHandler(HandlerBase):
    def get(self,taskid):
        self.write(self.ret_404_msg("404 error"))

    def post(self,taskid):
        pass
