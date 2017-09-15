#!/opt/env/python/bin/python

"""
    class of log
"""

import os
import sys
import logging
import logging.handlers

__author__ = 'wyett'

class LOG(object):
    def __init__(self, loggerdir, logfile="dbant.log")
        self.loggerdir = os.path.abspath('.')
        self.logfile = os.path.join(\
                       os.path.split(self.loggerdir)[0]\
                       + 'log' + logfile)

    def init_log(self):
        """
        print log
        """
        try:
            formatter = logging.Formatter("%(asctime)s - (%(process)d:%(thread)d)%(filename)s[%(funcName)s:%(lineno)d] %(levelname)-s %(message)s")
            file_handler = logging.handlers.RotatingFileHandler(self.logfile, mode='a', maxBytes=100*1024, backupCount=5, encoding=None, delay=0)
            file_handler.setFormatter(formatter)
            self.logger = logging.getLogger(self.logfile)
            self.logger.addHandler(file_handler)
            self.logger.addHandler(file_handler)
            self.logger.setLevel(logging.INFO)
            self.console = logging.StreamHandler()
            console.setFormatter(formatter)
            self.logger.addHandler(console)

            return logger
        except Exception, e:
            logging.error("initiate log failed: {0:s}".format(str(e)))
            sys.exit(PROGRAM_EXECUTE_ERROR)

