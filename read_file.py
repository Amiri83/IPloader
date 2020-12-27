import json
from pathlib import Path
from DB import dbconnect



if __name__ == "__main__":
     db = dbconnect.DBconnct
     db.get_id(1)