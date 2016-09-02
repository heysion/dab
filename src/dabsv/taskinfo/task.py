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
        task_data = taskinfo.task_get(self.session,self.channelname,self.hostname)
        ret_data = []
        for v in task_data:
            ret_data.append(dict(zip(k,v)))

#        pdb.set_trace()
        self.write(json.dumps(ret_data))
        pass
    def post(self):
        self.write("hello post")
        pass
