# Todo
#   - Handle exception when login fail
#   - Handle exceptione when timeout?
import requests
import json
from datetime import datetime
import csv
import concurrent.futures
from time import sleep
import argparse
import pandas as pd
from pprint import pprint 
headers = {
    'Content-Type': 'application/json' }

device_states = set()
output = []

now = datetime.now()

def get_clusters(file_path='clusters.json'):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} does no exists.")
    except json.JsonDecodeError:
        print(f"Error: The file {file_path} contains invalid JSON.")
        return None

clusters = get_clusters()
# clusters =  [{'cluster': 'sqa-4k', 'url': 'https://sqa-sca.manage.ovcirrus.com'}, {'cluster': 'prod-us', 'url': 'https://us.manage.ovcirrus.com'}, {'cluster': 'prod-eu', 'url': 'https://eu.manage.ovcirrus.com'}]

print("clusters = ", clusters)
if clusters is not None:
    for cluster in clusters:
        print(f"Cluster: {cluster['cluster']}, URL: {cluster['url']}")

def parse_argument():
    """parse cmd arguments
    """

    usage = 'Description: Get the device status in cluster'
    parser = argparse.ArgumentParser(description=usage, formatter_class=argparse.RawDescriptionHelpFormatter)

    # The choices parameter restricts the argument values to a specific set of valid options. If the user provides a value not in this list, argparse will raise an error.
    # The dest parameter sets the name of the attribute under which the argument value will be stored in the Namespace object returned by parse_args().
    # metavar just show output when using --help
    parser.add_argument(
            '-c',
            "--cluster",
            dest='cluster',
            action='store',
            metavar=('cluster'),
            choices=[cluster['cluster'] for cluster in clusters],
            help='The cluster name',
            required=True)

    parser.add_argument(
            '-u',
            "--username",
            dest='username',
            action='store',
            metavar=('username'),
            help='The username of superadmin account')
    
    parser.add_argument(
            '-p',
            "--password",
            dest='password',
            action='store',
            metavar=('password'),
            help='The password of superadmin account')

    parser.add_argument(
            '-m',
            "--msp",
            dest='msp',
            action='store',
            metavar=('msp'),
            help='(Optional) The MSP')

    parser.add_argument(
            '-o',
            "--org",
            dest='org',
            action='store',
            metavar=('org'),
            help='(Optional) The Organization')

    parser.add_argument(
            '-s',
            "--site",
            dest='site',
            action='store',
            metavar=('site'),
            help='(Optional) The Site')

    parser.add_argument(
            '-d',
            "--detail",
            dest='detail',
            action='store_true',
            help='(Optional) List device')

    args = parser.parse_args()
    if args.site and not args.org:
        print("Please input org!")
        exit(1)

    if args.org and not args.msp:
        print("Please input msp!")
        exit(1)

    return args
def requestAPI(url, headers, data=None, method='GET', timeout=15, max_retries=3, retry_interval=5):
    for attempt in range(max_retries):
        try:
            response = requests.request(method, url, headers=headers, data=data, timeout=timeout)
            response.raise_for_status()  # Raise an exception for 4XX/5XX status codes
            return response
        except requests.exceptions.Timeout:
            print(f"Timeout occurred. Retrying... ({attempt + 1}/{max_retries})")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            if attempt == max_retries - 1:
                raise e
        sleep(retry_interval)
    return None

def login(url, username, password):
    try:
        payload = json.dumps({
            "email": username,
            "password": password
        })
        response = requestAPI(url + "/api/user/signin", headers, payload, "POST")
        response = response.json()
        if 'access_token' in response:
            headers["Authorization"] = "Bearer {}".format(response['access_token'])
            print("Login successful!")
            return True
        elif "data" in response and "isTwoFAEnabled" in response["data"] and response["data"]["isTwoFAEnabled"] == True:
            userId = response["data"]["userId"]
            print("userId {}".format(userId))
            token = input("Please enter the token: ")
            payload2FA = json.dumps({
                "userId": userId,
                "token": token
            })

            response = requestAPI(url + "/api/user/signin/googleAuthenticator/verify", headers, payload2FA, "POST")
            response = response.json()
            if 'access_token' in response:
                headers["Authorization"] = "Bearer {}".format(response['access_token'])
                return True
        print(response)
        return False
    except Exception as exception:
        print("Login failed: {}".format(exception))
        return False

def get_msp(url):
    print("#################### get_msp ####################")
    try:
        response = requestAPI(url + "/api/msps", headers=headers, method="GET")
        response = response.json()
        # print("### response of get_msp ###")
        # pprint(response)
        return response
        '''
        reponse =
        {'data': {'createdAt': '2023-08-28T07:45:08.072Z',
          'id': '64ec5084ecec4252c3de11fb',
          'is2FARequired': False,
          'name': "OVNG-PT-TMA Thailand's MSP",
          'updatedAt': '2024-02-29T09:39:04.270Z'},
          'message': 'The MSP has been successfully fetched.',
          'status': 200}
          '''
    except Exception as exception:
        print("Get MSP failed: {}".format(exception))
        return False
    

def get_org(url, msp_id):
    # print("#################### get_org ####################")
    response = requestAPI(url + "/api/msps/" + msp_id + "/organizations/summary", headers=headers, method="GET")
    response = response.json()
    # print("### response of get_org ###")
    #       pprint(response)
    return response
    # return response api, including headers, statuscode, ...
    # => need to process this returned api
    # example
    '''
    reponse = 
    {'data': [{'countryCode': 'ES',
           'createdAt': '2024-05-09T02:42:07.322Z',
           'id': '663c37ff1072861ac0dbc662',
           'totalSites': 1,
           'updatedAt': '2024-05-09T02:42:07.322Z'},
          {'countryCode': 'AT',
           'createdAt': '2024-03-21T03:28:40.447Z',
           'id': '65fba96851621000f0a70880',
           'idleTimeout': 3600,
           'imageUrl': '',
           'updatedAt': '2024-03-21T03:28:40.447Z'},
          {'countryCode': 'TH',
           'createdAt': '2023-08-28T07:45:08.073Z',
           'id': '64ec5084ecec42502cde11fc',
           'idleTimeout': 3720,
           'imageUrl': '0290045d-ecd0-4316-8ae7-9005d941e61d.jpg',
           'totalDevices': 5,
           'totalOrgUsers': 7,
           'totalSites': 6,
           'updatedAt': '2024-01-25T10:35:25.730Z'}
           ]
    'message': 'The organizations have been successfully fetched.',
    'status': 200
    }
    '''

def get_site(url, org_id):
    # print("#################### get_site ####################")
    response = requestAPI(url + "/api/organizations/" + org_id + "/sites", headers=headers, method="GET")
    response = response.json()
    return response

def get_device_by_org(url, org_id):
    response = requestAPI(url + "/api/organizations/" + org_id + "/sites/device", headers=headers, method="GET")
    response = response.json()
    return response

def get_device_by_site(url, org_id, site_id):
    response = requestAPI(url + "/api/organizations/" + org_id + "/sites/" + site_id + "/devices", headers, method="GET")
    response = response.json()
    return response

def handle_msp(url, msp_id, msp_name, detail = False):
    # print("##############################################")
    # print("#### handle_msp ##############################")
    orgs = get_org(url, msp_id)
    # print("## orgs ###")
    # pprint("{orgs}")
    # orgs['data'] is list of dict
    ## processing responsed api of orgs
    org_params = []
    for org in orgs['data']:
        url = url
        msp_id = msp_id
        msp_name = msp_name
        org_id = org['id']
        org_name = org['name']
        detail = detail
        org_params.append((url, msp_id, msp_name, org_id, org_name, detail))
        
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        for tmp in executor.map(lambda p: handle_org(*p), org_params):
            pass
    # print("## orgs_params ###")
    # pprint(org_params)
    '''
    [('https://sqa-sca.manage.ovcirrus.com',
    '64ec5084ecec4252c3de11fb',
    "OVNG-PT-TMA Thailand's MSP",
    '663c37ff1072861ac0dbc662',
    'RAP ORG #20',
    False),
    ('https://sqa-sca.manage.ovcirrus.com',
    '64ec5084ecec4252c3de11fb',
    "OVNG-PT-TMA Thailand's MSP",
    '65fba96851621000f0a70880',
    'AAA',
    False),]
    '''

def handle_org(url, msp_id, msp_name, org_id, org_name, detail = False):
    # print("##############################################")
    # print("#### handle_org ##############################")
    sites = get_site(url, org_id)

    site_params = [(url, msp_id, msp_name, org_id, org_name, site['id'], site['name'], detail) for site in sites['data']]
    # print("## site_params ###")
    # pprint(site_params)
    '''
    [('https://sqa-sca.manage.ovcirrus.com',
    '64ec5084ecec4252c3de11fb',
    "OVNG-PT-TMA Thailand's MSP",
    '6516d1f8233996c5b7b208bf',
    'new-org-10.4-restoring',
    '6516d1f823399681c8b208c3',
    'Unnamed site',
    False)]
    '''
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        for o in executor.map(lambda p: handle_site(*p), site_params):
            if o:
                output.append(o)

    return True

def handle_site(url, msp_id, msp_name, org_id, org_name, site_id, site_name, detail = False):
    # print("##############################################")
    # print("#### handle_site ##############################")
    # site_devices: responsed api 
    # site_devices_data: actual data
    # device_states: list device states
    # state: iterates over each unique device state
    # devices_device_state: list device in current state
    # number_devices_device_state: len list device have same state

    site_devices = get_device_by_site(url, org_id, site_id)
    # print("## site_device ###")
    # pprint(site_devices)
    '''
    {'data': [{'_insertedTS': None,
            'serialNumber': 'AP199851',
            },
            {'_insertedTS': None,
            'serialNumber': '111111111111AA',},
            {'_insertedTS': None,
            'serialNumber': 'AAAAAAAAA',
            'site': {'id': '65b1e3b57a03a0ec03f85f56', 'name': 'ANH'}
            'workMode': '',
            'workingMode': None}],
            'message': 'Devices have been successfully fetched.',
            'status': 200}
        '''
    if not 'data' in site_devices:
        print(site_devices)
        
    # Retrieves the actual devices data.
    site_devices_data = site_devices['data']
    
    if not site_devices_data:
        return None
    
    for device in site_devices_data:
        # print("### device ###")
        # print(device)
        '''
        {'id': '65f8fcc9492bb0ae03078715', 'name': 'AP-1E:20', 'deviceStatus': 'waitingForFirstContact', 'ipAddress': '172.16.101.63', 'ipAddressV6': '', 'friendlyName': '172.16.101.63 (AP-1E:20)', 'state': 'active'}
        '''
        device_states.add(device['deviceStatus'] if 'deviceStatus' in device else 'UNKOWN')
    
    o = {
        "msp_id": msp_id,
        "msp_name": msp_name,
        "org_id": org_id,
        "org_name": org_name,
        "site_id": site_id,
        "site_name": site_name
    }
    
    log = "- MSP id {} - msp name {} - org id {} - org name {} - site id {} - site name: {}:".format(msp_id, msp_name, org_id, org_name, site_id, site_name)
    
    # Iterates over each unique device state.
    # Filters devices that match the current state.
    # Counts the number of devices in this state.
    # Adds the count and serial numbers (or the device itself if serial number is not present) to the dictionary o.
    for state in device_states:
        devices_device_state = [device for device in site_devices_data if 'deviceStatus' in device and device['deviceStatus'] == state]
        number_devices_device_state = len(devices_device_state)
        o[state] = {}
        o[state]['number'] = number_devices_device_state
        o[state]['data'] = [device['serialNumber'] if 'serialNumber' in device else str(device) for device in devices_device_state]

        log += "\n      + {}: {}".format(state, number_devices_device_state)
        if detail and number_devices_device_state != 0:
            log += ", list serial number device: {}".format(", ".join(o[state]['data']))

    print(log)
    return o
def main():

    args = parse_argument()
    cluster_name = args.cluster

    url = None
    for cluster in clusters:
        if cluster['cluster'] == cluster_name:
            url = cluster["url"]
            print("url: ", url)
            break
    # url = [cluster["url"] for cluster in clusters if cluster["cluster"] == cluster_name][0]
    now_str = "{}{:02d}{:02d}_{:02d}{:02d}{:02d}".format(now.year, now.month, now.day, now.hour, now.minute,        now.second)
    output_filename = f"./output/number_devices_{cluster_name}_{now_str}.csv"

    print(f"You are connecting to {url}!")
    if args.username is None:
        username = input("Please provide username: ")
    else:
        username = args.username
    password = args.password
    msp = args.msp
    org = args.org
    site = args.site
    detail = args.detail

    if not login(url, username, password):
        print("Can not login")
        return
    print("trigger")
    msp_data = get_msp(url)['data']
    ''' 
    one msp: type of msp_data: <class 'dict'>
        msp_data = { 'createdAt': '2023-08-28T07:45:08.072Z', 'updatedAt': '2024-02-29T09:39:04.270Z', 'id': '64ec5084ecec4252c3de11fb', 'name': "OVNG-PT-TMA Thailand's MSP", 'is2FARequired': False }
    # multiple msps: type of msp_data: <class 'list'>
    '''
    # print(f"msp_data: {msp_data}")
    # print(f"type of msp_data: {type(msp_data)}")

    if not msp and not org and not site:
        print("just pass cluster infor in command line!")
        msp_params = []
        if isinstance(msp_data, dict):
            url = url
            id = msp_data['id']
            name = msp_data['name']
            detail = detail
            msp_params.append((url, id, name, detail))

        elif isinstance(msp_data, list):
            for msp in msp_data:
                url = url
                id = msp['id']
                name = msp['name']
                detail = detail
                msp_params.append((url, id, name, detail))
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            for tmp in executor.map(lambda p: handle_msp(*p), msp_params):
                pass
        # print("##############################################")
        # print("##############################################")
        # msp_params  [('https://sqa-sca.manage.ovcirrus.com', '64ec5084ecec4252c3de11fb', "OVNG-PT-TMA Thailand's MSP", False)]
        # print("msp_params ", msp_params)
        

if __name__ == "__main__":
    main()
