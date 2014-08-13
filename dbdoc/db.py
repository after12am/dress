# encoding: utf-8
import os, sys
import MySQLdb

# object connects to MySQL
class _MySQL(object):
    
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
    
    def get_columns(self, table):
        self.cursor.execute("show full columns from %s;" % table)
        return self.cursor.fetchall()
    
    def get_table_status(self):
        self.cursor.execute("show table status;")
        return self.cursor.fetchall()

# object connects to PostgresSQL
class _PostgreSQL(object):
    
    def __init__(self, host, user, passwd, database, charset):
        pass
    
    def __del__(self):
        pass
    
    def get_columns(self, table):
        pass
    
    def get_table_status(self):
        pass

# object connects to SQLite3
class _SQLite3(object):
    
    def __init__(self, host, user, passwd, database, charset):
        pass
    
    def __del__(self):
        pass
    
    def get_columns(self, table):
        pass
    
    def get_table_status(self):
        pass

def factory(host, user, passwd, database, charset):
    return _MySQL(host, user, passwd, database, charset)