#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-08-25
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
import time
import sys
import logging
from logging import handlers

from daemon import Daemon
from dab.util.config import DaemonConfig
from dab.api.daemon import HttpDaemonApi

import pdb

class DabDaemon(Daemon):
    def __init__(self):
        default_config = "../../etc/daemon.conf"
        self.opt = DaemonConfig.get_options()

        #test config
        self.opt.config = default_config

        self.daemon_config = DaemonConfig(self.opt.config)
        self.daemon_config.update_options(self.opt)
        self.initlogger()
        super(DabDaemon,self).__init__(options=self.daemon_config.options)

    def initlogger(self):
        options = self.daemon_config.options
        if not hasattr(options,"logger"):
            options.logger = logging.getLogger(options.appname)
        
        options.logger.setLevel(logging.DEBUG)
        options.logger.propagate = False
        local_log = logging.FileHandler("%s"%(options.logfile))
        
        if options.verbose:
            local_log.setLevel(logging.DEBUG)
        else:
            local_log.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s %(name)s: %(message)s",
                                                  "%b %e %H:%M:%S")
        local_log.setFormatter(formatter)
        options.logger.addHandler(local_log)
        
    def main(self):
        print(self.daemon_config.options.__dict__)
        if len(sys.argv) >= 2:
            if 'start' == sys.argv[1]:
                self.start(self.daemon_config)
            elif 'stop' == sys.argv[1]:
                self.stop()
            elif 'restart' == sys.argv[1]:
                self.restart()
            else:
                print "Unknown command"
                sys.exit(2)
            sys.exit(0)
        else:
            print "usage: %s start|stop|restart other config" % sys.argv[0]
            sys.exit(2)

    def run(self,daemonconfig):
        taskapi = HttpDaemonApi(daemonconfig)
        while True:
            print("Howdy!  Gig'em!  Whoop!")
            #taskapi.daemon_fetch_task_list(channelname="dptest")
            time.sleep(10)
    

class TestMain(DabDaemon):
    def run(self,daemonconfig):
        taskapi = HttpDaemonApi(daemonconfig)
        while True:
            print("Howdy!  Gig'em!  Whoop!")
            #taskapi.daemon_fetch_task_list(channelname="dptest")
            time.sleep(10)
    pass

if __name__ == "__main__":
    app = TestMain()
    app.main()
# if __name__ == "__main__":
#     opt = DaemonConfig.get_options()
#     if opt.config == "/etc/dab/daemon.conf":
#         opt.config = default_config
#     test = DaemonConfig(opt.config)
#     test.update_options(opt)
#     initlogger(test.options)
#     print(test.options.__dict__)
#     app = AppMain(options=test.options)
#     if len(sys.argv) >= 2:
#         if 'start' == sys.argv[1]:
#             app.start(test)
#         elif 'stop' == sys.argv[1]:
#             app.stop()
#         elif 'restart' == sys.argv[1]:
#             app.restart()
#         else:
#             print "Unknown command"
#             sys.exit(2)
#         sys.exit(0)
#     else:
#         print "usage: %s start|stop|restart other config" % sys.argv[0]
#         sys.exit(2)
