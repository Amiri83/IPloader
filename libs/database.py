from libs.dbconnect import DBconnect
import sqlite3
import json
import libs.readConfig
import logging

configs = libs.readConfig.Reader()
logging.basicConfig(filename=configs.log_destination,
                    filemode='a', format='%(asctime)s- %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.INFO)


class DB:
    db = DBconnect()

    @staticmethod
    def insert_data(ips):
        ips = json.loads(ips)
        with sqlite3.connect(configs.dbpath) as conn:
            command = "INSERT INTO ip_addresses VALUES(?,?,?) "
            for ip in ips:
                conn.execute(command, tuple(ip.values()))
            conn.commit()
        logging.info("New IPs inserted to DB...")

    @staticmethod
    def insert_abused(ips):
        ips = json.loads(ips)
        with sqlite3.connect(configs.dbpath) as conn:
            command = "INSERT INTO abused_address VALUES(?,?,?,?,?,?) "
            for ip in ips:
                conn.execute(command, tuple(ip.values()))
            conn.commit()
        logging.info("New IPs inserted to Abused Table...")


    @staticmethod
    def insert_expired_data(ips):
        ips = json.loads(ips)
        with sqlite3.connect(configs.dbpath) as conn:
            command = "INSERT INTO expired_addresses VALUES(?,?,?) "
            for ip in ips:
                conn.execute(command, tuple(ip.values()))
            conn.commit()

    @staticmethod
    def get_ips() :
        ip_list = []
        with sqlite3.connect(configs.dbpath) as conn:
            logging.info("Reading db to get existing ips")
            command = "SELECT * FROM ip_addresses"
            cursor = conn.execute(command)
            for row in cursor:
                ip_list.append(row[1])
            return ip_list

    @staticmethod
    def get_data() :
        # ip_list = []
        with sqlite3.connect(configs.dbpath) as conn:
            # logging.info("reading existing database info to get full IP Lists using SELECT * FROM ip_addresses ")
            command = "SELECT * FROM ip_addresses"
            cursor = conn.execute(command)
            rows = cursor.fetchall()
            return rows
