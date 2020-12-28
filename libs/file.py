import json
from libs.dbconnect import DBconnect
from datetime import datetime
from pathlib import Path
import libs.readConfig
import logging

configs = libs.readConfig.Reader()


class File:
    ip_list = []
    
    logging.basicConfig(filename=configs.log_destination,
                        filemode='a', format='%(asctime)s- %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
                        level=logging.INFO)
    
    def __init__(self, file_location):
        self.file_location = file_location
    
    def read_data(self):
        path = Path(self.file_location)
        counter = 0
        if path.exists():
            logging.info(f"Found file in {self.file_location} , reading ...")
            try:
                with open(self.file_location) as ips:
                    for ip in ips:
                        self.ip_list.append(ip.strip())
                        counter = counter + 1
            except BaseException as exp:
                logging.error(f"{exp}")
                logging.error(f"{type(exp)}")
            
            logging.info(f"Found  {counter} ips")
            return self.ip_list
        else:
            logging.error(f"file {self.file_location} does not exist .")
            return None
    
    @staticmethod
    def convert(ips):
        db = DBconnect()
        ip_list = []
        id_db = db.get_id()
        dt = datetime.today().strftime('%b %d %Y %I:%M%p')
        try:
            for ip in ips:
                id_db = id_db + 1
                ip_dict = {"id": id_db, "ip": ip.strip(), "date_added": dt}
                ip_list.append(ip_dict)
        except BaseException as exp:
            logging.error(f"{exp}")
            logging.error(f"{type(exp)}")
        
        return json.dumps(ip_list)
