import requests
import sys
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings()

def get_key(firewall_ip, firewall_admin, firewall_password):
    response = requests.get("https://" + firewall_ip + "/api?type=keygen&user=" + firewall_admin + "&password=" + firewall_password, verify=False)

    if re.search(b'success', response.content):
        print("API Key creation successful for device: " + firewall_ip)

    else:
        print("API Key creation failed")
        sys.exit()

    api_key = re.search(b"(<key>)(.+?)(</key>)", response.content).group(2).decode('UTF-8')

    return api_key
