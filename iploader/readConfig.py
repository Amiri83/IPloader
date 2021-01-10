import configparser
from pathlib import Path

path = Path('/opt/config.ini')
if path.exists() is False:
    print("Config File \"/opt/config.ini\" does not exist.\nAborting program ...")
    exit(1)

config = configparser.ConfigParser()
config.read('/opt/config.ini')


class Reader:

    def __init__(self):
        self.__token = config['conf']['Token']
        self.__infile = config['conf']['Infile']
        self.__outfile = config['conf']['Outfile']
        self.__dbpath = config['conf']['DBPath']
        self.__expiration_days = config['conf']['ExpirationDays']
        self.__log_destination = config['conf']['LogDest']


    @property
    def infile(self):
        return self.__infile

    @property
    def outfile(self):
        return self.__outfile
    
    @property
    def dbpath(self):
        return self.__dbpath

    @property
    def expiration_days(self):
        return self.__expiration_days

    @property
    def log_destination(self):
        return self.__log_destination

    @property
    def token(self):
        return self.__token

