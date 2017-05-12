#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-09-28
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''

class TaskQueue(object):
    def __new__(cls,*args,**kw):
        if not hasattr(cls,'_instace'):
            orig = super(TaskQueue,cls)
            cls._instace = orig.__new__(cls,*args,**kw)
        return cls._instace

    def __init__(self):
        if not hasattr(self,'_task_queue'):
            self._task_queue = {}
        self.taskid = 0
        pass
    def get_taskinfo(self,key):
        if self._task_queue.has_key(key):
            return self._task_queue[key]
        return None
    def set_taskinfo(self,key,info):
        if not self._task_queue.has_key(key):
            self._task_queue[key]=info
            return True
        return False
    def rm_taskinfo(self,key):
        if self._task_queue.has_key(key):
            del self._task_queue[key]
            return True
        return False
    def length(self):
        return len(self._task_queue)
    pass
