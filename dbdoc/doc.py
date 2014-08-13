# encoding: utf-8
import os, sys, shutil, tempfile, db, datetime
from jinja2 import Template

# create work dir...
def setup():
    dirname = os.path.dirname(os.path.abspath(__file__))
    temp = tempfile.mkdtemp()
    if os.path.exists(temp):
        shutil.rmtree(temp)
    # copy static files
    shutil.copytree(dirname + '/_static', temp + '/_static')
    # return temp dir
    return temp

# run data into template
def render(temp, options):
    # dbdoc model object
    dbdoc = db.factory(
        host = options.host, 
        user = options.user, 
        passwd = options.password, 
        database = options.database, 
        charset = options.charset
    )
    
    # set table status
    tablestatus = {}
    for row in dbdoc.tablestatus():
        table = row[0]
        tablestatus.setdefault(table, {})
        tablestatus[table] = row
    
    # set colum info
    columns = {}
    for table in tablestatus:
        columns.setdefault(table, {})
        columns[table] = dbdoc.columns(table)
    
    # render
    dirname = os.path.dirname(os.path.abspath(__file__))
    data = open(dirname + '/_templates/index.ctp', 'r').read()
    template = Template(data.decode('utf8'))
    f = open(temp + '/index.html', 'w')
    f.write(template.render(
        database = options.database,
        tablestatus = tablestatus,
        columns = columns,
        version = options.version if options.version else '',
        author = options.author if options.author else '',
        date = datetime.datetime.today()
    ).encode("utf-8"))
    f.close()

# create database schema design document
def export(options, args = None):
    dirname = os.path.dirname(os.path.abspath(__file__))
    temp = setup()
    render(temp, options)
    # export document to {output}
    shutil.move(temp, './')
    if os.path.exists(dirname + '/htdocs'):
        shutil.rmtree(dirname + '/htdocs')
    os.rename(os.path.basename(temp), 'htdocs')
