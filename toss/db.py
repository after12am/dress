# encoding: utf-8
import os, sys, MySQLdb

# object connects to MySQL
class TossMySQL(object):
    
    def __init__(self, host, user, passwd, database, charset):
        if database is None:
            self.con = MySQLdb.connect(host=host, user=user, passwd=passwd, charset=charset)
        else:
            self.con = MySQLdb.connect(host=host, user=user, passwd=passwd, charset=charset, db=database)
        self.cursor = self.con.cursor()
    
    def __del__(self):
        if hasattr(self, 'cursor'):
            self.cursor.close()
        if hasattr(self, 'con'):
            self.con.close()
    
    def tables(self):
        self.cursor.execute("show tables;")
        return (row[0] for row in self.cursor.fetchall())
    
    def columns(self, table):
        self.cursor.execute("show full columns from %s;" % table)
        return self.cursor.fetchall()
    
    def tablestatus(self):
        self.cursor.execute("show table status;")
        return self.cursor.fetchall()

# object connects to PostgresSQL
class TossPostgreSQL(object):
    
    def __init__(self, arg):
        super(TossPostgreSQL, self).__init__()
        self.arg = arg

# object connects to SQLite3
class TossSQLite3(object):
    
    def __init__(self, arg):
        super(TossSQLite3, self).__init__()
        self.arg = arg

def factory(host, user, passwd, database, charset):
    return TossMySQL(host=host, user=user, passwd=passwd, database=database, charset=charset)
