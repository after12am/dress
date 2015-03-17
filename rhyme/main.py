# encoding: utf-8
import os, sys, io
import defs
import yaml
from config import get_config
from optparse import OptionParser
from archives import StaticDirectory, Archive
from templates import IndexTemplate, SQLTemplate

def create_conf_file(datasource):
    
    out = None
    
    if datasource.lower() == 'mysql':
        out = dict(
            version = '',
            author = '',
            docname = '',
            database = dict(
                datasource = 'Database/MySQL',
                user = 'user',
                password = 'password',
                database = 'database',
                host = '127.0.0.1',
                port = 3306,
                charset = 'utf8'
            )
        )
    
    if datasource.lower() == 'postgres':
        out = dict(
            version = '',
            author = '',
            docname = '',
            database = dict(
                datasource = 'Database/PostgreSQL',
                user = 'user',
                password = 'password',
                database = 'database',
                host = '127.0.0.1',
                port = 5432,
                charset = 'utf8'
            )
        )
    
    if datasource.lower() == 'sqlite3':
        out = dict(
            version = '',
            author = '',
            docname = '',
            database = dict(
                datasource = 'Database/SQLite3',
                timeout = 5000
            )
        )
    
    if out is not None:
        with io.open(defs.config_name, 'w') as f:
            f.write(unicode(yaml.dump(out, default_flow_style = False), 'utf-8'))
        return 1
    return 0


def export_database_document():
    
    options = get_config(defs.config_name)
    docname = "%s_%s" % (options.docname, options.version) if options.version else options.docname
    dirname = os.path.abspath(os.path.dirname(__file__))
    
    # static files
    files = StaticDirectory('static', os.path.join(dirname, '_static'))
    
    # create top page
    index = IndexTemplate('index.html')
    index.render(docname=options.docname, author=options.author, version=options.version)
    
    # creating create statements file
    statements = SQLTemplate('sql.txt')
    statements.render()
    
    # exporting database document
    archive = Archive(index, files, statements)
    if not archive.exists(docname):
        archive.save(docname)
        return 1
    return 0


def main(argv=sys.argv[1:]):
    
    parser = OptionParser(
        usage="%prog [config|export] [options]",
        add_help_option=False
    )
    
    parser.add_option(
        "--help", "--usage", 
        action='help'
    )
    
    if not argv:
        parser.error('A command is required.')
    
    # creating configuration file
    if argv[0] == 'config':
        
        parser.add_option(
            "-d", "--datasource", 
            dest="datasource",
            help="Supported database. MySQL, SQLite3, PostgreSQL are supported.",
            type="string",
            default=None
        )
        
        (options, args) = parser.parse_args()
        
        if os.path.exists(defs.config_name):
            sys.exit("Aborted due to \"%s\" existence." % defs.config_name)
        
        if not options.datasource.lower() in defs.valid_datasources:
            sys.exit("Aborted due to invalid datasource.")
        
        if create_conf_file(options.datasource):
            sys.stdout.write("Success to create \".rhyme.yml\" file!\n")
        else:
            sys.stdout.error("Failed to create \".rhyme.yml\" file :(\n")
    
    
    # exporting database document
    if argv[0] == 'export':
        
        if not os.path.exists(defs.config_name):
            sys.exit("Aborted due to \"%s\" missing." % defs.config_name)
        
        if export_database_document():
            sys.stdout.write("database document created!\n")
        else:
            sys.stdout.error("Failed to create documentation. File exists error\n")


if __name__ == '__main__': main()

