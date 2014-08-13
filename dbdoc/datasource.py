# encoding: utf-8
import os, sys
import MySQLdb

# connects to MySQL
class _MySQL(object):
    
    def __init__(self):
        self.con = None
        self.cursor = None
    
    def __del__(self):
        self.close()
    
    def connect(self, host, user, passwd, database, charset):
        if database is None:
            self.con = MySQLdb.connect(host=host, user=user, passwd=passwd, charset=charset)
        else:
            self.con = MySQLdb.connect(host=host, user=user, passwd=passwd, charset=charset, db=database)
        self.cursor = self.con.cursor()
    
    def close(self):
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

# connects to SQLite3
class _SQLite3(object):
    
    def __init__(self):
        pass
    
    def __del__(self):
        pass
    
    def connect(self, host, user, passwd, database, charset):
        pass
    
    def close(self):
        pass
    
    def get_columns(self, table):
        pass
    
    def get_table_status(self):
        pass

# connects to PostgreSQL
class _PostgreSQL(object):
    
    def __init__(self):
        pass
    
    def __del__(self):
        pass
    
    def connect(self, host, user, passwd, database, charset):
        pass
    
    def close(self):
        pass
    
    def get_columns(self, table):
        pass
    
    def get_table_status(self):
        pass

def factory(datasource):
    if datasource is 'mysql': return _MySQL()
    if datasource is 'sqlite': return _SQLite3()
    if datasource is 'postgresql': return _PostgreSQL()
    return None
