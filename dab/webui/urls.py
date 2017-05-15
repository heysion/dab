#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2017-04-06
@author: Heysion Yuan
@copyright: 2017, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''

from taskctrl import TaskList , TaskInfo
from disctrl import DiscIndex, DiscNew, DiscInfo, DiscList
from taskctrl2 import TaskNew2
from pubctrl import PubIndex

views = [
    (r'/task', TaskIndex),
    (r'/task/([0-9]+)', TaskInfo),
    (r'/disc)', DiscIndex),
    (r'/pub)', PubIndex),
#    (r'/task/list', TaskListHandler),
#    (r'/task/([0-9]+)/info', TaskInfoHandler), # /task/<id>/info
#    (r'/task/([0-9]+)/result', TaskResultHandler), # /task/<id>/result
#    (r'/task/([0-9]+)/delete', TaskDelHandler), # /task/<id>/delete
]

# views = [
#     (r'/newtask', TaskNew),
#     (r'/newtask2', TaskNew2),
#     (r'/task/list', TaskList),
#     (r'/task/([0-9]+)', TaskInfo),
#     (r'/pub', PubIndex),
#     (r'/task/list', TaskListHandler),
#     (r'/task/([0-9]+)/info', TaskInfoHandler), # /task/<id>/info
#     (r'/task/([0-9]+)/result', TaskResultHandler), # /task/<id>/result
#     (r'/task/([0-9]+)/delete', TaskDelHandler), # /task/<id>/delete
# ]
