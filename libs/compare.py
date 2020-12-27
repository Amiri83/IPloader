from libs.file import Check
from libs.database import DB

file_check = Check("/tmp/ip_list.txt")
db = DB()
print(file_check.isExist())

print(db.read_data())