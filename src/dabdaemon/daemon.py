#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-08-24
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
import fcntl
import atexit
import os
import sys
import time
import signal
import logging
from logging import handlers

import pdb
class Daemon(object):
    """
    A generic daemon class.
    Usage: subclass the Daemon class and override the run() method
    """
    def __init__(self, app=None, pid=None, user=None,
                 group=None,home_dir=None, umask=022, 
                 verbose=False,logger=None,foreground=False,options=None):
        if options is None:
            self.app = app
            self.pidfile = pid
            self.home_dir = home_dir
            self.verbose = verbose
            self.umask = umask
            self.daemon_alive = True
            self.logger = logger
            self.foreground = foreground
        else:
            self.app = options.appname
            self.pidfile = options.pidfile
            self.home_dir = options.workdir
            self.verbose = options.verbose
            self.umask = umask
            self.daemon_alive = True
            self.logger = options.logger
            self.foreground = options.foreground

        print(self.__dict__)

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

        os.chdir(self.home_dir)
        os.setsid()
        os.umask(self.umask)

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

        # uid, gid = -1, -1
        # if self.group:
        #     try:
        #         gid = grp.getgrnam(self.group).gr_gid
        #     except KeyError:
        #         print("Group {0} not found".format(self.group))
        #         sys.exit(1)

        # if self.user:
        #     try:
        #         uid = pwd.getpwnam(self.user).pw_uid
        #     except KeyError:
        #         print("User {0} not found.".format(self.user))
        #         sys.exit(1)

        # if uid != -1 or gid != -1:
        #     os.chown(self.pid, uid, gid)

        # if self.group:
        #     try:
        #         os.setgid(gid)
        #     except OSError:
        #         print("Unable to change gid.")
        #         sys.exit(1)

        # if self.user:
        #     try:
        #         uid = pwd.getpwnam(self.user).pw_uid
        #     except KeyError:
        #         print("User {0} not found.".format(self.user))
        #         sys.exit(1)
        #     try:
        #         os.setuid(uid)
        #     except OSError:
        #         print("Unable to change uid.")
        #         sys.exit(1)

        def sigtermhandler(signum, frame):
            self.daemon_alive = False
            sys.exit()

        signal.signal(signal.SIGTERM, sigtermhandler)
        signal.signal(signal.SIGINT, sigtermhandler)

        # Write pidfile
        atexit.register(self.quit)

    def quit(self):
        """cleanup pid file at exit"""
        self.logger.warn("Stopping %s daemon"%(self.app))
        os.remove(self.pidfile)
        sys.exit(0)
    
    def startlogger(self):
        if self.logger is None:
            self.logger = logging.getLogger(self.app)
            self.logger.setLevel(logging.DEBUG)
            self.logger.propagate = False
            #local log handler
            local_log = logging.FileHandler("/var/log/%s.log"%(self.app))
            
            if self.verbose:
                local_log.setLevel(logging.DEBUG)
            else:
                local_log.setLevel(logging.INFO)
            formatter = logging.Formatter("%(asctime)s %(name)s: %(message)s",
                                              "%b %e %H:%M:%S")
            local_log.setFormatter(formatter)
            self.logger.addHandler(local_log)

    def start(self, *args, **kwargs):
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
        self.startlogger()

        self.logger.warn("Starting %s daemon."%(self.app))
        self.run(*args, **kwargs)

    def stop(self):
        """
        Stop the daemon
        """
        # Get the pid from the pidfile
        pid = self.get_pid()

        if not pid:
            self.logger.warn("pidfile %s does not exist. Not running?\n" % self.pidfile)

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

    def restart(self):
        """
        Restart the daemon
        """
        self.stop()
        self.start()

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

    def is_running(self):
        pid = self.get_pid()

        if pid is None:
            self.logger.warn('Daemon %s is stopped'%(app))
        elif os.path.exists('/proc/%d' % pid):
            print('Process (pid %d) is running...' % pid)
        else:
            print('Process (pid %d) is killed' % pid)

        return pid and os.path.exists('/proc/%d' % pid)

    def run(self):
        """
        You should override this method when you subclass Daemon.
        daemonized by start() or restart().
        """
        raise NotImplementedError
