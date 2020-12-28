from pathlib import Path
from libs.dbconnect import DBconnct
import sqlite3
import json


# from libs.file import File

class DB:
    db =DBconnct()
    @staticmethod
    def insert_data(ips):
        ips = json.loads(ips)
        with sqlite3.connect("data.db") as conn:
            command = "INSERT INTO ip_addresses VALUES(?,?,?) "
            for ip in ips:
                conn.execute(command, tuple(ip.values()))
            conn.commit()
        print("New Ips from file inserted to DB...")
    
    db =DBconnct()
    @staticmethod
    def insert_expired_data(ips):
        ips = json.loads(ips)
        with sqlite3.connect("data.db") as conn:
            command = "INSERT INTO expired_addresses VALUES(?,?,?) "
            for ip in ips:
                conn.execute(command, tuple(ip.values()))
            conn.commit()
        print("New Ips from file inserted to DB...")
        
    def get_ips(self):
        ip_list = []
        with sqlite3.connect("data.db") as conn:
            print("reading existing database info")
            command = "SELECT * FROM ip_addresses"
            cursor = conn.execute(command)
            for row in cursor:
                ip_list.append(row[1])
            return ip_list
        
    def get_data(self):
        ip_list = []
        with sqlite3.connect("data.db") as conn:
            print("reading existing database info")
            command = "SELECT * FROM ip_addresses"
            cursor = conn.execute(command)
            rows = cursor.fetchall()
            return rows
        

# db = DB()
# db.read_data()
