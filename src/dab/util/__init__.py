#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-08-25
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
class BufferLoading:
    no_error = False
    no_buffer = True

    def has_noerror(self):
        if (self.no_error ) and (not self.no_buffer ) :
            return True
        else:
            return False
