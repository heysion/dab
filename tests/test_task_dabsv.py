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
    url = 'http://127.0.0.1:8080/task/list'
    values = {'username': 'trusty',
              'password': 'qwe123',
              'channelname': 'dptest',
              'hostname':'dptest'}

    response = requests.get(url,data=json.dumps(values))
    print response.content

def test_taskinfo_get_top_daemoncli():
    url = 'http://127.0.0.1:8080/task/top/3'
    values = {'username': 'trusty',
              'password': 'qwe123',
              'channelname': 'dptest',
              'hostname':'dptest'}

    response = requests.get(url,data=json.dumps(values))
    print response.content


def test_task_update_list_daemoncli():
    url = 'http://127.0.0.1:8080/task/1/update'
    values = {'username': 'trusty',
              'password': 'qwe123',
              'channelname': 'dptest',
              'hostname':'dptest',
              'state':100,
              'taskid':11}

    response = requests.post(url,data=json.dumps(values))
    print response.content

if __name__ == "__main__":
    # test_taskinfo_get_list_daemoncli()
    test_taskinfo_get_top_daemoncli()

