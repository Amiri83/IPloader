import sqlite3
import json
import logging
from iploader.readConfig import Reader

reader = Reader()


class DB:
    logging.basicConfig(filename=reader.log_destination,
                        filemode='a', format='%(asctime)s- %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
                        level=logging.INFO)
    
    def __init__(self):
        
        try:
            with sqlite3.connect(reader.dbpath) as conn:
                command = 'create table if not exists ip_addresses ( id INTEGER PRIMARY KEY , ' \
                          'ip STRING NOT NULL,' \
                          'date_added STRING NOT NULL)'
                command2 = 'create table if not exists abused_address (  ' \
                           'ip STRING NOT NULL,' \
                           'countryCode STRING ,' \
                           'isp STRING ,' \
                           'domain STRING ,' \
                           'totalReports STRING ,' \
                           'lastReportedAt STRING )'
                
                conn.execute(command)
                conn.execute(command2)
        except BaseException as exp:
            logging.error(f"{exp}")
            logging.error(f"{type(exp)}")
    
    @staticmethod
    def insert_data(ips):
        ips = json.loads(ips)
        with sqlite3.connect(reader.dbpath) as conn:
            command = "INSERT INTO ip_addresses VALUES(?,?,?) "
            for ip in ips:
                conn.execute(command, tuple(ip.values()))
            conn.commit()
        logging.info("New IPs inserted to DB...")
        print("New IPs inserted to DB...")
    @staticmethod
    def insert_abused(ips):
        ips = json.loads(ips)
        with sqlite3.connect(reader.dbpath) as conn:
            command = "INSERT INTO abused_address VALUES(?,?,?,?,?,?) "
            for ip in ips:
                conn.execute(command, tuple(ip.values()))
            conn.commit()
        logging.info("New IPs inserted to Abused Table...")
        print("New IPs inserted to Abused Table...")

    @staticmethod
    def insert_expired_data(ips):
        ips = json.loads(ips)
        with sqlite3.connect(reader.dbpath) as conn:
            command = "INSERT INTO expired_addresses VALUES(?,?,?) "
            for ip in ips:
                conn.execute(command, tuple(ip.values()))
            conn.commit()
    
    @staticmethod
    def get_ips():
        ip_list = []
        with sqlite3.connect(reader.dbpath) as conn:
            logging.info("Reading db to get existing ips")
            command = "SELECT * FROM ip_addresses"
            cursor = conn.execute(command)
            for row in cursor:
                ip_list.append(row[1])
            
            return ip_list
    
    @staticmethod
    def get_data():
        # ip_list = []
        with sqlite3.connect(reader.dbpath) as conn:
            # logging.info("reading existing database info to get full IP Lists using SELECT * FROM ip_addresses ")
            command = "SELECT * FROM ip_addresses"
            cursor = conn.execute(command)
            rows = cursor.fetchall()
            return rows
    
    @staticmethod
    def get_id():
        try:
            with sqlite3.connect(reader.dbpath) as conn:
                command = "SELECT id from ip_addresses ORDER by id DESC"
                cursor = conn.execute(command)
                rows = cursor.fetchone()
                if rows is None:
                    logging.info("Got row numbers from DB = 0 rows")
                    print("Got row numbers from DB = 0 rows")
                    return 0
                else:
                    index = list(rows).pop()
                    logging.info(f"Got row numbers from DB = {index} rows")
                    print(f"Got row numbers from DB = {index} rows")
                    return index
        except BaseException as exp:
            logging.error(f"{exp}")
            logging.error(f"{type(exp)}")
