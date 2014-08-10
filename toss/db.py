import os, sys, MySQLdb
from pprint import pprint

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

def factory(options):
    # return TossMySQL(host=options['host'], user=options['user'], passwd=options['password'], database=options['database'], charset=options['charset'])
    return TossMySQL(host=options.host, user=options.user, passwd=options.password, database=options.database, charset=options.charset)