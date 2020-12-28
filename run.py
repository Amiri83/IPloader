from libs.compare import Compare
from libs.database import DB

compare = Compare()
db = DB()
result = compare.do_compare("/tmp/ip_list.txt")
if result is not None:
    print("new ips will be insert to DB")
    db.insert_data(result)
else:
    print("no new Ip found")


expired_ips=(compare.get_expried_ips())
final_ips = compare.do_compare_expire(expired_ips)
with open("/var/www/html/ip.txt","w") as f:
    for final_ip in final_ips:
        f.write("%s\n" % final_ip)
        
        

# if len(expired_ips) != 0 :
#     expried_json=compare.create_expired_json(expired_ips)
#     db.insert_expired_data(expried_json)
