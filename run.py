from libs.compare import Compare
from libs.database import DB
import time
import libs.readConfig
from libs.AbuseCheck import Abuse
import logging
import json

try:
    configs = libs.readConfig.Reader()
    print("starting ...")
    logging.basicConfig(filename=configs.log_destination,
                        filemode='a', format='%(asctime)s- %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
                        level=logging.INFO)
    compare = Compare()
    db = DB()
    abuse = Abuse()
    logging.info("========== Started ==============")
    result = compare.do_compare(configs.infile)
    abuse_list = []
    if result is not None:
        logging.info("Checking new IPS against Abuse DB")
        for ips in result:
            abuse_result = abuse.send_req(str(ips["ip"]))
            time.sleep(1)
            if abuse_result is not None:
                logging.info(f"{abuse_result['ip']} -> Keep")
                abuse_list.append(abuse_result)
            else:
                logging.info(f"{ips['ip']} -> Remove")
                result.remove(ips)
        db.insert_data(json.dumps(result))

    else:
        logging.info("No new IP found")
    try:
        expired_ips = (compare.get_expired_ips())
        final_ips = compare.do_compare_expire(expired_ips)
        with open(configs.outfile, "w") as f:
            for final_ip in final_ips:
                f.write("%s\n" % final_ip)
    except BaseException as exp:
        logging.error(f"{exp}")

except BaseException as exp:
    print(exp)
    print(type(exp))


db.insert_abused(json.dumps(abuse_list))
print("Done.")
logging.info("=========== Finished ============")
