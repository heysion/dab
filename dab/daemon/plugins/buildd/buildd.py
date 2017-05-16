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
from multiprocessing import Process,Queue,Event,Manager
import pdb

import subprocess
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
    def task_worker(self,task_cntl_queue, task_data_queue, task_pool):
        taskinfo = task_data_queue.get()
        print(taskinfo)
        if taskinfo is not None:
            task_pool[taskinfo["taskid"]] = os.getpid()
            log_name = "{}/{}-{}.log".format(self.workdir,taskinfo["buildname"],taskinfo["taskid"])
            log_file = open(log_name,"a+")

            self.taskapi.daemon_update_taskinfo_build(self.username,taskinfo["taskid"])
            proc_cmd= ["deepin-buildpkg","-d", "%s/%s"%(self.httpdatasv,taskinfo["dscfile"]), "-p"]
            print(proc_cmd)

            ret = subprocess.call(proc_cmd,stdout=log_file,stderr=log_file)
            log_file.close()            

            if ret/256 == 0 :
                self.taskapi.daemon_update_taskinfo_success(self.username,taskinfo["taskid"])
            else:
                self.taskapi.daemon_update_taskinfo_failed(self.username,taskinfo["taskid"])
            pass

        else:
            return None
        #taskid = 1
        #task_q.put(taskinfo)
        task_cntl_queue.put({'event': 'exit', 'pid': os.getpid()})
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

    def proxy_task_process(self,task_cntl_queue, task_data_queue, exit_flag, task_pool):
        while True:
            if exit_flag.is_set():
                #if exit kill self
                task_cntl_queue.put({'event': 'exit', 'pid': os.getpid()})
                break

            print("proc counter %d"%(proc_counter.value))
            if proc_counter.value > 4:
                self.failed_sleep()
                print("runing proc %d"%proc_counter.value)
                continue
            else:
                taskinfo = self.fetch_task_api()
                if taskinfo is not None :
                    task_id = taskinfo['taskid']
                    if task_id not in task_pool.keys():
                        task_pool[task_id] = None
                        task_cntl_queue.put({'event': 'newtask'})
                        task_data_queue.put(taskinfo)
                else:
                    self.failed_sleep()
                    continue
                pass

    def run(self,daemonconfig):
        self.httpdatasv = daemonconfig.options.topurl
        self.username = daemonconfig.options.username
        self.taskapi = HttpDaemonApi(daemonconfig)
        self.workdir = daemonconfig.options.workdir

        manager = Manager()

        task_pool = manager.dict()
        proc_pool = {}
        task_cntl_queue = Queue()
        task_data_queue = Queue()
        exit_flag = mp.Event()

        signal(SIGINT, lambda x, y: exit_flag.set())
        # siginterrupt(SIGINT, False)

        #print 'main {} started'.format(os.getpid())
        proc = mp.Process(target=self.proxy_task_process, 
                          args=(task_cntl_queue, task_data_queue, exit_flag, task_pool))
        proc.start()
        proc_pid = proc.pid
        proc_pool[proc_pid] = proc
        update_counter()
        #print 'proxy {} started'.format(proc.pid)

        while True:
            item = task_cntl_queue.get()
            if item['event'] == 'newtask':
                proc = mp.Process(target=self.task_worker, args=(task_cntl_queue, task_data_queue, task_pool))
                proc.start()
                proc_pool[proc.pid] = proc
                update_counter()
                # print 'worker {} started'.format(proc.pid)
            elif item['event'] == 'exit':
                proc = proc_pool.pop(item['pid'])
                task_id = task_pool.keys()[task_pool.values().index(item['pid'])]
                if task_id is not None:
                    task_pool.pop(task_id)
                reduce_counter()
                proc.join()
                # print 'child {} stopped'.format(item['pid'])
            else:
                pass
                # print 'It\'s impossible !'
                
            if not proc_pool: 
                break
        #print 'main {} stopped'.format(os.getpid())

if __name__ == "__main__":
    app = BuildDispatcher()
    app.main()
