#!/usr/bin/python2
# -*- coding: utf-8 -*-
'''
@date: 2016-09-07
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
import yaml
import json
from dabsv import HandlerBase

class DaemonLoginHandler(HandlerBase):
    def get(self):
        self.wirte("login failed")
        pass
