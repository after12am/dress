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
        if hasattr(self, 'conn') and self.conn:
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
        if hasattr(self, 'conn') and self.conn:
            self.conn.close()
    
    def get_tables(self):
        self.cursor.execute("select name from sqlite_master where type = 'table'")
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
        self.cursor.execute("select sql from sqlite_master where type = 'table' and name = '%s'" % table)
        ret = self.cursor.fetchall()
        return ret[0][0]
        

class PostgreSQL(object):
    
    def __init__(self, host, user, password, database):
        self.conn = None
        self.cursor = None
        self.host = host
        self.user = user
        self.password = password
        self.database = database
    
    def __del__(self):
        self.close()
    
    def connect(self):
        import pgdb
        self.conn = pgdb.connect(host=self.host, user=self.user, \
            password=self.password, database=self.database)
        self.cursor = self.conn.cursor()
    
    def close(self):
        if hasattr(self, 'cursor') and self.cursor:
            self.cursor.close()
        if hasattr(self, 'conn') and self.conn:
            self.conn.close()
    
    def get_tables(self):
        self.cursor.execute("select relname as TABLE_NAME from pg_stat_user_tables;")
        return [item[0] for item in self.cursor.fetchall()]
    
    def get_columns(self, table):
        query = """
            select
                *
            from
                information_schema.columns
            where
                table_catalog = '%s'
            and table_name = '%s'
            order by ordinal_position;
        """
        self.cursor.execute(query % (self.database, table))
        columns_status = self.cursor.fetchall()
        comments = self.get_comments_related_to_columns(table)
        key_status = self.get_key_status(table)
        # merge comment on column
        columns_status = [item + ['', ''] for item in columns_status]
        for comment in comments:
            for k, info in enumerate(columns_status):
                if info[3] == comment[0]:
                    columns_status[k][-2] = comment[1]
        for key in key_status:
            for k, info in enumerate(columns_status):
                if info[3] in key[1]:
                    columns_status[k][-1] = key[0][0:3]
        return columns_status
    
    def get_comments_related_to_columns(self, table):
        query = """
            select
                pa.attname as COLUMN_NAME,
                pd.description as COLUMN_COMMENT
            from
                pg_stat_all_tables psat,
                pg_description pd,
                pg_attribute pa
            where
                psat.schemaname = (select schemaname from pg_stat_user_tables where relname = '%s')
            and psat.relname = '%s'
            and psat.relid = pd.objoid
            and pd.objsubid <> 0
            and pd.objoid = pa.attrelid
            and pd.objsubid = pa.attnum
            order by pd.objsubid;
        """
        self.cursor.execute(query % (table, table))
        return self.cursor.fetchall()
    
    def get_key_status(self, table):
        query = """
            select
                tc.constraint_name as CONSTRAINT_NAME,
                ccu.column_name as COLUMN_NAME,
                tc.constraint_type as CONSTRAINT_TYPE
            from
            	information_schema.table_constraints tc,
            	information_schema.constraint_column_usage ccu
            where
            	tc.table_catalog = '%s'
            and tc.table_name = '%s'
            and tc.table_catalog = ccu.table_catalog
            and tc.table_schema = ccu.table_schema
            and tc.table_name = ccu.table_name
            and tc.constraint_name = ccu.constraint_name
        """
        self.cursor.execute(query % (self.database, table))
        key = {}
        for item in self.cursor.fetchall():
            key.setdefault(item[0], [item[2], []])
            key[item[0]][1].append(item[1])
        values = key.values()
        for k, item in enumerate(values):
            if item[0].lower() == 'unique' and len(item[1]) >= 2:
                values[k][0] = 'MULTIPLE'
        return values
    
    def get_table_status(self):
        pass
    
    def get_table_comment(self, table):
        query = """
            select
                pd.description
            from
                pg_stat_user_tables psut, pg_description pd
            where
                psut.relname = '%s'
            and psut.relid = pd.objoid
            and pd.objsubid = 0;
        """
        self.cursor.execute(query % table)
        ret = self.cursor.fetchall()
        return ret[0][-1]
    
    def get_create_statement(self, table):
        # I think about how I output create statement
        # import commands
        # commands.getoutput("pg_dump -U postgres --schema-only my_db ")
        return ""

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
            server = "%s:%s" % (str(options.host), str(options.port),)
            cls.instance = PostgreSQL(host=server, user=options.user, \
                password=options.password, database=options.database)
        if hasattr(cls, 'instance') and cls.instance:
            cls.instance.connect()
            return True
        return False
    
    @classmethod
    def close(cls):
        if hasattr(cls, 'instance') and cls.instance:
            cls.instance.close()

def select(datasource):
    DataSource.select(datasource)

def connect(options):
    return DataSource.connect(options)

def close():
    DataSource.close()

def get_instance():
    return DataSource()
