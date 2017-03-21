#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-08-25
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
import pdb
import os.path

from ConfigParser import ConfigParser
from optparse import OptionParser
import argparse
from error import ConfigError
import argparse

import sys

def str2bool(r):
    return r == "True"

def str2int(r):
    return int(r)

class DaemonConfig(object):
    def __new__(cls,*args,**kw):
        if not hasattr(cls,"_instance"):
            orig = super(DaemonConfig, cls)
            cls._instace = orig.__new__(cls, *args, **kw)
        return cls._instace

    def update_options(self,dabargs):
        """process options from command line and config file"""
        parser = argparse.ArgumentParser("[option]",description="daemon options from command line and config file")
        parser.add_argument("-c", "--config", dest="config",
                          help="use alternate configuration file", metavar="FILE",
                          default="/etc/dab/daemon.conf")

        parser.add_argument("-p","--pid", dest="pidfile",
                          help="run pid file")

        parser.add_argument("-l","--log", dest="logfile",
                          help="daemon log file")

        parser.add_argument("-v", "--verbose", action="store_true", default=False,
                          help="show verbose output")

        parser.add_argument("-d", "--debug", dest="debug", action="store_true", 
                            help="show debug output",default=False)


        parser.add_argument("--fg", dest="foreground",
                          action="store_true", default=False,
                          help="run in foreground")
        parser.add_argument("--forcelock", dest="forcelock",
                          action="store_true", default=False,
                          help="force lock for exclusive session")

        parser.add_argument("--appname", help="specify appname")
        parser.add_argument("--username", help="specify user")
        parser.add_argument("--password", help="specify password")

        parser.add_argument("--maxjobs", type=int, help="Specify maxjobs")
        parser.add_argument("--sleeptime", type=int, help="Specify the polling interval")
        parser.add_argument("--server", help="url for server api")
        parser.add_argument("--topurl", help="Specify topurl")

        parser.add_argument("--topdir", help="Specify topdir")
        parser.add_argument("--workdir", help="Specify workdir")
        parser.add_argument("--arches", help="Specify arches")


        options = parser.parse_args(args=dabargs)
        # load config
        if options.config:
            if os.path.exists(options.config):
                self.config = options.config
            else:
                raise ConfigError("not found config %s"%(config))
            self.confp = ConfigParser()
            self.confp.read(self.config)
            if not self.confp.has_section("daemon"):
                raise ConfigError("not found service section")
            
            for key ,value in self.confp.items("daemon"):
                if not getattr(self, key, None):
                    setattr(self, key, value)
        #merge options to config
        opt_list = vars(options)
        for key in opt_list.keys():
            if opt_list[key]:
                setattr(self, key, opt_list[key])
        if not isinstance(self.maxjobs, int):
            self.maxjobs = int(self.maxjobs)
        if not isinstance(self.sleeptime, int):
            self.sleeptime = int(self.sleeptime)
        if not isinstance(self.debug, bool):
            self.debug = str2bool(self.debug)
        if not isinstance(self.foreground, bool):
            self.foreground = str2bool(self.foreground)
        if not isinstance(self.forcelock, bool):
            self.forcelock = str2bool(self.forcelock)
        if not isinstance(self.verbose, bool):
            self.verbose = str2bool(self.verbose)

class DabsvConfig(object):
    def __new__(cls,*args,**kw):
        if not hasattr(cls,"_instance"):
            orig = super(DabsvConfig, cls)
            cls._instace = orig.__new__(cls, *args, **kw)
        return cls._instace

    def update_options(self,dabargs):
        """process options from command line and config file"""
        parser = argparse.ArgumentParser("[option]",description="service options from command line and config file")
        parser.add_argument("-c", "--config", dest="config",
                          help="use alternate configuration file", metavar="FILE",
                          default="/etc/dab/dabsv.conf")

        parser.add_argument("-d", "--debug", dest="debug", action="store_true", 
                            help="show debug output",
                            default=False)

        parser.add_argument("--dbtype", help="database type")
        parser.add_argument("--dbhost", help="database host ip")
        parser.add_argument("--dbport", help="database host port",type=int)
        parser.add_argument("--dbuname", help="database username")
        parser.add_argument("--dbpasswd", help="database password")

        options = parser.parse_args(args=dabargs)
        # load config
        if options.config:
            if os.path.exists(options.config):
                self.config = options.config
            else:
                raise ConfigError("not found config %s"%(config))
            self.confp = ConfigParser()
            self.confp.read(self.config)
            if not self.confp.has_section("service"):
                raise ConfigError("not found service section")
            
            for key ,value in self.confp.items("service"):
                if not getattr(self, key, None):
                    setattr(self, key, value)
        #merge options to config
        opt_list = vars(options)
        for key in opt_list.keys():
            if opt_list[key]:
                setattr(self, key, opt_list[key])
        if not isinstance(self.dbport, int):
            self.dbport = int(self.dbport)
        if not isinstance(self.debug, bool):
            self.debug = str2bool(self.debug)
        # if options.debug:
        #     self.debug = options.debug
        # if options.dbtype.lower() in "sqlite":
        #     pass
        pass

if __name__ == "__main__":
    opt = DaemonConfig()
    print sys.argv
    opt.update_options(sys.argv[1:])
    print(opt.__dict__)



