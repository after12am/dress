# encoding: utf-8
import os, sys, io
import shutil
import tempfile
import datetime
import defs

class StaticDirectory(object):
    
    def __init__(self, name, dirpath):
        self.name = name
        self.path = dirpath


class File(object):
    
    def __init__(self, name):
        self.name = name
        f, self.path = tempfile.mkstemp()
        os.close(f)
    
    # delete the tempfile
    def delete(self):
        if os.path.exists(self.path):
            os.remove(self.path)
    
    # input data has to be unicode
    def render(self, data):
        if data is not None:
            with open(self.path, 'w') as f:
                f.write(data.encode('utf-8'))


class Archive(object):
    
    def __init__(self, *kwds):
        self.list = list(kwds)
        self.path = tempfile.mkdtemp()
    
    def __copy(self, file_or_dir):
        output = os.path.join(self.path, file_or_dir.name)
        copy = shutil.copytree if os.path.isdir(file_or_dir.path) else shutil.copyfile
        copy(file_or_dir.path, output)
    
    def save(self, archive_name):
        if not self.list:
            raise ValueError("nothing for archive")
        for item in self.list:
            self.__copy(item)
        shutil.move(self.path, './')
        os.rename(os.path.basename(self.path), archive_name)
    
    # whether docs exist or not
    def exists(self, archive_name):
        dirname = os.path.abspath(os.path.dirname(__file__))
        return os.path.exists(os.path.join(dirname, archive_name))

