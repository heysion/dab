#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-09-05
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
from multiprocessing import Process ,Queue ,Pool
import multiprocessing

import os
import time
import signal

from dabdaemon.plugins import Plugin

class Main(Plugin):

    def __init__(self):
        self.manager = multiprocessing.Manager()
        self.lock = self.manager.Lock()
        self.task_queue = self.manager.Queue()
        self.finish_queue = self.manager.Queue()
        self.task_list = []
        self.work_pool = Pool()
        self.work_pool_manager = multiprocessing.Manager()
        pass
    
    def fetch_task(self):
        def sigtermhandler(signum, frame):
            sys.exit()

        signal.signal(signal.SIGTERM, sigtermhandler)
        signal.signal(signal.SIGINT, sigtermhandler)

        while True:
            print("fetch:q1 %d q2 %d"%(self.task_queue.qsize(),
                                       self.finish_queue.qsize()))
            if self.task_queue.qsize() < 4:
                for value in range(4):
                    print("pm: %d put:%d"%(os.getpid(),value))
                    self.task_queue.put(value)

            while not self.finish_queue.empty():
                value = finish_queue.get()
                print("pm: %d get q2 %d"%(os.getpid(),value))
                self.task_list.remove(value)
            time.sleep(3)

    def worker(self):
        print("woker: %d "%(os.getpid()))
        def sigtermhandler(signum, frame):
            sys.exit()

        signal.signal(signal.SIGTERM, sigtermhandler)
        signal.signal(signal.SIGINT, sigtermhandler)

        while True:
            if not self.task_queue.empty():
                value = self.task_queue.get()
                print("dopid: %d get q1 %d"%(os.getpid(),value))
                self.task_list.append(value)
                time.sleep(5)
                self.finish_queue.put(value)
                print("dopid: %d put q2 %d"%(os.getpid(),value))
            else:
                time.sleep(5)
    
    def work_main(self):
        #print("workmain: %d "%(os.getpid()))
        for work in range(2):
            self.work_pool.apply_async(self.worker)
        self.work_pool.close()
        self.work_pool.join()

    def init(self):
        self.fetch_process = Process(target=self.fetch_task)
        self.work_process = Process(target=self.work_main)
        pass
    
    def run(self):
        self.init()
        self.fetch_process.start()
        self.work_process.start()
        self.fetch_process.join()
        self.work_process.join()
    pass

if __name__ == "__main__":
    app = Main()
    app.run()
