#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2017-04-06
@author: Heysion Yuan
@copyright: 2017, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''

from taskctrl import TaskList , TaskInfo
views = [
    (r'/task', TaskList),
    (r'/task/([0-9]+)', TaskInfo),
#    (r'/task/list', TaskListHandler),
#    (r'/task/([0-9]+)/info', TaskInfoHandler), # /task/<id>/info
#    (r'/task/([0-9]+)/result', TaskResultHandler), # /task/<id>/result
#    (r'/task/([0-9]+)/delete', TaskDelHandler), # /task/<id>/delete
]
