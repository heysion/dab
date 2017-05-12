#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-08-25
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
class ConfigError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return repr(self.msg)

class DabdbError(ConfigError):
    pass

