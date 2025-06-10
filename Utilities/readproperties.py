
import configparser
import os

config= configparser.RawConfigParser()

config.read(os.path.abspath(os.curdir)+ "\\configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def ApplicationURL():
        url=config.get("commoninfo","url")
        return url

    @staticmethod
    def getUserEamil():
        username=config.get("commoninfo","email")
        return username

    @staticmethod
    def getPassword():
        password=config.get("commoninfo","password")
        return password


