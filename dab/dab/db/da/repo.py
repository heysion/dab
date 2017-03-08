#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2016-08-19
@author: Heysion Yuan
@copyright: 2016, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
from sqlalchemy import Column, ForeignKey, Integer, String

from __init__ import Base,da_session,da_create_engine
from __init__ import da_init_test as dainit


class RepoCtl(Base):
    __tablename__ = 'repoctl'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    package_name = Column(String(256), ForeignKey("pkginfo.name"))
    version = Column(String(256))

    def add_repoctl(self, session, reponame, pkgname, pkgversion):
        if self.package is None or self.build is None:
            u = session.query(Package).join(Build).filter(
                Package.name==pkgname,
                Build.package_name==pkgname,
                Build.version==pkgversion).dsec(Build.id).first()
            if u is None:
                raise DabdbError("not found user name")
            else:
            print(u)
        self.name = reponame
        self.package_name = pkgname
        self.version = pkgversion
        session.add(self)
        session.flush()
        pass

    def del_repoctl(self,session):
        if self.package is None or self.build is None:
            raise DabdbError("not found  pkginfo")
            # u = session.query(Package).join(Build).filter(
            #     Package.name==pkgname,
            #     Build.package_name==pkgname,
            #     Build.version==pkgversion).dsec(Build.id).first()
            # if u is None:
            #     raise DabdbError("not found user name")
            self.name = reponame
            self.package_name = p
            self.version = pkgversion
        else:
            xx
        session.add(self)
        session.flush()


class Repo(Base):
    __tablename__ = 'repoinfo'
    name = Column(String(256))
    repoctl_name = Column(String(256))
    update_time = Column(String(20))
    repo_config = Column(String(256))
    enabled = Column(Boolean)
    

def run_test():
    session = dainit(True)
    new_obj = Repo(name="test")
    session.add(new_obj)
    session.commit()

if __name__ == "__main__":
    run_test()
    pass    
