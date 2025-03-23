## 🛡️ Problem Overview

At our network edge, we used a **Fortigate firewall** to block malicious IPs reported daily—often 60–70 addresses, suspected of hacking attempts. We faced several challenges:

1. **Hosting the Blocklist**  
Fortigate required the Bad-IP list to be hosted on a web server (e.g., Nginx) to import and apply it.

2. **IP Reputation Uncertainty**  
Not all IPs were confirmed threats. We needed to **verify them against AbuseIPDB** before blacklisting.

3. **No Auto-Expiration**  
Fortigate lacked **time-based blocking**—once blocked, IPs remained indefinitely unless manually removed.

## 🧩 Solution: IPloader

**IPloader** automates the process of validating, managing, and serving threat IP lists for Fortigate firewalls. It solves the challenges by:

- Validating IPs against **AbuseIPDB** to confirm threat reputation.
- Storing IPs in a **SQLite database** to prevent duplicates and manage expiration.
- Automatically **removing expired IPs** after a defined time.
- Serving the verified IP list via **Nginx** for Fortigate to import and block.
- Running as a **systemd timer** to update the list daily, with no manual effort.

![IPloader Workflow](docs/iploader_shadow.png)

# AbuseIPDB IPLoader

Abuse DB IP loader is a tool to check a list of given IP aginest abuseipDB (https://www.abuseipdb.com/) to determine which one is 100% attacker ips 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install iploader.

```bash
pip3 install iploader
```

## Usage
after installation create a config.ini file in /opt/ like follow:
```bash
[DEFAULT]
Description = IPFloader
Version =1.0

[conf]
Infile = /tmp/ip_list.txt
DBPath = /opt/data.db
Outfile = /var/www/html/ip.txt
ExpirationDays = 60
LogDest = /var/log/ip_loader.log
Token = <YOUR ABUSEDB TOKEN>
```
Inflie:
csv list of IPS that you want to check against abuseipDB , should look like this :

```bash
1.1.1.1
2.2.2.2
3.4.5.2
....
```
outfile:
where to put the file 

LogDest:
All events will be dispplayed on console and logged into this log file for future refrence 

ExpirationDays:
put it 0 if you dont need ips to be expired and be remoevd form exported file:

DBpath: 
a location for sqllite3 DB

## How does it works ?
it uses a sqllite db to store ips which is read from file , DB is used for 2 reason 
1- Prevent from importing dupicate IPS from file 
2- Expire IPS after spsfice days .
second function is use if you want blacklist Abused ip for specific days not always , when IP is read from file it will insert into db with date and time 
each time you run program it checks expiration in config.ini date with insertion date in DB if date is passed will remove IP form outfile 
if you want to use expriation date you need to put program in crontab to run at-least once a day

## Adding as a system service 
firts set service 
```sh
root@MON-IPREP:/lib/systemd/system# vim iploader.service 
[Unit]
Description=iploader

[Service]
Type=simple
ExecStart=/usr/local/bin/iploader

[Timer]
OnCalendar=daily
Persistent=true

[Install]
WantedBy=timers.target
```
then set timer
root@MON-IPREP:/lib/systemd/system# vim iploader.timer   
```sh
[Unit]
Description=daily run for iploader

[Timer]
OnCalendar=daily
RandomizedDelaySec=12h
Persistent=true

[Install]
WantedBy=timers.target
```
reload the daemon 
```sh
systemctl daemon-reload
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/MIT/)
