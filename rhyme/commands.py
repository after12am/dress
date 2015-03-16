import os, sys, defs
from optparse import OptionParser
from documentor import *

# create configuration file
def config():
    
    parser = OptionParser(
        usage="%prog [options]",
        # version="%prog pre-alpha",
        add_help_option=False
    )
    
    parser.add_option(
        "-d", "--datasource", 
        dest="datasource",
        help="Supported database. Supported are mysql, sqlite3, postgres",
        type="string",
        default=None
    )
    
    parser.add_option(
        "--help", "--usage", 
        action='help'
    )
    
    (options, args) = parser.parse_args()
    
    config = dict(
        version = '',
        author = '',
        docname = 'sample',
        datasource = 'Database/MySQL',
        user = 'user',
        password = 'password',
        database = 'database',
        host = '127.0.0.1',
        port = '3306',
        charset = 'utf8'
    )
    
    if options.datasource.lower() == 'postgres':
        config = dict(
            version = '',
            author = '',
            docname = 'sample',
            datasource = 'Database/PostgreSQL',
            user = 'user',
            password = 'password',
            database = 'database',
            host = '127.0.0.1',
            port = '5432',
            charset = 'utf8'
        )
    elif options.datasource.lower() == 'sqlite3':
        config = dict(
            version = '',
            docname = 'docname',
            author = '',
            datasource = 'Database/SQLite3'
        )
    
    if not os.path.exists(defs.config_name):
        with open(defs.config_name, 'w') as f:
            f.write(yaml.dump(config))
    else:
        print "aborted due to `%s` existence." % defs.config_name


# export database document
def export():
    
    from config import config
    options = config(defs.config_name)
    
    if not options:
        print "failed due to missing `%s`." % defs.config_name
    
    project = "%s_%s" % (options.docname, options.version) if options.version else options.docname
    static = Directory(defs.static)
    
    # create database documentation page
    doc = IndexTemplate()
    doc.render(docname=options.docname, author=options.author, version=options.version)
    doc.save()
    
    # create `create statements` page
    stmts = SQLTemplate()
    stmts.render()
    stmts.save()
    
    # packaging the document
    documentor = Documentor(project)
    documentor.add(static, 'static')
    documentor.add(doc, 'index.html')
    documentor.add(stmts, 'sql.txt')
    
    # exporting the document
    if not documentor.exists():
        documentor.deploy()
        print "database document created!"
    else:
        sys.exit("Failed to create documentation. File exists error")
