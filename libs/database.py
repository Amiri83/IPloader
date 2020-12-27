from pathlib import Path
import sqlite3
import json
#from libs.file import File

class DB:

    def insert_data(self):
        ips = json.loads(Path("/tmp/temp_ips.json").read_text())
        with sqlite3.connect("data.db") as conn:
            command = "INSERT INTO ip_addresses VALUES(?,?,?) "
            for ip in ips:
                conn.execute(command, tuple(ip.values()))
            conn.commit()
        print("New Ips from file inserted to DB...")

    def get_ips(self):
        with sqlite3.connect("data.db") as conn:
            print("reading existing database info")
            command = "SELECT ip FROM ip_addresses"
            curser = conn.execute(command)
            rows = curser.fetchall()
            if len(rows) == 0:
                print("No data found in DB")
            return rows

#db = DB()
#db.read_data()




