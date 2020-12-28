import configparser

config = configparser.ConfigParser()
config.read('config.ini')


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
