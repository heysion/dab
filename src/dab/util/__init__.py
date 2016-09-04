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
        if (self.no_error) and (not self.no_buffer):
            return True
        else:
            return False

class HttpRetPact:
    def __init__(self,retcode,retmsg=None,pact=None):
        self.ret_code = retcode
        self.ret_msg = retmsg
        self.pact = pact
        if self.pact :
            for k,v in self.pact.iteritems():
                if not getattr(self, k, None):
                    setattr(self, k, v)

    def update(self,pact):
        for k,v in pact.iteritems():
            setattr(self, k, v)
        self.pach = pact
    
    def hassuccess(self):
        return (self.ret_code is 0)
            
