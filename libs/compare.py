from libs.file import File
from libs.database import DB
from libs.dbconnect import DBconnct
from pathlib import Path
import datetime
import json
import libs.readConfig
import logging

configs = libs.readConfig.Reader()


class Compare:
    logging.basicConfig(filename=configs.log_destination,
                        filemode='a', format='%(asctime)s- %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',level=logging.INFO)
    
    @staticmethod
    def do_compare(file_location):
        try:
            path = Path(file_location)
            if path.exists():
                file = File(file_location)
                db = DB()
                file_ips = (file.read_data())
                db_ips = db.get_ips()
                unique_ips = list(set(file_ips) - set(db_ips))
                if len(unique_ips) == 0:
                    return None
                else:
                    return file.convert(unique_ips)
            else:
                logging.error(f"{configs.infile} doesn't exist")
                return None
        except BaseException as exp:
            print(exp)
    
    @staticmethod
    def do_compare_expire(ips):
        db = DB()
        db_ip_list = []
        db_ips = db.get_data()
        for db_ip in db_ips:
            db_ip_list.append(db_ip[1])
        
        diff = list(set(db_ip_list) - set(ips))
        
        return diff
    
    @staticmethod
    def get_expried_ips():
        db = DB()
        data = db.get_data()
        today = datetime.datetime.now()
        dead_line = datetime.timedelta(days=int(configs.expiration_days))
        earlier = today - dead_line
        expired_ips = []
        for i in data:
            date_time_str = (i[2])
            date_time_obj = datetime.datetime.strptime(date_time_str, '%b %d %Y %I:%M%p')
            if earlier.date() >= date_time_obj.date():
                expired_ips.append(i[1])
        
        return expired_ips
    
    @staticmethod
    def create_expired_json(ips):
        ip_list = []
        db2 = DBconnct()
        id2 = db2.get_id2()
        for ip in ips:
            dt = datetime.date.today().strftime('%b %d %Y %I:%M%p')
            ip_dict = {"id": id2, "ip": ip, "date_added": dt}
            ip_list.append(ip_dict)
            id2 = id2 + 1
        
        return json.dumps(ip_list)
