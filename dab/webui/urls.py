#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2017-04-06
@author: Heysion Yuan
@copyright: 2017, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''

from taskctrl import TaskIndex, TaskInfo, TaskNew
from disctrl import DiscIndex, DiscNew, DiscInfo, DiscList
from targetctrl import TargetIndex, TargetNew
from pkgctrl import PkgIndex, PkgNew
from buildctrl import BuildIndex, BuildNew
from dab.webui import NotFound
#from taskctrl2 import TaskNew2
from pubctrl import PubIndex

views = [
    (r'/', NotFound),
    (r'/targetindex', TargetIndex),
    (r'/targetnew', TargetNew),
    (r'/pkgindex', PkgIndex),
    (r'/pkgnew', PkgNew),
    (r'/buildindex', BuildIndex),
    (r'/buildnew', BuildNew),
    (r'/taskindex', TaskIndex),
    (r'/discindex', DiscIndex),
    (r'/repoindex', NotFound),
    (r'/chlindex', NotFound),
    (r'/usrindex', NotFound),
    (r'/task', TaskIndex),
    (r'/tasknew', TaskNew),
    (r'/task/([0-9]+)', TaskInfo),
    (r'/discindex', DiscIndex),
    (r'/disc', DiscIndex),
]
