#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-08-25
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
import os.path

import pdb
from ConfigParser import ConfigParser
from optparse import OptionParser
from error import ConfigException

class DaemonConfig():
    def __init__(self,config="/etc/dab/daemon.conf"):
        if os.path.exists(config):
            self.config = config
        else:
            raise ConfigException("not found config %s"%(config))
        self.confp = ConfigParser()
        self.confp.read(self.config)
        if not self.confp.has_section("daemon"):
            raise ConfigException("not found daemon section")

    def update_options(self,options):
        if not hasattr(self,"options"):
            self.options = options
        for key ,value in self.confp.items("daemon"):
            if not getattr(self.options, key, None) :
                setattr(self.options, key, value)
            pass

        pass
    @classmethod
    def get_options(cls):
        """process options from command line and config file"""
        parser = OptionParser()
        parser.add_option("-c", "--config", dest="config",
                          help="use alternate configuration file", metavar="FILE",
                          default="/etc/dab/daemon.conf")

        parser.add_option("-p","--pid", dest="pidfile",
                          help="run pid file")

        parser.add_option("-l","--log", dest="logfile",
                          help="daemon log file")

        parser.add_option("-v", "--verbose", action="store_true", default=False,
                          help="show verbose output")
        parser.add_option("-d", "--debug", action="store_true", default=False,
                          help="show debug output")


        parser.add_option("--fg", dest="foreground",
                          action="store_true", default=False,
                          help="run in foreground")
        parser.add_option("--forcelock", dest="forcelock",
                          action="store_true", default=False,
                          help="force lock for exclusive session")

        parser.add_option("--appname", help="specify appname")
        parser.add_option("--username", help="specify user")
        parser.add_option("--password", help="specify password")

        parser.add_option("--maxjobs", type='int', help="Specify maxjobs")
        parser.add_option("--sleeptime", type='int', help="Specify the polling interval")
        parser.add_option("--server", help="url for server api")
        parser.add_option("--topurl", help="Specify topurl")

        parser.add_option("--topdir", help="Specify topdir")
        parser.add_option("--workdir", help="Specify workdir")
        (options, args) = parser.parse_args()
        return options

    pass

if __name__ == "__main__":
    opt = DaemonConfig.get_options()
    print(opt.__dict__)
    test = DaemonConfig(opt.config)
    test.update_options(opt)
    print(test.options.__dict__)
    print(test.options.workdir)

# daemon_config = "cbsd.conf"
# config = ConfigParser()
# config.read(daemon_config)
# for x in config.sections():
#     pass

# config.has_section("common")
# print config.items("common")
# print dict(config.items("cbsd"))

