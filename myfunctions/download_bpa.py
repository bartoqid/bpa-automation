import requests
import datetime
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings()

#Create timestamp
currenttime = '{:%d-%m-%Y-%H%M%S}'.format(datetime.datetime.now())

def download_bpa(task_id, token, firewall_ip):
    auth = {'Authorization': 'Token %s' % token}
    call = 'https://bpa.paloaltonetworks.com/api/v1/results/' + task_id + '/download/'

    response = requests.get(call, headers=auth, verify=False)

    file = open(firewall_ip + "-" + currenttime + "-bpa.zip", 'wb')
    size = file.write(response.content)
    file.close()

    return size