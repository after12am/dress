# encoding: utf-8
import os, sys, shutil, tempfile, datetime, datasource
from jinja2 import Environment, FileSystemLoader
from collections import OrderedDict
import helper

__dirname__  = os.path.dirname(os.path.abspath(__file__))
__static__   = os.path.join(__dirname__, '_static')
__template__ = '_templates'

class Documentor(object):
     
    def __init__(self, name):
        self.name = name
        self.temp = self._create()
    
    def __del__(self):
        self._destroy()
    
    # create docs and return the path
    def _create(self):
        return tempfile.mkdtemp()
    
    def _destroy(self):
        pass
    
    # dest is relative path from docs
    def add(self, src, dest):
        output = os.path.join(self.temp, dest)
        copy = shutil.copytree if os.path.isdir(src) else shutil.copyfile
        copy(src, output)
    
    # remove specified file from docs
    def remove(self, path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        elif os.path.exists(path):
            os.remove(path)
    
    # delete docs
    def deploy(self):
        shutil.move(self.temp, './')
        os.rename(os.path.basename(self.temp), self.name)
    
    # whether docs exist or not
    def exists(self):
        return os.path.exists(os.path.join(__dirname__, self.name))

class File(object):
    
    def __init__(self):
        self.temp = self._create()
        self.buff = None
    
    def __del__(self):
        self._destroy()
    
    @property
    def path(self):
        return self.temp
    
    # create the temp file and return the path
    def _create(self):
        f, path = tempfile.mkstemp()
        os.close(f)
        return path
    
    # delete the temp file
    def _destroy(self):
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

class IndexTemplate(Template):
    
    def render(self, database, author, version):
        db = datasource.get_instance()
        data = {}
        data['name']   = database,
        # can't understand why there is a need to be converted to a string type
        data['name']   = data['name'][0]
        data['tables'] = OrderedDict()
        for table in db.get_tables():
            data['tables'][table] = {}
            data['tables'][table]['comment'] = db.get_table_comment(table)
            data['tables'][table]['columns'] = db.get_columns(table)
        # running data into template...
        self.buff = Template.env.get_template('index.ctp').render(
            datasource = db.__class__.__name__.lower(),
            database = data,
            version = version,
            author = author,
            today = datetime.datetime.today()
        )

class SQLTemplate(Template):
    
    def render(self):
        db = datasource.get_instance()
        self.buff = db.get_create_statements()
        
# create database documentation
def publish(database, author, version):
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
    documentor.add(__static__, 'static')
    documentor.add(doc.path, 'index.html')
    documentor.add(stmts.path, 'sql.txt')
    
    # exporting the document
    if not documentor.exists():
        documentor.deploy()
    else:
        print "File exists error\n"
