# encoding: utf-8

# convert dictionary to object
class dict2obj(object):
    def __init__(self, dictionary):
        self.__dict__ = dictionary