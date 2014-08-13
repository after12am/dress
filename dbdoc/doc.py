# encoding: utf-8
import os, sys, shutil, tempfile, datetime
from jinja2 import Environment, FileSystemLoader
from db import factory
from pprint import pprint

__dirname__ = os.path.dirname(os.path.abspath(__file__))
__static__  = os.path.join(__dirname__, '_static')
__output__  = 'htdocs'

# create temp dir and return the path
def create_temp_dir():
    return tempfile.mkdtemp()

def setup(tempdir):
    # copy static files
    shutil.copytree(__static__, os.path.join(tempdir, '_static'))

# running data into template...
def render(output, content):
    with open(output, 'w') as f:
        f.write(content.encode('utf-8'))

# create database documentation
def export(options, args = None):
    tempdir = create_temp_dir()
    setup(tempdir)
    
    db = factory(host=options.host, user=options.user, passwd=options.password, database=options.database, charset = options.charset)
    env = Environment(loader=FileSystemLoader('_templates'))
    
    database = {
        'name'  : options.database,
        'tables': {}
    }
    
    for item in db.get_table_status():
        table = item[0]
        database['tables'][table] = {}
        database['tables'][table]['status']  = item
        database['tables'][table]['columns'] = db.get_columns(table)
    
    template = env.get_template('index.ctp')
    output = os.path.join(tempdir, 'index.html')
    render(output, template.render(
        database = database,
        version = options.version if options.version else '',
        author = options.author if options.author else '',
        today = datetime.datetime.today()
    ))
    
    shutil.move(tempdir, './')
    if os.path.exists(os.path.join(__dirname__, __output__)):
        # have to alert the error
        print "file exists error"
    os.rename(os.path.basename(tempdir), __output__)