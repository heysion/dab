from dab_models import Package
from dab_dbconnection import dbconn
import pdb

class DABBuild():
    def all(self):
        print "build all package"
        pass

    def update_src_changelog(self,bp):
        '''dch -v ${package_ver}+git~${package_commid} -D unstable "rebuild for deepin-sh"'''
        pass
    
    def package(self,bp):
        print "build package"
        '''debuild -e USE_GGCGO=1 -e CGO_ENABLED=1 -us -uc -sa -j8'''
        pass

    def dput_package(self,bp):
        pass

class BuildPackage():
    def __init__(self,name):
        self._session = dbconn()
        self.bp = self._session.query(Package).filter(Package.package_name == name).one()
    
    def update_ver(self):
        print "update db version"
        self.bp.package_build_freq  = self.bp.package_build_freq if self.bp.package_build_freq else 0+ 1
        pass

    def commit(self):
        self._session.commit()

    def bprint(self):
        print(self.bp.package_name,self.bp.package_version_main,self.bp.package_build_freq)

class DABCli():
    def __init__(self,opt):
        self._opt = opt
        self._build = DABBuild()


    def run(self):
        if self._opt.build_all_package:
            self._build.all()
        else:
            bp = BuildPackage(self._opt.package_name)
            #bp.bprint()
            if self._opt.update_verb_version:
                bp.update_ver()
            self._build.package(bp)
            bp.commit()
            #bp.bprint()
