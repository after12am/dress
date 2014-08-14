# encoding: utf-8
import os, sys

class MySQL(object):
    
    def __init__(self, **kwargs):
        self.con = None
        self.cursor = None
        self.host = kwargs['host']
        self.user = kwargs['user']
        self.password = kwargs['password']
        self.database = kwargs['database']
        self.charset = kwargs['charset']
    
    def __del__(self):
        self.close()
    
    def connect(self):
        import MySQLdb
        self.con = MySQLdb.connect(host=self.host, user=self.user, passwd=self.password, charset=self.charset, db=self.database)
        self.cursor = self.con.cursor()
    
    def close(self):
        if hasattr(self, 'cursor') and self.cursor:
            self.cursor.close()
        if hasattr(self, 'con') and self.con:
            self.con.close()
    
    def get_columns(self, table):
        self.cursor.execute("show full columns from %s;" % table)
        return self.cursor.fetchall()
    
    def get_table_status(self):
        self.cursor.execute("show table status;")
        return self.cursor.fetchall()

class SQLite3(object):
    
    def __init__(self, **kwargs):
        pass
    
    def __del__(self):
        pass
    
    def connect(self):
        pass
    
    def close(self):
        pass
    
    def get_columns(self, table):
        pass
    
    def get_table_status(self):
        pass

class PostgreSQL(object):
    
    def __init__(self, **kwargs):
        pass
    
    def __del__(self):
        pass
    
    def connect(self):
        pass
    
    def close(self):
        pass
    
    def get_columns(self, table):
        pass
    
    def get_table_status(self):
        pass

class DataSource(object):
    
    def __new__(cls, *args, **kwargs):
        if hasattr(cls, 'instance'):
            return cls.instance
        return None
    
    @classmethod
    def select(cls, datasource):
        cls.datasource = datasource
    
    @classmethod
    def connect(cls, **kwargs):
        if cls.datasource == MySQL.__name__.lower(): cls.instance = MySQL(**kwargs)
        if cls.datasource == SQLite3.__name__.lower(): cls.instance = _SQLite3(**kwargs)
        if cls.datasource == PostgreSQL.__name__.lower(): cls.instance = _PostgreSQL(**kwargs)
        if hasattr(cls, 'instance') and cls.instance:
            cls.instance.connect()
    
    @classmethod
    def close(cls):
        if hasattr(cls, 'instance') and cls.instance:
            cls.instance.close()

def select(datasource):
    DataSource.select(datasource)

def connect(**kwargs):
    DataSource.connect(**kwargs)

def close():
    DataSource.close()

def get_instance():
    return DataSource()
