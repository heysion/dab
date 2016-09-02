#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-08-30
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''


from dabdb.da.tasks import Task as daTask
from dabsv import HandlerBase
from dabdb.da.dbconn import dbinit

import pdb


class TaskHandler(HandlerBase):
    def get(self):
        self.http_buffer_loading()
        if not (hasattr(self,"channelid") and hasattr(self,"hostid")) :
            self.write(self.ret_404_msg("404 error"))
        self.db,self.session = dbinit("postgres")
        task_dataset = daTask.get_task_info_daemon(self.channelid,self.hostid)
        print(task_dataset)
        self.write("hello get%s"%(self.description))
        pass
    def post(self):
        self.write("hello post")
        pass
