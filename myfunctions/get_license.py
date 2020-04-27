import requests
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings()
from xml.etree.ElementTree import fromstring, ElementTree

def get_license(firewall_ip, api_key):
    values = {'type': 'op', 'cmd': '<request><license><info></info></license></request>', 'key': api_key}
    call = 'https://%s/api/' % (firewall_ip)

    response = requests.post(call, data=values, verify=False)

    xmltree = ElementTree(fromstring(response.text))

    root = xmltree.getroot()

    if root.attrib["status"] == "success":
        print("Get license successful")
        return response
    else:
        print("Get license failed")
        sys.exit()