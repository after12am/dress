# encoding: utf-8
import os, sys, shutil, tempfile, datetime, datasource, defs
from jinja2 import Environment, FileSystemLoader
from collections import OrderedDict
import helper

class Directory(object):
    
    def __init__(self, dirpath = None):
        self.temp = dirpath if dirpath else self._create()
    
    def __del__(self):
        self._destroy()
    
    @property
    def path(self):
        return self.temp
    
    # create docs and return the path
    def _create(self):
        return tempfile.mkdtemp()
    
    def _destroy(self):
        pass
    
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

class Documentor(Directory):
     
    def __init__(self, name):
        self.name = name
        self.temp = self._create()
    
    # dest is relative path from docs
    def add(self, file_or_dir, dest):
        output = os.path.join(self.temp, dest)
        copy = shutil.copytree if os.path.isdir(file_or_dir.path) else shutil.copyfile
        copy(file_or_dir.path, output)
        
    # delete docs
    def deploy(self):
        shutil.move(self.temp, './')
        os.rename(os.path.basename(self.temp), self.name)
    
    # whether docs exist or not
    def exists(self):
        return os.path.exists(os.path.join(defs.dirname, self.name))

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
    
    env = Environment(loader=FileSystemLoader(defs.template))
    
    def __init__(self):
        super(Template, self).__init__()

class IndexTemplate(Template):
    
    def render(self, docname, author, version):
        db = datasource.DB.getinstance()
        data = {}
        data['name']   = docname,
        # can't understand why there is a need to be converted to a string type
        data['name']   = data['name'][0]
        data['tables'] = OrderedDict()
        for table in db.get_tables():
            data['tables'][table] = {}
            data['tables'][table]['comment'] = db.get_table_comment(table)
            data['tables'][table]['columns'] = db.get_columns(table)
        # running data into template...
        data = Template.env.get_template('index.ctp').render(
            datasource = db.__class__.__name__.lower(),
            database = data,
            version = version,
            author = author,
            today = datetime.datetime.today()
        )
        super(IndexTemplate, self).render(data)

class SQLTemplate(Template):
    
    def render(self):
        db = datasource.DB.getinstance()
        data = db.get_create_statements()
        super(SQLTemplate, self).render(data)
        
# create database documentation
# def publish():
#     
#     
#     a = datasource.DB.connect()
#     print a
#     sys.exit()
#     from config import config
#     options = config(defs.config_name)
#     
#     project = "%s_%s" % (options.docname, options.version) if options.version else options.docname
#     static = Directory(__static__)
#     
#     # create database documentation page
#     doc = IndexTemplate()
#     doc.render(docname=options.docname, author=options.author, version=options.version)
#     doc.save()
#     
#     # create `create statements` page
#     stmts = SQLTemplate()
#     stmts.render()
#     stmts.save()
#     
#     # packaging the document
#     documentor = Documentor(project)
#     documentor.add(static, 'static')
#     documentor.add(doc, 'index.html')
#     documentor.add(stmts, 'sql.txt')
#     
#     # disconnecting from database
#     db.close()
#     
#     # exporting the document
#     if not documentor.exists():
#         documentor.deploy()
#     else:
#         sys.exit("Failed to create documentation. File exists error")
