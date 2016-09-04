#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-09-02
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
from da.tasks import Task as daTask
from da.source import Source as daSource
from dabdb.dbconn import dbinit
from sqlalchemy.sql import text

import pdb

def get_list_daemoncli(session,channelname,hostname):
    """ get task  """
    #sqlt = {"channelname":"dptest","hostname":"dptest"}
    sqlcmd = """select taskinfo.id,state,
    to_char(create_time,'MM-DD-YYYY HH24:MI:SS'),taskinfo.build_name,
    srcinfo.name,srcinfo.version,srcinfo.dsc_file 
    from taskinfo join srcinfo on srcinfo.id = taskinfo.src_id  
    where taskinfo.channel_name='%s' and taskinfo.host_name='%s'"""%(channelname,
                                                                     hostname)

    dbfetch = session.execute(sqlcmd)
    dataset = dbfetch.fetchall()
    return dataset

if __name__ == "__main__":
    db,session = dbinit("postgres")
    ret_data = task_get(session,"dptest","dptest")
    print(ret_data)
    pass
    
