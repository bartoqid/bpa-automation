import requests
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings()
from xml.etree.ElementTree import fromstring, ElementTree

def get_tsf(firewall_ip, api_key):
    values = {'type': 'export', 'category': 'tech-support', 'key': api_key}
    call = 'https://%s/api/' % (firewall_ip)

    response = requests.post(call, data=values, verify=False)

    xmltree = ElementTree(fromstring(response.text))

    root = xmltree.getroot()

    if root.attrib["status"] == "success":
        print("TSF Generated")

    else:
        print("TSF failed")
        sys.exit()

    jobid = xmltree.findtext('./result/job')

    return jobid