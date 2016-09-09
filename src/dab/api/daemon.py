#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-09-03
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
import requests

from dab.util.error import ConfigError
from dab.util import HttpRetPact
import json

class HttpDaemonApi:
    def __init__(self,daemonconfig):
        if not hasattr(daemonconfig,"options"):
            raise ConfigError("not found daemon config options")
        self.options = daemonconfig.options

    def daemon_login_dasv(self):
        """
        daemon login api
        return body struct = ['username','hostname','channelname']
        """
        pass

    def daemon_fetch_task_list(self,channelname,loginkey=None):
        """
        daemon fetch task list
        """
        api_url = self.options.server+"task"
        req_values = {'username':self.options.username,
                      'channelname':channelname,
                      'hostname':self.options.username}
        response = requests.get(url=api_url,data=json.dumps(req_values))
        if response :
            print(response.content)
            http_ret_pact = HttpRetPact(response.content)
            print(http_ret_pact.__dict__)
            return http_ret_pact
        else:
            return None

    def daemon_update_task_state(self,channelname,loginkey=None,state,taskid):
        """
        daemon fetch task list
        """
        api_url = self.options.server+"task"
        req_values = {'username':self.options.username,
                      'channelname':channelname,
                      'hostname':self.options.username,
                      'state':state,
                      'taskid':taskid}
        response = requests.post(url=api_url,data=json.dumps(req_values))
        if response :
            print(response.content)
            http_ret_pact = HttpRetPact(response.content)
            print(http_ret_pact.__dict__)
            return http_ret_pact
        else:
            return None
