# encoding: utf-8
import os, sys, doc
from optparse import OptionParser

def dbdoc_main(argv=sys.argv[1:]):
    
    parser = OptionParser(
        usage="%prog [options]",
        version="%prog pre-alpha",
        add_help_option=False
    )
    
    parser.add_option(
        "--datasource", 
        dest="datasource",
        help="Supported datasource. valid options are mysql, sqlite, postgres",
        type="string",
        default=None
    )
    
    parser.add_option(
        "-u", "--user", 
        dest="user",
        help="MySQL user name that is used to connect the server",
        type="string",
        default='root'
    )
    
    parser.add_option(
        "-p",
        dest="password",
        action="store_true"
    )
    
    parser.add_option(
        "--password", 
        dest="password",
        help="MySQL password that is used to connect the server",
        type="string",
        default=''
    )
    
    parser.add_option(
        "-P", "--port", 
        dest="port",
        help="MySQL port number to use for TCP/IP connection",
        type="int",
        default='3306'
    )
    
    parser.add_option(
        "-h", "--host", 
        dest="host",
        help="MySQL server host",
        type="string",
        default='127.0.0.1'
    )
    
    parser.add_option(
        "-D", "--database", 
        dest="database",
        help="Database should be used",
        type="string",
        default=None
    )
    
    parser.add_option(
        "--default-character-set", 
        dest="charset",
        help="character set used as default",
        type="string",
        default="utf8"
    )
    
    parser.add_option(
        "--author", 
        dest="author",
        help="author",
        type="string",
        default="All rights reserved"
    )
    
    parser.add_option(
        "-v", # "--version",
        dest="version",
        help="version",
        type="string",
        default=None
    )
    
    parser.add_option(
        "--help", "--usage", 
        action='help'
    )
    
    (options, args) = parser.parse_args()
    if options.password is True:
        options.password = raw_input('password:')
    
    doc.export(options=options, args=args)

if __name__ == '__main__': dbdoc_main()