#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-09-02
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
from models import Task as dbTask
from models import Source as dbSource
from dab.db import Base
#from dab.db.dbconn import dbinit
# from sqlalchemy.sql import text
from datetime import datetime

#import pdb
class Taskinfo:
    def __init__(self,database):
        self.db = database
        Base.Meta.datebase = database

    def get_list_daemoncli(self,channelname,hostname):
        """ get task  """
        sqlcmd = """select taskinfo.id,state,
        to_char(create_time,'MM-DD-YYYY HH24:MI:SS'),taskinfo.build_name,
        srcinfo.name,srcinfo.version,srcinfo.dsc_file 
        from taskinfo join srcinfo on srcinfo.id = taskinfo.src_id  
        where taskinfo.channel_name='%s' and taskinfo.host_name='%s'"""%(channelname,
                                                                         hostname)
        dbfetch = self.db.execute(sqlcmd)
        dataset = dbfetch.fetchall()
        return dataset

        def get_top_daemoncli(session,channelname,hostname,count=1):
            """ get task  """
            #sqlt = {"channelname":"dptest","hostname":"dptest"}
            sqlcmd = """select taskinfo.id,state,
            to_char(create_time,'MM-DD-YYYY HH24:MI:SS'),taskinfo.build_name,
            srcinfo.name,srcinfo.version,srcinfo.dsc_file 
            from taskinfo join srcinfo on srcinfo.id = taskinfo.src_id  
            where taskinfo.channel_name='%s' and taskinfo.host_name='%s' 
            and (state=0 or state=NULL) order by id asc limit %d """%(channelname,
                                                                      hostname,int(count))

            dbfetch = self.db.execute(sqlcmd)
            dataset = dbfetch.fetchall()
        return dataset


        def update_daemoncli(self,taskid,channelname,
                             hostname,state,starttime=None,
                             completiontime=None):
            task_obj = self.db.query(daTask).filter(daTask.id==taskid).first()
            if not task_obj:
                return False
            if task_obj.state in (0,None) and state == 100:
                task_obj.start_time = datetime.now()
            if state in (400,500):
                task_obj.completion_time = datetime.now()
            task_obj.state = state
            self.db.commit()
            return True
        # 0 init 100 submit 200 start 300 build 400 failed 500 success 

# if __name__ == "__main__":
#     db,session = dbinit("postgres")
#     ret_data = update_daemoncli(session,11,
#                                 channelname=None,hostname="dptest",
#                                 state=400,starttime=None,
#                                 completiontime=None)
#     print(ret_data)
#     pass
    
