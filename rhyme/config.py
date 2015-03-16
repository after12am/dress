# encoding: utf-8
import os
import yaml
from misc import dict2obj

def config(filename):
    if os.path.exists(filename):
        if os.path.isfile(filename):
            with open(filename, 'r') as f:
                return dict2obj(yaml.load(f))
    return False

