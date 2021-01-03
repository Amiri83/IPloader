from iploader.file import File
from iploader.database import DB
from pathlib import Path
import datetime
import logging
from iploader.readConfig import Reader

reader = Reader()


class Compare:
    logging.basicConfig(filename=reader.log_destination,
                        filemode='a', format='%(asctime)s- %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
                        level=logging.INFO)
    
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
                logging.error(f"{reader.infile} doesn't exist")
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
    def get_expired_ips():
        db = DB()
        data = db.get_data()
        today = datetime.datetime.now()
        dead_line = datetime.timedelta(days=int(reader.expiration_days))
        earlier = today - dead_line
        expired_ips = []
        for i in data:
            date_time_str = (i[2])
            date_time_obj = datetime.datetime.strptime(date_time_str, '%b %d %Y %I:%M%p')
            if earlier.date() >= date_time_obj.date():
                expired_ips.append(i[1])
        return expired_ips
