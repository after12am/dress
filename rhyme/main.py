# encoding: utf-8
import os, sys
import command

def rhyme_main(argv=sys.argv[1:]):
    if len(argv) == 0:
        return
    if argv[0] == 'config':
        command.config()
        return
    if argv[0] == 'export':
        command.export()
        return

if __name__ == '__main__': rhyme_main()