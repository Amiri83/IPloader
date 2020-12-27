import sqlite3


class DBconnct:
    def __init__(self):
        
        try:
            with sqlite3.connect("data.db") as conn:
                command = 'create table if not exists ip_addresses ( id INTEGER PRIMARY KEY , ' \
                          'ip STRING NOT NULL,' \
                          'date_added STRING NOT NULL)'
                conn.execute(command)
        except BaseException as exp:
            print(exp)
            print(type(exp))
    
    def get_id(self):
        try:
            with sqlite3.connect("data.db") as conn:
                command = "SELECT id from ip_addresses ORDER by id DESC"
                cursor = conn.execute(command)
                rows = cursor.fetchone()
                if rows == None:
                    return 0
                else:
                    return rows
        except BaseException as exp:
            print(exp)
            print(type(exp))


