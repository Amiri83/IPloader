from libs.compare import Compare
from libs.database import DB
import libs.readConfig
import logging

try:
    configs = libs.readConfig.Reader()
    print("starting ...")
    logging.basicConfig(filename=configs.log_destination,
                        filemode='a', format='%(asctime)s- %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',level=logging.INFO)
    compare = Compare()
    db = DB()
    logging.info("========== Started ==============")
    result = compare.do_compare(configs.infile)
    if result is not None:
        logging.info("new ips will be insert to DB")
        db.insert_data(result)
    else:
        logging.info("no new Ip found")
    try:
        expired_ips = (compare.get_expried_ips())
        final_ips = compare.do_compare_expire(expired_ips)
        with open(configs.outfile, "w") as f:
            for final_ip in final_ips:
                f.write("%s\n" % final_ip)
    except BaseException as exp:
        logging.error(f"{exp}")
        
except BaseException as exp:
    print(exp)
    print(type(exp))
    
print("Done.")
logging.info("=========== Finished ============")
# if len(expired_ips) != 0 :
#     expried_json=compare.create_expired_json(expired_ips)
#     db.insert_expired_data(expried_json)
