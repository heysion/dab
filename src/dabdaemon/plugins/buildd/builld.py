#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-09-21
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
import time
import multiprocessing as mp

from signal import signal, SIGINT, SIG_IGN, siginterrupt
from dabdaemon import DabDaemon
from dab.api.daemon import HttpDaemonApi
from multiprocessing import Process
import pdb

import os
import sys

from utils import Counter

proc_counter = Counter()

def update_counter():
    global proc_counter
    proc_counter.increment()

def reduce_counter():
    global proc_counter
    proc_counter.reduce()


class BuildDispatcher(DabDaemon):
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

    def task_worker(self,cntl_q, data_q, task_q):
        taskinfo = data_q.get()
        if taskinfo is not None:
            proc_cmd= ["deepin-buildpkg","-d", "%s/%s"%(self.httpdatasv,taskinfo["dscfile"]), "-p"]
            ret = subprocess.call(proc_cmd)
            pass
        else:
            return None
        taskid = 1
        task_q.put({"event":'updatetask','taskid':taskid})
        cntl_q.put({'event': 'exit', 'pid': os.getpid()})
        pass

    def fetch_task_api(self):
        ret_task = self.taskapi.daemon_fetch_task_first(channelname="dptest")
        print(ret_task)
        if ret_task and len(ret_task.list) == 1:
            taskid = ret_task.list[0]['taskid']
            dsc_file = ret_task.list[0]['srcdsc_file']
            build_name = ret_task.list[0]['buildname']
            return {"taskid":taskid,"dscfile":dsc_file,"buildname":build_name}
        else:
            return None
        pass

    def failed_sleep(self):
        time.sleep(5)

    def get_task_process(self,cntl_q, data_q, task_q, exit_flag):
        while True:
            print("proc counter %d"%(proc_counter.value))
            if proc_counter.value > 4:
                self.failed_sleep()
                print("runing proc %d"%proc_counter.value)
                continue
            taskinfo = self.fetch_task_api()
            if taskinfo is not None:
                cntl_q.put({'event': 'newtask'})
                data_q.put(taskinfo)
            else:
                self.failed_sleep()
                continue
                pass
            if exit_flag.is_set():
                cntl_q.put({'event': 'exit', 'pid': os.getpid()})
                break
            else:
                pass
            taskinfo = task_q.get()
            if taskinfo is not None:
                self.taskapi.daemon_update_taskinfo_build(self.username,taskid)
                pass
            else:
                continue
                pass

    def run(self,daemonconfig):
        self.httpdatasv = daemonconfig.options.topurl
        self.username = daemonconfig.options.username
        self.taskapi = HttpDaemonApi(daemonconfig)

        proc_pool = {} 
        cntl_q = mp.Queue() 
        data_q = mp.Queue() 
        task_q = mp.Queue() 
        exit_flag = mp.Event() 

        signal(SIGINT, lambda x, y: exit_flag.set())
        siginterrupt(SIGINT, False)

        print 'main {} started'.format(os.getpid())
        proc = mp.Process(target=self.get_task_process, args=(cntl_q, data_q, task_q, exit_flag))
        proc.start()
        proc_pid = proc.pid
        proc_pool[proc_pid] = proc
        update_counter()
        print 'proxy {} started'.format(proc.pid)

        while True:
            item = cntl_q.get()
            if item['event'] == 'newtask':
                proc = mp.Process(target=self.task_worker, args=(cntl_q, data_q, task_q))
                proc.start()
                proc_pool[proc.pid] = proc
                update_counter()
                print("proc pool size:%d"%(len(proc_pool)))

                print 'worker {} started'.format(proc.pid)
            elif item['event'] == 'exit':
                proc = proc_pool.pop(item['pid'])
                reduce_counter()
                proc.join()
                print 'child {} stopped'.format(item['pid'])
            else:
                print 'It\'s impossible !'

            if not proc_pool: 
                break

            print 'main {} stopped'.format(os.getpid())


if __name__ == "__main__":
    app = BuildDispatcher()
    app.main()
