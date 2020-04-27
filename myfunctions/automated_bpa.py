from myfunctions.get_api_key import get_key
from myfunctions.get_running_config import get_running_config
from myfunctions.get_system_info import get_system_info
from myfunctions.get_license import get_license
from myfunctions.get_time import get_time
from myfunctions.submit_bpa import submit_bpa
from myfunctions.download_bpa import download_bpa
from hurry.filesize import size

def automated_bpa(firewall_ip, firewall_admin, firewall_password, token):
    firewall_ip = firewall_ip.rstrip('\n')

    api_key = get_key(firewall_ip, firewall_admin, firewall_password)

    xmlfw = (get_running_config(firewall_ip, api_key)).content

    systemfw = (get_system_info(firewall_ip, api_key)).content
    licensefw = (get_license(firewall_ip, api_key)).content
    timefw = (get_time(firewall_ip, api_key)).content

    task_id = submit_bpa(xmlfw, systemfw, licensefw, timefw, token)

    d_size = download_bpa(task_id, token, firewall_ip)

    print("Download BPA report with the size of:", size(d_size), "Bytes")