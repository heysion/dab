#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2017-03-27
@author: Heysion Yuan
@copyright: 2017, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
import os
import sys
import imp

pysettings_path="/home/ndk/deepin-work/src-code-repo/deepin-auto-build/etc/settings.py"
print pysettings_path
print sys.path
if os.path.exists(pysettings_path):
    print "load "+os.path.basename(pysettings_path)+" found"
    sys.path.append(os.path.dirname(pysettings_path))
    from settings import EnvDabsv
    dd = EnvDabsv.getdatabase()
    if locals().has_key("EnvDabsv1"):
        print "yes"
    else:
        print "no"
else:
    print sys.path
    print "load "+os.path.basename(pysettings_path)+" not found"
