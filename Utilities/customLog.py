
import logging
import os
from logging import basicConfig

class LogGen:
    @staticmethod
    def loggen():
        path=os.path.abspath(os.curdir)+"\\log\\automation.log"
        logging.basicConfig(filename=path,level=logging.DEBUG)
        return logging

