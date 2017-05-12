#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-09-27
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
import time
import pyuv
import os
import sys


def process_exit_cb(proc,exit_status,term_signal):
    print(exit_status)
    if hasattr(proc,"taskid"):
        print("proc len: %d"%(tasklist.length()))
        #tasklist.rm_taskinfo(int(proc.taskid))
    pass

def stop_timer(handler):
    handler.stop()

def again_timer(handler):
    handler.again()

def run_sleep(tp):
    time.sleep(tp)


def start_process(handler_timer):
    stop_timer(handler_timer)
    if tasklist.length() > 3:
        time.sleep(5)
    else:
        taskid = tasklist.taskid + 1
        tasklist.taskid = taskid
        tasklist.set_taskinfo(taskid ,"a%d"%(taskid))

        proc_env  = os.environ.copy()
        log_file = open("abc.log","a+")

        proc_logfile = pyuv.StdIO(fd=log_file.fileno(),flags=pyuv.UV_INHERIT_FD)
        proc_args= ["bash","./tttt.sh","1"]
        proc = pyuv.Process(loopmain)
        pp = proc.spawn(loopmain,args=proc_args,
                        exit_callback=process_exit_cb,
                        env=proc_env,
                        stdio=[proc_logfile,proc_logfile,proc_logfile])
        pp.taskid = taskid
        

        again_timer(handler_timer)

loopmain = pyuv.Loop.default_loop()
timermain = pyuv.Timer(loopmain)
tasklist = TaskList()
timermain.start(start_process,1,2)
loopmain.run()

