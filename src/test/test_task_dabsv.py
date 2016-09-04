#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-09-01
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
import requests
import json

def test_taskinfo_get_list_daemoncli():
    url = 'http://127.0.0.1:8080/task'
    values = {'username': 'trusty',
              'password': 'qwe123',
              'channelname': 'dptest',
              'hostname':'dptest'}

    response = requests.get(url,data=json.dumps(values))
    print response.content

if __name__ == "__main__":
    test_taskinfo_get_list_daemoncli()
