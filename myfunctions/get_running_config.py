import requests
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings()
from xml.etree.ElementTree import fromstring, ElementTree

def get_running_config(firewall_ip, api_key):
    values = {'type': 'config', 'action': 'show', 'key': api_key}
    call = 'https://%s/api/' % (firewall_ip)

    response = requests.post(call, data=values, verify=False)

    xmltree = ElementTree(fromstring(response.text))

    root = xmltree.getroot()

    if root.attrib["status"] == "success":
        print("Get device running config successful")
        return response
    else:
        print("Get device running config failed")
        sys.exit()