import requests
import datetime
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings()

#Create timestamp
currenttime = '{:%d-%m-%Y-%H%M%S}'.format(datetime.datetime.now())

def download_stats(firewall_ip, api_key, jobid):
    values = {'type': 'export', 'category': 'stats-dump', 'action': 'get', 'job-id': jobid, 'key': api_key}
    call = 'https://%s/api/' % (firewall_ip)

    response = requests.post(call, data=values, verify=False)

    file = open(firewall_ip + "-" + currenttime + "-statsdump.tgz", 'wb')
    size = file.write(response.content)
    file.close()

    return size

def download_tsf(firewall_ip, api_key, jobid):
    values = {'type': 'export', 'category': 'tech-support', 'action': 'get', 'job-id': jobid, 'key': api_key}
    call = 'https://%s/api/' % (firewall_ip)

    response = requests.post(call, data=values, verify=False)

    file = open(firewall_ip + "-" + currenttime + "-tsf.tgz", 'wb')
    size = file.write(response.content)
    file.close()

    return size

