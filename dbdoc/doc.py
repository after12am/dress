# encoding: utf-8
import os, sys, shutil, tempfile, datetime, datasource
from jinja2 import Environment, FileSystemLoader
from pprint import pprint

__dirname__ = os.path.dirname(os.path.abspath(__file__))
__static__  = os.path.join(__dirname__, '_static')
__output__  = '%s.dbdoc'

# create temp dir and return the path
def create_temp_dir():
    tempdir = tempfile.mkdtemp()
    shutil.copytree(__static__, os.path.join(tempdir, '_static'))
    return tempdir

# save file to...
def save(output, content):
    with open(output, 'w') as f:
        f.write(content.encode('utf-8'))

# running data into template and save as html
def render(tempdir, options):
    # get datasource instance
    db = datasource.factory(options.datasource)
    if db is None:
        sys.exit('Unknown datasource')
    db.connect(host=options.host, user=options.user, passwd=options.password, database=options.database, charset = options.charset)
    # create data
    database = {}
    database['name']   = options.database,
    database['tables'] = {}
    for item in db.get_table_status():
        table = item[0]
        database['tables'][table] = {}
        database['tables'][table]['status']  = item
        database['tables'][table]['columns'] = db.get_columns(table)
    # output
    env = Environment(loader=FileSystemLoader('_templates'))
    template = env.get_template('index.ctp')
    output = os.path.join(tempdir, 'index.html')
    save(output, template.render(
        database = database,
        version = options.version if options.version else '',
        author = options.author,
        today = datetime.datetime.today()
    ))

# create database documentation
def export(options, args = None):
    tempdir = create_temp_dir()
    render(tempdir, options)
    if os.path.exists(os.path.join(__dirname__, __output__ % options.database)):
        sys.exit("file exists error")
    shutil.move(tempdir, './')
    os.rename(os.path.basename(tempdir), __output__ % options.database)
