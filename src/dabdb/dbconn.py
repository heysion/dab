from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *
from sqlalchemy.engine.url import URL

class SQLBase():
    def __init__(self,dbsetting):
        self.conn = create_engine(URL(**dbsetting))

    def getconn(self):
        if hasattr(self,"conn"):
            return self.conn
        else:
            return None
    pass

class PgConn(SQLBase):
    pass

class SqliteConn(SQLBase):
    pass
# engine = create_engine('sqlite:///dabdb.db')
# Base.metadata.bind = engine
# DBSession = sessionmaker(bind=engine)
"""
postgresql 0
sqlite3 1
"""
DATABASE = {
    'drivername': 'postgres',
    'host': '192.168.122.10',
    'port': '5432',
    'username': 'postgres',
    'password': 'qwe123',
    'database': 'dabdb'
}

def dbinit(dbtype="postgre",dbsetting=DATABASE):
    if dbtype == "postgre":
        db = PgConn(dbsetting)
        return db
    elif dbtype == "sqlite3":
        db = SqliteConn(dbsetting)
        return db
    else:
        return None

import pdb

if __name__ == "__main__":
    dbase = dbinit()
    e = dbase.getconn()
    import da
    from da.users import User
    User.metadata.create_all(e)
    DBSession = da.da_session(bind=e)
    sesion = DBSession()
    new_obj = User(name="test")
    sesion.add(new_obj)
    sesion.commit()
    print(dbase)
    print(sesion.__dict__)
    pdb.set_trace()