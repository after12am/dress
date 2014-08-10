import os, sys, db
from jinja2 import Template

def export(options, args = None):
    
    dbo = db.factory(options)
    
    # set table status
    tablestatus = {}
    for row in dbo.tablestatus():
        table = row[0]
        tablestatus.setdefault(table, {})
        tablestatus[table] = row
    
    # set colum info
    columns = {}
    for table in tablestatus:
        columns.setdefault(table, {})
        columns[table] = dbo.columns(table)
    
    # render
    dirname = os.path.dirname(os.path.abspath(__file__))
    template = Template(open('%s/template/index.tpl' % dirname, 'r').read())
    print template.render(
        database = options['database'],
        tablestatus = tablestatus,
        columns = columns
    )
