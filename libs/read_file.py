import json
from libs.dbconnect import DBconnct
from datetime import  datetime
from pathlib import Path

file_location="/tmp/ip_list.txt"
db = DBconnct()
ip_list = []
dt = datetime.today().strftime('%Y-%m-%d')

class ReadFile:
   
    def readfile(self):
        path = Path(file_location)
        if (path.exists()):
            id = db.get_id()
            try:
                with open(file_location) as ips:
                 for ip in ips:
                     id = id + 1
                     ip_dict ={"id":id,"ip":ip.strip() , "date_added":dt }
                     ip_list.append(ip_dict)
                     
            except BaseException as exp:
                print(exp)
                print(type(exp))
                
            #print(ip_list)
            data = json.dumps(ip_list)
            Path("../temp_ips.json").write_text(data)
        else:
            print(f"file {file_location} does not exist " )
            exit(0)
            
