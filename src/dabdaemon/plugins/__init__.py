#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-09-04
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
class PluginManager:
    pass

class Plugin:
    def create(self):
        pass
    def init(self):
        pass
    def do_run(self):
        pass
    def do_finish(self):
        pass
    def clean(self):
        pass
