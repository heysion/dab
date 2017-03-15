# -*- coding: utf-8 -*-
#!/usr/bin/env python

import tornado.web
import pdb
from task import TaskListHandler,TaskUpdateHandler,TaskTopHandler


handlers = [
    (r'/task/list', TaskListHandler),
    (r'/task/top/([0-9]+)', TaskTopHandler),
    (r'/task/([0-9]+)/update', TaskUpdateHandler),
#    (r'/task/list', TaskListHandler),
#    (r'/task/([0-9]+)/info', TaskInfoHandler), # /task/<id>/info
#    (r'/task/([0-9]+)/result', TaskResultHandler), # /task/<id>/result
#    (r'/task/([0-9]+)/delete', TaskDelHandler), # /task/<id>/delete
]
