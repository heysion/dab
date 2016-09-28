# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado

import tornado.httpserver
import tornado.web
import tornado.ioloop
import psycopg2
import psycopg2.pool

from tornado.options import define ,options
import urls as models

define("port", default = 8080, help = "run on the given port", type = int)
define("db_host", default = "db_host", help = "community database host")
define("db_database", default = "db_name", help = "community database name")
define("db_port", default = 5432, help = "db port", type = int)
define("db_user", default = "db_user", help = "community database user")
define("db_password", default = "db_password", help = "community database password")
minconn=4
maxconn=16
class App(tornado.web.Application):
    def __init__(self):
        settings = dict(
            debug = True,
            #xsrf_cookies = True,
            cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
        )
        handlers = [
#            (r"/",None),
        ]
        """host='localhost' dbname='my_database' user='postgres' password='secret'"""
        #self._pool = psycopg2.pool.SimpleConnectionPool(minconn, maxconn,host="192.168.122.10",port=5432,password="qwe123",user="postgres",dbname="dabdb")
        handlers.extend(models.sub_handles)
        tornado.web.Application.__init__(self,handlers,**settings)

def run_server():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(App())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    pass

if __name__ == "__main__":
    run_server()
    pass
