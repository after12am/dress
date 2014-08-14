# encoding: utf-8
import os, sys, shutil, tempfile, datetime, datasource
from jinja2 import Environment, FileSystemLoader
from pprint import pprint

# tell template dir path to jinja2
env = Environment(loader=FileSystemLoader('_templates'))

__dirname__ = os.path.dirname(os.path.abspath(__file__))
__static__  = os.path.join(__dirname__, '_static')

class Documentor(object):
     
    def __init__(self, name):
        self.name = name
        self.tempdir = create_temp_dir()
    
    # dest is relative path from tempdir
    def add(self, src, dest):
        output = os.path.join(self.tempdir, dest)
        if os.path.isdir(src):
            shutil.copytree(src, output)
        else:
            shutil.copyfile(src, output)
    
    def remove(self, src):
        pass
    
    def deploy(self):
        shutil.move(self.tempdir, './')
        os.rename(os.path.basename(self.tempdir), self.name)
    
    def locked(self):
        return os.path.exists(os.path.join(__dirname__, self.name))

class IndexDoc(object):
    
    def __init__(self):
        self.tempfile = create_temp_file()
        self.template = 'index.ctp'
        self.content = None
    
    def render(self, database, author, version):
        db = datasource.get_instance()
        data = {}
        data['name']   = database,
        data['tables'] = {}
        for item in db.get_table_status():
            table = item[0]
            data['tables'][table] = {}
            data['tables'][table]['status']  = item
            data['tables'][table]['columns'] = db.get_columns(table)
        # running data into template...
        self.content = env.get_template(self.template).render(
            database = data,
            version = version if version else '',
            author = author,
            today = datetime.datetime.today()
        )
    
    def save(self):
        if self.content is not None:
            with open(self.tempfile, 'w') as f:
                f.write(self.content.encode('utf-8'))
    
    def destroy(self):
        os.remove(self.tempfile)
    
    def path(self):
        return self.tempfile

# create temp directory and return the path
def create_temp_dir():
    return tempfile.mkdtemp()

# create temp file and return the path
def create_temp_file():
    f, path = tempfile.mkstemp()
    os.close(f)
    return path

# create database documentation
def export(database, author, version):
    
    doc = IndexDoc()
    doc.render(database=database, author=author, version=version)
    doc.save()
    
    # packaging the document
    documentor = Documentor('dbdoc')
    documentor.add(__static__, '_static')
    documentor.add(doc.path(), 'index.html')
    
    # delete temp file
    doc.destroy()
    
    # exporting the document
    if not documentor.locked():
        documentor.deploy()
    else:
        print "File exists error\n"
