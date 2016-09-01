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

import pdb

class TaskHandler(HandlerBase):
    def get(self):
        self.http_buffer_loading()
        if not (hasattr(self,"username") and hasattr(self,"password")) :
            self.write(self.ret_404_msg("404 error"))
        self.write("hello get%s"%(self.description))
        pass
    def post(self):
        self.write("hello post")
        pass
