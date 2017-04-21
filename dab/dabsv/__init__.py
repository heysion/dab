#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-09-01
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''

import tornado.web

import yaml

from dab.util import BufferLoading

import pdb 

class HandlerBase(tornado.web.RequestHandler):
    def ret_404_msg(self,msg):
        ret_data = {'retcode': 404, 'retmsg': msg}
        return yaml.dump(ret_data)
        pass
    def http_buffer_loading(self):
        self.bl = BufferLoading()
        if len(self.request.body):
            try:
                self.bl.no_buffer = False
                self.req_json = yaml.safe_load(self.request.body)
                for k,v in self.req_json.items():
                    if not getattr(self, k, None) :
                        setattr(self, k, v)
                        print(k,v)
            except ValueError as e:
                self.bl.no_error = False
            except KeyError as e:
                self.bl.no_error = False
            except AttributeError as e:
                self.bl.no_error = False
            finally:
                pass
