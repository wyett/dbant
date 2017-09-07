import os
import sys
import logging
import logging.handlers


class LOG(object):
    def __init__(self, logger,logfile)
        self.logger=logger
        self.logfile=logfile

    def init_log(self, logfile):
        """
        print log
        """
        try:
            formatter = logging.Formatter("%(asctime)s - (%(process)d:%(thread)d)%(filename)s[%(funcName)s:%(lineno)d] %(levelname)-s %(message)s")
            file_handler = logging.handlers.RotatingFileHandler(log_file, mode='a', maxBytes=100*1024, backupCount=5, encoding=None, delay=0)
            file_handler.setFormatter(formatter)
            self.logger = logging.getLogger(log_file)
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

