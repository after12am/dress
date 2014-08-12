import os, sys, shutil, tempfile, db
from jinja2 import Template

def setup():
    dirname = os.path.dirname(os.path.abspath(__file__))
    temp = tempfile.mkdtemp()
    if os.path.exists(temp):
        shutil.rmtree(temp)
    # copy static files
    shutil.copytree(dirname + '/_static', temp + '/_static')
    # return temp dir
    return temp

def render(temp, options):
    # toss model object
    toss = db.factory(host=options.host, user=options.user, passwd=options.password, database=options.database, charset=options.charset)
    
    # set table status
    tablestatus = {}
    for row in toss.tablestatus():
        table = row[0]
        tablestatus.setdefault(table, {})
        tablestatus[table] = row
    
    # set colum info
    columns = {}
    for table in tablestatus:
        columns.setdefault(table, {})
        columns[table] = toss.columns(table)
    
    # render
    dirname = os.path.dirname(os.path.abspath(__file__))
    data = open(dirname + '/_templates/index.ctp', 'r').read()
    template = Template(data.decode('utf8'))
    f = open(temp + '/index.html', 'w')
    f.write(template.render(
        database = options.database,
        tablestatus = tablestatus,
        columns = columns
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