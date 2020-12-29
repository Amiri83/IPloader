import sqlite3
import libs.readConfig
import logging

configs = libs.readConfig.Reader()

logging.basicConfig(filename=configs.log_destination,
                    filemode='a', format='%(asctime)s- %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.INFO)


class DBconnect():
    def __init__(self):

        try:
            with sqlite3.connect(configs.dbpath) as conn:
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
    def get_id() -> int:
        try:
            with sqlite3.connect(configs.dbpath) as conn:
                command = "SELECT id from ip_addresses ORDER by id DESC"
                cursor = conn.execute(command)
                rows = cursor.fetchone()
                if rows is None:
                    logging.info("Got row numbers from DB = 0 rows")
                    return 0
                else:
                    index = list(rows).pop()
                    logging.info(f"Got row numbers from DB = {index} rows")
                    return index
        except BaseException as exp:
            logging.error(f"{exp}")
            logging.error(f"{type(exp)}")
