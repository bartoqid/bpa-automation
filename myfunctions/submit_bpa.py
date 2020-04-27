import requests
import json
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings()

def get_result(task_id, token):
    auth = {'Authorization': 'Token %s' % token}
    call = 'https://bpa.paloaltonetworks.com/api/v1/results/' + task_id
    print("Sending request to: ", call)
    response = requests.get(call, headers=auth, verify=False)
    return response


def submit_bpa(xml, info, license, gettime, token):
    values = {'xml': xml, 'system_info': info,  'license_info': license, 'system_time': gettime, 'generate_zip_bundle': 'true'}
    auth = {'Authorization': 'Token %s' % token}
    call = 'https://bpa.paloaltonetworks.com/api/v1/create/'
    response = requests.post(call, headers=auth, data=values, verify=False)

    task_name = json.loads((response.content).decode("ascii"))

    result = get_result((task_name["task_id"]), token)

    status = json.loads((result.content).decode("ascii"))

    while "processing" in status.values():
        print("processing BPA, status: ", status.get("status"))
        result = get_result((task_name["task_id"]), token)
        status = json.loads((result.content).decode("ascii"))
        time.sleep(5)

    else:
        return (task_name["task_id"])

