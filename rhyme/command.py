import os, sys, documentor
import yaml
from optparse import OptionParser

config_file_name = '.rhyme.yml'

def config():
    """
        create configuration file
    """
    parser = OptionParser(
        usage="%prog [options]",
        version="%prog pre-alpha",
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
        author = [''],
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
            author = [''],
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
            docname = 'sample',
            author = [''],
            datasource = 'Database/SQLite3'
        )
    
    with open(config_file_name, 'w') as f:
        f.write(yaml.dump(config))


def export():
    
    class dict2obj(object):
        def __init__(self, dictionary):
            self.__dict__ = dictionary
    
    """
        export database document
    """
    if os.path.exists(config_file_name):
        if os.path.isfile(config_file_name):
            with open(config_file_name, 'r') as f:
                documentor.publish(dict2obj(yaml.load(f)))


if __name__ == '__main__': export()