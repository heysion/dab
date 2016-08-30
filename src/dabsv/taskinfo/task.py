#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-08-30
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
import tornado.web
import pdb


class TaskHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello get")
        pass
    def post(self):
        self.write("hello post")
        pass
