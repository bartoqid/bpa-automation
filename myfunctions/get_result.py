import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings()

def get_result(task_id, token):
    auth = {'Authorization': 'Token %s' % token}
    call = 'https://bpa.paloaltonetworks.com/api/v1/results/' + task_id
    print(call)
    response = requests.get(call, headers=auth, verify=False)

    return response