import requests
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings()
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import fromstring, ElementTree

def get_stats_dump(firewall_ip, api_key):
    values = {'type': 'export', 'category': 'stats-dump', 'key': api_key}
    call = 'https://%s/api/' % (firewall_ip)

    response = requests.post(call, data=values, verify=False)

    xmltree = ElementTree(fromstring(response.text))

    root = xmltree.getroot()

    if root.attrib["status"] == "success":
        print("Stats Dump Generated")

    else:
        print("Stats dump failed")
        sys.exit()

    jobid = xmltree.findtext('./result/job')

    return jobid