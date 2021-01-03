import requests
import json
from iploader.readConfig import Reader

reader = Reader()
KEY = reader.token


class Abuse:
    
    @staticmethod
    def send_req(ip):
        print(f"Checking {ip.strip()} against Abuse DB")
        url = 'https://api.abuseipdb.com/api/v2/check'
        querystring = {
            'ipAddress': ip
        }
        headers = {
            'Accept': 'application/json',
            'Key': KEY
        }
        response = requests.request(method='GET', url=url, headers=headers, params=querystring)
        if response.headers['X-RateLimit-Remaining'] == 0 or response.status_code == 429:
            print("Rate Limiting reached. Got 429 error!")
            exit()
        response = json.loads(response.text)
        try:
            if response['errors'] is not None:
                return None
        except BaseException as exp:
            print(exp)
        if response['data']['isWhitelisted'] is False \
                and response['data']['abuseConfidenceScore'] == 100 \
                and response['data']['totalReports'] > 0:
            
            result = dict({"ip": ip, "countryCode": response['data']['countryCode'], "isp": response['data']['isp'],
                           "domain": response['data']['domain'],
                           "totalReports": str(response['data']['totalReports']),
                           "lastReportedAt": response['data']['lastReportedAt']})
            print(f"{ip.strip()} -> Abused")
            
            return result
        
        else:
            print(f"{ip.strip()} -> OK")
            return None

# abuse = Abuse()
# print (abuse.send_req("1.1.1.1"))
