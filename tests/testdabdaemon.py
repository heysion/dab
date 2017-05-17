#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-08-24
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''

import time
import sys

import os

sys.path.append("../dabdaemon/")

from daemon import Daemon

class App(Daemon):
    def run(self):
        while True:
            print("Howdy!  Gig'em!  Whoop!")
            time.sleep(10)

if __name__ == "__main__":
    app = App(app="test",pid="/tmp/test.pid",foreground=True,verbose=True)
    #app = App(pidfile="/tmp/test.pid")
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            app.start()
        elif 'stop' == sys.argv[1]:
            app.stop()
        elif 'restart' == sys.argv[1]:
            app.restart()
        else:
            print "Unknown command"
            sys.exit(2)
        sys.exit(0)
    else:
        print "usage: %s start|stop|restart" % sys.argv[0]
        sys.exit(2)
