import requests
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings()
from xml.etree.ElementTree import fromstring, ElementTree

def get_time(firewall_ip, api_key):
    values = {'type': 'op', 'cmd': '<show><clock></clock></show>', 'key': api_key}
    call = 'https://%s/api/' % (firewall_ip)

    response = requests.post(call, data=values, verify=False)

    xmltree = ElementTree(fromstring(response.text))

    root = xmltree.getroot()

    if root.attrib["status"] == "success":
        print("Get time successful")
        return response
    else:
        print("Get time failed")
        sys.exit()