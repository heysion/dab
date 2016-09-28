#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-09-21
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
import time

from dabdaemon import DabDaemon
from dab.api.daemon import HttpDaemonApi
from multiprocessing import Process
from taskqueue import TaskQueue
import pdb

import pyuv
import os
import sys

class BuildDispatcher(DabDaemon):
    loopmain = pyuv.Loop.default_loop()
    timermain = pyuv.Timer(loopmain)
    tasklist = TaskQueue()
        
    def process_exit_cb(self,proc,exit_status,term_signal):
        print(exit_status)
        if hasattr(proc,"taskid"):
            print("proc len: %d"%(self.tasklist.length()))
            if exit_status is 0 :
                self.taskapi.daemon_update_taskinfo_success(self.username,int(proc.taskid))
                self.tasklist.rm_taskinfo(int(proc.taskid))
            else:
                self.taskapi.daemon_update_taskinfo_failed(self.username,int(proc.taskid))
        else:
            print("error task info")
        pass

    def stop_timer(self,handler):
        handler.stop()

    def again_timer(self,handler):
        handler.again()

    def run_sleep(self,tp):
        time.sleep(tp)

    def start_process(self,handler_timer):
        self.stop_timer(handler_timer)
        if self.tasklist.length() > 3:
            print("get task")
            time.sleep(5)
        else:
            ret_task = self.taskapi.daemon_fetch_task_first(channelname="dptest")
            if len(ret_task.list) == 1:
                taskid = ret_task.list[0]['taskid']
                dsc_file = ret_task.list[0]['srcdsc_file']
                build_name = ret_task.list[0]['buildname']
                
                if self.tasklist.set_taskinfo(taskid ,ret_task.list[0]) :
                    proc_env  = os.environ.copy()
                    log_file = open("abc.log","a+")

                    proc_logfile = pyuv.StdIO(fd=log_file.fileno(),flags=pyuv.UV_INHERIT_FD)
                    proc_args= ["deepin-buildpkg","-d", "%s/%s"%(self.httpdatasv,dsc_file), "-p"]
                    print(proc_args)
                    proc = pyuv.Process(self.loopmain)
                    pp = proc.spawn(self.loopmain,args=proc_args,
                                    exit_callback=self.process_exit_cb,
                                    env=proc_env,
                                    stdio=[proc_logfile,proc_logfile,proc_logfile])
                    pp.taskid = taskid
                    self.taskapi.daemon_update_taskinfo_build(self.username,taskid)
                else:
                    time.sleep(5)
                    print("same task")
            else:
                print("no task found")
        
        self.again_timer(handler_timer)

    def run(self,daemonconfig):
        self.httpdatasv = daemonconfig.options.topurl
        self.username = daemonconfig.options.username
        self.taskapi = HttpDaemonApi(daemonconfig)

        self.timermain.start(self.start_process,1,2)

        self.loopmain.run()

if __name__ == "__main__":
    app = BuildDispatcher()
    app.main()
