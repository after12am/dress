# encoding: utf-8
import os, sys

class MySQL(object):
    
    def __init__(self, host, user, password, charset, database):
        self.conn = None
        self.cursor = None
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
    
    def __del__(self):
        self.close()
    
    def connect(self):
        import MySQLdb
        self.conn = MySQLdb.connect(host=self.host, user=self.user, \
            passwd=self.password, charset=self.charset, db=self.database)
        self.cursor = self.conn.cursor()
    
    def close(self):
        if hasattr(self, 'cursor') and self.cursor:
            self.cursor.close()
        if hasattr(self, 'con') and self.conn:
            self.conn.close()
    
    def get_tables(self):
        self.cursor.execute("show tables;")
        return [item[0] for item in self.cursor.fetchall()]
    
    def get_columns(self, table):
        self.cursor.execute("show full columns from %s;" % table)
        return self.cursor.fetchall()
    
    # not compatible with other datasource
    def get_table_status(self):
        self.cursor.execute("show table status;")
        return self.cursor.fetchall()
    
    def get_table_comment(self, table):
        self.cursor.execute("show table status where name = '%s';" % table)
        ret = self.cursor.fetchall()
        return ret[0][-1]
    
    def get_create_statement(self, table):
        self.cursor.execute("show create table %s;" % table)
        ret = self.cursor.fetchall()
        return ret[0][1]

class SQLite3(object):
    
    def __init__(self, database):
        self.conn = None
        self.cursor = None
        self.database = database
        self.timeout = 5000
    
    def __del__(self):
        self.close()
    
    def connect(self):
        import sqlite3
        self.conn = sqlite3.connect(self.database, timeout = self.timeout)
        self.cursor = self.conn.cursor()
    
    def close(self):
        if hasattr(self, 'cursor') and self.cursor:
            self.cursor.close()
        if hasattr(self, 'con') and self.conn:
            self.conn.close()
    
    def get_tables(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
        return [item[0] for item in self.cursor.fetchall()]
    
    def get_columns(self, table):
        self.cursor.execute("pragma table_info('%s')" % table)
        return self.cursor.fetchall()
        
    
    def get_table_status(self):
        pass
    
    def get_table_comment(self, table):
        # can not set table comment in sqlite
        return ''
        
    def get_create_statement(self, table):
        self.cursor.execute("SELECT sql FROM sqlite_master WHERE type = 'table' AND name = '%s'" % table)
        ret = self.cursor.fetchall()
        return ret[0][0]
        

class PostgreSQL(object):
    
    def __init__(self, host, user, password, charset, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
    
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
    
    def get_create_statement(self, table):
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
    def connect(cls, options):
        if cls.datasource == 'mysql':
            cls.instance = MySQL(host=options.host, user=options.user, \
                password=options.password, charset=options.charset, database=options.database)
        if cls.datasource == 'sqlite3':
            cls.instance = SQLite3(options.database)
        if cls.datasource == 'postgresql':
            cls.instance = PostgreSQL(host=options.host, user=options.user, \
                password=options.password, charset=options.charset, database=options.database)
        if hasattr(cls, 'instance') and cls.instance:
            cls.instance.connect()
    
    @classmethod
    def close(cls):
        if hasattr(cls, 'instance') and cls.instance:
            cls.instance.close()

def select(datasource):
    DataSource.select(datasource)

def connect(options):
    DataSource.connect(options)

def close():
    DataSource.close()

def get_instance():
    return DataSource()
