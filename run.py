from libs.file import File
from libs.database import DB

file= File("/tmp/ip_list.txt")
db = DB()
file_ips = (file.read_data())
db_ips = db.get_ips()
uniqe_ips = list(set(file_ips) | set(db_ips))
converetd = file.convert(uniqe_ips)


    