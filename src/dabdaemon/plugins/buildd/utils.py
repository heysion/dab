#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-11-25
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
import multiprocessing as mp
'''
mutliprocces counter
'''
class Counter(object):
    def __init__(self):
        self.val = mp.Value('i', 0)

    def increment(self, n=1):
        with self.val.get_lock():
            self.val.value += n

    def reduce(self, n=1):
        with self.val.get_lock():
            self.val.value -= n

    @property
    def value(self):
        return self.val.value
