# encoding: utf-8
import os, sys, shutil, tempfile, datetime, datasource
from jinja2 import Environment, FileSystemLoader

__dirname__  = os.path.dirname(os.path.abspath(__file__))
__static__   = os.path.join(__dirname__, '_static')
__template__ = '_templates'

class Documentor(object):
     
    def __init__(self, name):
        self.name = name
        self.temp = self.create()
    
    # create temp directory and return the path
    def create(self):
        return tempfile.mkdtemp()
    
    # dest is relative path from the temp dir
    def add(self, src, dest):
        output = os.path.join(self.temp, dest)
        copy = shutil.copytree if os.path.isdir(src) else shutil.copyfile
        copy(src, output)
    
    def remove(self, path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        elif os.path.exists(path):
            os.remove(path)
    
    # delete temp dir
    def deploy(self):
        shutil.move(self.temp, './')
        os.rename(os.path.basename(self.temp), self.name)
    
    def exists(self):
        return os.path.exists(os.path.join(__dirname__, self.name))

class File(object):
    
    def __init__(self):
        self.temp = self.create()
        self.buff = None
    
    def __del__(self):
        self.destroy()
    
    @property
    def path(self):
        return self.temp
    
    # create the temp file and return the path
    def create(self):
        f, path = tempfile.mkstemp()
        os.close(f)
        return path
    
    # delete the temp file
    def destroy(self):
        if os.path.exists(self.temp):
            os.remove(self.temp)
    
    def render(self, data):
        self.buff = data
    
    def save(self):
        if self.buff is not None:
            with open(self.temp, 'w') as f:
                f.write(self.buff.encode('utf-8'))

class Template(File):
    
    env = Environment(loader=FileSystemLoader(__template__))
    
    def __init__(self):
        super(Template, self).__init__()
        self.template = None

class IndexTemplate(Template):
    
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
        self.buff = Template.env.get_template('index.ctp').render(
            database = data,
            version = version if version else '',
            author = author,
            today = datetime.datetime.today()
        )

class SQLTemplate(Template):
    
    def render(self):
        db = datasource.get_instance()
        data = ""
        for table in db.get_tables():
            data += db.get_create_statement(table) + "\n\n"
        self.buff = data
        
# create database documentation
def export(database, author, version):
    # create database documentation page
    doc = IndexTemplate()
    doc.render(database=database, author=author, version=version)
    doc.save()
    
    # create `create statements` page
    stmts = SQLTemplate()
    stmts.render()
    stmts.save()
    
    # packaging the document
    documentor = Documentor('dbdoc_' + database)
    documentor.add(__static__, '_static')
    documentor.add(doc.path, 'index.html')
    documentor.add(stmts.path, 'sql.txt')
    
    # delete temp file
    doc.destroy()
    
    # exporting the document
    if not documentor.exists():
        documentor.deploy()
    else:
        print "File exists error\n"
