from myfunctions.get_stats_dump import get_stats_dump
from myfunctions.get_status import get_status_stats
from myfunctions.download_stats import download_stats
from myfunctions.get_api_key import get_key
import time

def generate_dump(firewall_ip, firewall_admin, firewall_password):

    firewall_ip = firewall_ip.rstrip('\n')

    api_key = get_key(firewall_ip, firewall_admin, firewall_password)
    job_id = get_stats_dump(firewall_ip, api_key)
    status_progress = (get_status_stats(firewall_ip, api_key, job_id))

    while status_progress[0] != "FIN":
        time.sleep(5)
        print("Waiting for device: " + firewall_ip + " stats dump to be generated")
        print("Job ID: " + job_id + " Status: " + status_progress[0] + " Progress : " + status_progress[1] + "%\n")
        status_progress = (get_status_stats(firewall_ip, api_key, job_id))
    else:
        size = download_stats(firewall_ip, api_key, job_id)
        print("Successfully transferred " + str(size) + " Bytes\n")