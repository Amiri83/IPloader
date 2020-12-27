from pathlib import Path
import sqlite3
import json
from libs.read_file import ReadFile



readfile = ReadFile()
readfile.readfile()

ips = json.loads(Path("/tmp/temp_ips.json").read_text())
with sqlite3.connect("data.db") as conn:
    command = "INSERT INTO ip_addresses VALUES(?,?,?) "
    for  ip in ips :
        conn.execute(command,tuple(ip.values()))
    conn.commit()
        

