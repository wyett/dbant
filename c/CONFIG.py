#!/opt/env/python/bin/python

"""
anlysis all config file under ../conf/
"""


import os
import re
import ConfigParser

__author__ = 'wyett'

class CONFIG(object):
    """ parser config file """
    def __init__(self, fname="logant.conf"):
        self.dname = os.path.abspath('.')
        self.fname = os.path.join(\
             os.path.split(self.dname)[0], 'conf', fname)

    def __str__(self):
        return self.fname

    def readConfigfile(self):
        dc = {}
        cf = ConfigParser.ConfigParser()
        cf.read(self.fname)
        for o in cf.sections():
            dc[o] = cf.items(o)

        return dc

    def taskParser(self, taskline):
        tp = {}
        for item in taskline.split(','):
            tp[item.strip().split('=')[0]] = item.strip().split('=')[1]
        return tp

    def readTaskfile(self):
        tc = []
        with open(self.fname, 'rb') as f:
            for line in f.read().split('\n'):
                if re.match(r'^#', line) or len(line)==0:
                    pass
                else:
                    tc.append(line)
        return list(map(self.taskParser, tc))

#eof
