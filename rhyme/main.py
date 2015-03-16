# encoding: utf-8
import os, sys
import commands

def rhyme_main(argv=sys.argv[1:]):
    if len(argv) == 0:
        return
    if argv[0] == 'config':
        commands.config()
        return
    if argv[0] == 'export':
        commands.export()
        return

if __name__ == '__main__': rhyme_main()