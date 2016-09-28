#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-08-25
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
import yaml

import pdb

class BufferLoading:
    no_error = False
    no_buffer = True

    def has_noerror(self):
        if (self.no_error) and (not self.no_buffer):
            return True
        else:
            return False

class HttpRetPact:
    def __init__(self,httpbuffer):
        print(httpbuffer)
        self.http_buffer = yaml.safe_load(httpbuffer)
        print(self.http_buffer)
        for k,v in self.http_buffer.iteritems():
            if not getattr(self, k, None):
                setattr(self, k, v)

    # def update(self,pact):
    #     for k,v in pact.iteritems():
    #         setattr(self, k, v)
    #     self.pach = pact
    
    def hassuccess(self):
        return (self.ret_code is 0)
            
