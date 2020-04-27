import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings()
from xml.etree.ElementTree import fromstring, ElementTree

def get_status_stats(firewall_ip, api_key, jobid):
    values = {'type': 'export', 'category': 'stats-dump', 'action': 'status', 'job-id': jobid,  'key': api_key}
    call = 'https://%s/api/' % (firewall_ip)

    response = requests.post(call, data=values, verify=False)

    xmltree = ElementTree(fromstring(response.text))

    status = xmltree.findtext('./result/job/status')

    progress = xmltree.findtext('./result/job/progress')

    return status, progress

def get_status_tsf(firewall_ip, api_key, jobid):
    values = {'type': 'export', 'category': 'tech-support', 'action': 'status', 'job-id': jobid,  'key': api_key}
    call = 'https://%s/api/' % (firewall_ip)

    response = requests.post(call, data=values, verify=False)

    xmltree = ElementTree(fromstring(response.text))

    status = xmltree.findtext('./result/job/status')

    progress = xmltree.findtext('./result/job/progress')

    return status, progress