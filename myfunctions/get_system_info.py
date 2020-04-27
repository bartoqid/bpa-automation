import requests
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings()
from xml.etree.ElementTree import fromstring, ElementTree

def get_system_info(firewall_ip, api_key):
    values = {'type': 'op', 'cmd': '<show><system><info></info></system></show>', 'key': api_key}
    call = 'https://%s/api/' % (firewall_ip)

    response = requests.post(call, data=values, verify=False)

    xmltree = ElementTree(fromstring(response.text))

    root = xmltree.getroot()

    if root.attrib["status"] == "success":
        print("Get system info successful")
        return response

    else:
        print("Get system info failed")
        sys.exit()