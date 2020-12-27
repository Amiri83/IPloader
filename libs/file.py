import json
from libs.dbconnect import DBconnct
from datetime import  datetime
from pathlib import Path


class File():
    ip_list = []

    def __init__(self,file_location):
        self.file_location = file_location

    def read_data(self):
        path = Path(self.file_location)
        counter = 0
        if (path.exists()):
            print(f"Found new file! in {self.file_location} , reading ...")
            try:
                with open(self.file_location) as ips:
                 for ip in ips:
                     self.ip_list.append(ip.strip())
                     counter = counter + 1
            except BaseException as exp:
                print(exp)
                print(type(exp))

            #data = json.dumps(ip_list)
            #Path("/tmp/temp_ips.json").write_text(data)
            print (f"Found  {counter} ips")
            return self.ip_list
        else:
            print(f"file {self.file_location} does not exist ." )
            return None

    @staticmethod
    def convert(ips):
        db = DBconnct()
        ip_list =[]
        id = db.get_id()
        counter =0
        dt = datetime.today().strftime('%Y-%m-%d')
        try:
            for ip in ips:
             ip_dict = {"id": id, "ip": ip, "date_added": dt}
             ip_list.append(ip_dict)
             counter = counter + 1
        except BaseException as exp:
            print(exp)
            print(type(exp))

        return json.dumps(ip_list)