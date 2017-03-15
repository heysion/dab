import fcntl
import atexit
import os
import sys
import time
import signal

import multiprocessing as mp

import time
import multiprocessing as mp
import random

#from signal import signal, SIGINT, SIGHUP, SIG_IGN, siginterrupt
from multiprocessing import Process,Queue,Event,Manager

import subprocess
import os
import sys

class Daemon(object):
    def __init__(self):
        self.foreground = True
        self.pidfile = "/tmp/pidfile-001"
        pass

    def get_pid(self):
        try:
            pf = file(self.pidfile, 'r')
            pid = int(pf.read().strip())
            pf.close()
        except IOError:
            pid = None
        except SystemExit:
            pid = None
        return pid

    def start(self):
        """
        Start the daemon
        """
        if os.path.isfile(self.pidfile):
            with open(self.pidfile, "r") as old_pidfile:
                old_pid = old_pidfile.read()
        try:
            lockfile = open(self.pidfile, "w")
        except IOError:
            print("Unable to create the pidfile.")
            sys.exit(1)
        try:
            # locked.
            fcntl.flock(lockfile, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except IOError:
            print("Unable to lock on the pidfile.")
            # We need to overwrite the pidfile if we got here.
            with open(self.pidfile, "w") as pidfile:
                pidfile.write(old_pid)
            sys.exit(1)

        # Start the daemon
        if not self.foreground :
            self.daemonize()

        # Flush pid in pidfile
        try:
            lockfile.write("%s" % (os.getpid()))
            lockfile.flush()
        except IOError:
            print("Unable to write pid to the pidfile.")
            sys.exit(1)

        # Start the logger

        self.run()

    def restart(self):
        """
        Restart the daemon
        """
        self.stop()
        self.start()

    def stop(self):
        """
        Stop the daemon
        """
        # Get the pid from the pidfile
        pid = self.get_pid()

        if not pid:
            if os.path.exists(self.pidfile):
                os.remove(self.pidfile)

            return  # Not an error in a restart

        # Try killing the daemon process
        try:
            i = 0
            while True:
                os.kill(pid, signal.SIGTERM)
                time.sleep(0.1)
                i = i + 1
                if i % 10 == 0:
                    os.kill(pid, signal.SIGHUP)
        except OSError as err:
            err = str(err)
            if err.find("No such process") > 0:
                if os.path.exists(self.pidfile):
                    os.remove(self.pidfile)
            else:
                self.logger.warn(err)
                sys.exit(1)

    def daemonize(self):
        #Do first Fork
        try:
            pid = os.fork()
            if pid != 0:
                sys.exit(0)
        except OSError as e:
            sys.stderr.write(
                "fork #1 failed: %d (%s)\n" % (e.errno, e.strerror))
            sys.exit(1)

        os.chdir("/tmp")
        os.setsid()
        os.umask(022)

        # Do second fork
        try:
            pid = os.fork()
            if pid != 0:
                sys.exit(0)
        except OSError as e:
            sys.stderr.write(
                "fork #2 failed: %d (%s)\n" % (e.errno, e.strerror))
            sys.exit(1)

        devnull = "/dev/null"
        if hasattr(os, "devnull"):
            devnull = os.devnull

        devnull_fd = os.open(devnull, os.O_RDWR)
        os.dup2(devnull_fd, 0)
        os.dup2(devnull_fd, 1)
        os.dup2(devnull_fd, 2)
        os.close(devnull_fd)


        def sigtermhandler(signum, frame):
            self.daemon_alive = False
            sys.exit()

        signal.signal(signal.SIGTERM, sigtermhandler)
        signal.signal(signal.SIGINT, sigtermhandler)

        # Write pidfile
        atexit.register(self.quit)

    def quit(self):
        """cleanup pid file at exit"""
        sys.exit(0)

        if os.path.isfile(self.pidfile):
            with open(self.pidfile, "r") as old_pidfile:
                old_pid = old_pidfile.read()
        try:
            lockfile = open(self.pidfile, "w")
        except IOError:
            print("Unable to create the pidfile.")
            sys.exit(1)
        try:
            # locked.
            fcntl.flock(lopckfile, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except IOError:
            print("Unable to lock on the pidfile.")
            # We need to overwrite the pidfile if we got here.
            with open(self.pidfile, "w") as pidfile:
                pidfile.write(old_pid)
            sys.exit(1)


        # Start the daemon
        if not self.foreground :
            self.daemonize()


        # Flush pid in pidfile
        try:
            lockfile.write("%s" % (os.getpid()))
            lockfile.flush()
        except IOError:
            print("Unable to write pid to the pidfile.")
            sys.exit(1)

        # Start the logger
        self.run(*args, **kwargs)

    def run(self):
        """
        You should override this method when you subclass Daemon.
        daemonized by start() or restart().
        """
        raise NotImplementedError

'''
mutliprocces counter
'''
class Counter(object):
    def __init__(self):
        self.val = mp.Value('i', 0)

    def increment(self, n=1):
        with self.val.get_lock():
            self.val.value += n

    def reduce(self, n=1):
        with self.val.get_lock():
            self.val.value -= n

    @property
    def value(self):
        return self.val.value

proc_counter = Counter()

def update_counter():
    global proc_counter
    print("counter %d"%proc_counter.value)
    proc_counter.increment()

def reduce_counter():
    global proc_counter
    proc_counter.reduce()

class TestMain(Daemon):
    def main(self):
        #pdb.set_trace()
        if len(sys.argv) >= 2:
            if 'start' in sys.argv:
                self.start()
            elif 'stop' in sys.argv:
                self.stop()
            elif 'restart' in sys.argv:
                self.restart()
            else:
                print "Unknown command"
                sys.exit(2)
            sys.exit(0)
        else:
            print "usage: %s start|stop|restart other config" % sys.argv[0]
            sys.exit(2)

    def run(self):
        manager = Manager()
        proc_pool = {}
        task_cntl_queue = Queue()
        task_data_queue = Queue()
        exit_flag = mp.Event()

        signal.signal(signal.SIGHUP, lambda x, y: exit_flag.set())
        signal.signal(signal.SIGTERM, lambda x, y: exit_flag.set())
        signal.siginterrupt(signal.SIGHUP, False)
        signal.siginterrupt(signal.SIGTERM, False)

        print 'main {} started'.format(os.getpid())
        proc = mp.Process(target=self.proxy_task_process, 
                          args=(task_cntl_queue, task_data_queue, exit_flag))
        proc.start()
        proc_pid = proc.pid
        proc_pool[proc_pid] = proc
        update_counter()
        print 'proxy {} started'.format(proc.pid)

        while True:
            item = task_cntl_queue.get()
            if item['event'] == 'newtask':
                proc = mp.Process(target=self.task_worker, args=(task_cntl_queue, task_data_queue))
                proc.start()
                proc_pool[proc.pid] = proc
                update_counter()
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

            
    def task_worker(self,task_cntl_queue, task_data_queue):
        taskinfo = task_data_queue.get()
        print taskinfo
        print "pid %d"%(os.getpid())
        time.sleep(random.choice([10,20,30]))
        task_cntl_queue.put({'event': 'exit', 'pid': os.getpid()})
        pass

    def fetch_task_api(self):
        pass
    def failed_sleep(self):
        time.sleep(5)

    def proxy_task_process(self,task_cntl_queue, task_data_queue, exit_flag):
        while True:
            print("proc counter %d"%(proc_counter.value))
            if exit_flag.is_set():
                #if exit kill self
                task_cntl_queue.put({'event': 'exit', 'pid': os.getpid()})
                break

            print("proc counter %d"%(proc_counter.value))
            if proc_counter.value > 4:
                self.failed_sleep()
                print("====runing proc %d"%proc_counter.value)
                continue
            else:
                task_cntl_queue.put({'event': 'newtask'})
                taskinfo={"id":1}
                task_data_queue.put(taskinfo)
                time.sleep(1)



if __name__ == "__main__":
    test = TestMain()
    test.main()
    pass
