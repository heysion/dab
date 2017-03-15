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

import pdb

def fetch_process(q,lock):
    q1 ,q2 = q
    def sigtermhandler(signum, frame):
        sys.exit()

    signal.signal(signal.SIGTERM, sigtermhandler)
    signal.signal(signal.SIGINT, sigtermhandler)

    while True:
        print("pm:q1 %d q2 %d"%(q1.qsize(),q2.qsize()))
        if q1.qsize() < 4:
            lock.acquire()
            for value in range(4):
                print("pm: %d put:%d"%(os.getpid(),value))
                q1.put(value)
            lock.release()

        while not q2.empty():
            value = q2.get()
            print("pm: %d get q2 %d"%(os.getpid(),value))
        time.sleep(3)
        
def work_process(q,lock):
    print("dowork: %d "%(os.getpid()))
    q1 ,q2 = q
    def sigtermhandler(signum, frame):
        sys.exit()

    signal.signal(signal.SIGTERM, sigtermhandler)
    signal.signal(signal.SIGINT, sigtermhandler)

    while True:
        if not q1.empty():
            value = q1.get()
            print("dopid: %d get q1 %d"%(os.getpid(),value))
            time.sleep(5)
            #lock.acquire()
            q2.put(value)
            print("dopid: %d put q2 %d"%(os.getpid(),value))
            #locl.release()
        else:
            time.sleep(5)

def dowork_process(q):
    print("pw: %d "%(os.getpid()))
    pw_manager = multiprocessing.Manager()
    dowork_pool = Pool()
    lock = pw_manager.Lock()
    for work in range(2):
        dowork_pool.apply_async(work_process,args=(q,lock))
    dowork_pool.close()
    dowork_pool.join()
    
if __name__ == "__main__":
    manager = multiprocessing.Manager()
    lock = manager.Lock()
    q = (manager.Queue(),manager.Queue())
    pm = Process(target=fetch_process,args=(q,lock))
    pw = Process(target=dowork_process,args=(q,))
    pm.start()
    pw.start()
    pm.join()
    pw.join()
