#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2017-04-06
@author: Heysion Yuan
@copyright: 2017, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
import tornado.web
import yaml

import pdb

class WebBase(tornado.web.RequestHandler):
    def ret_404_msg(self,msg):
        return {'retcode': 404, 'retmsg': msg}
        
    def ret_ok_data(self,data):
        return {'retcode': 000, 'retmsg': "OK", 'retdata':data}

    pass

class APIBase(tornado.web.RequestHandler):
    def ret_404_msg(self,msg):
        ret_data = {'retcode': 404, 'retmsg': msg}
        return yaml.dump(ret_data)

    def ret_ok_data(self,data):
        ret_data = {'retcode': 000, 'retmsg': "OK", 'retdata':data}
        return yaml.dump(ret_data)

    def http_buffer_loading(self):
        self.bl = {"no_buffer":None,"no_error":None}
        print(self.request.body)
        #pdb.set_trace()
        if len(self.request.body):
            try:
                self.bl["no_buffer"] = False
                self.req_json = yaml.safe_load(self.request.body)
                for k,v in self.req_json.items():
                    if not getattr(self, k, None) :
                        setattr(self, k, v)
                        print(k,v)
            except ValueError as e:
                self.bl["no_error"] = False
            except KeyError as e:
                self.bl["no_error"] = False
            except AttributeError as e:
                self.bl["no_error"] = False
            finally:
                pass

    pass

class NotFound(WebBase):
    def get(self):
        self.render("404.html")
        #self.set_status(404)

    def post(self):
        self.render("404.html")

    # def ret_404_msg(self,msg):
    #     ret_data = {'retcode': 404, 'retmsg': msg}
    #     return yaml.dump(ret_data)
    #     pass
    # def http_buffer_loading(self):
    #     self.bl = BufferLoading()
    #     if len(self.request.body):
    #         try:
    #             self.bl.no_buffer = False
    #             self.req_json = yaml.safe_load(self.request.body)
    #             for k,v in self.req_json.items():
    #                 if not getattr(self, k, None) :
    #                     setattr(self, k, v)
    #                     print(k,v)
    #         except ValueError, e:
    #             self.bl.no_error = False
    #         except KeyError, e:
    #             self.bl.no_error = False
    #         except AttributeError, e:
    #             self.bl.no_error = False
    #         finally:
    #             pass
