import configparser
from pathlib import Path

path = Path('/opt/config.ini')
if path.exists() == False:
    print("Config File \"/opt/config.ini\" does not exist.\nAborting program ...")
    exit(1)

config = configparser.ConfigParser()
config.read('/opt/config.ini')

class Reader:

    @property
    def infile(self):
        return config['conf']['Infile']

    @property
    def outfile(self):
        return config['conf']['Outfile']

    @property
    def dbpath(self):
        return config['conf']['DBPath']

    @property
    def expiration_days(self):
        return config['conf']['ExpirationDays']

    @property
    def log_destination(self):
        return config['conf']['LogDest']

    @property
    def token(self):
        return config['conf']['Token']

