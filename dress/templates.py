# encoding: utf-8
import datetime
import datasource
from collections import OrderedDict
from jinja2 import Environment, FileSystemLoader
from archives import File

class Template(File):
    
    env = Environment(loader=FileSystemLoader('_templates'))
    
    def __init__(self, name):
        super(Template, self).__init__(name)


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

