import requests
import json
from datetime import datetime
import csv
import concurrent.futures
from time import sleep
import argparse
import pandas as pd

headers = {
    'Content-Type': 'application/json'
}

device_states = set()
output = []

now = datetime.now()


def get_clusters(file_path='clusters.json'):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return None
    except json.JSONDecodeError:
        print(f"Error: The file {file_path} contains invalid JSON.")
        return None

clusters = get_clusters()

if clusters is not None:
    for cluster in clusters:
        print(f"Cluster: {cluster['cluster']}, URL: {cluster['url']}")

clusters = get_clusters()

def parse_argument():
    """parse cmd arguments
    """
    usage = 'Description: Get the device status in cluster'
    parser = argparse.ArgumentParser(description=usage,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-c', "--cluster", dest='cluster', action='store', metavar=('cluster'),
                        choices=[cluster['cluster'] for cluster in clusters],
                        help='The cluster name', required=True)
    parser.add_argument('-u', "--username", dest='username', action='store', metavar=('username'),
                        help='The username of superadmin account')
    parser.add_argument('-m', "--msp", dest='msp', action='store', metavar=('msp'),
                        help='(Optional) The MSP')
    parser.add_argument('-o', "--org", dest='org', action='store', metavar=('org'),
                        help='(Optional) The organization')
    parser.add_argument('-s', "--site", dest='site', action='store', metavar=('site'),
                        help='(Optional) The site')

    parser.add_argument('-d', "--detail", dest='detail', action='store_true',
                        help='(Optional) List device')

    args = parser.parse_args()

    if args.site and not args.org:
        print("Please input org!")
        exit(1)

    if args.org and not args.msp:
        print("Please input msp!")
        exit(1)

    return args

def requestAPI(url, headers, data = None, method = 'GET'):
    while(True):
        count = 0
        try:
            if data:
                response = requests.request(method, url, headers=headers, data=data, timeout=15)
            else:
                response = requests.request(method, url, headers=headers, timeout=15)

            if response.status_code == 200:
                return response
            else:
                raise Exception(response)
        except Exception as exception:
            if count >= 15:
                raise exception
            count += 1
            sleep(5)

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
        elif "data" in response and "isTwoFAEnabled" in response["data"] and  response["data"]["isTwoFAEnabled"] == True:
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
        print (response)
        return False

    except Exception as exception:
        print( "Login failed: {}".format(exception))
        return False

def get_msp(url):
    try:
        response = requestAPI(url + "/api/msps", headers=headers, method="GET")
        response = response.json()
        return response
    except Exception as exception:
        print( "Get MSP failed: {}".format(exception))
        return False

def get_org(url, msp_id):
    response = requestAPI(url + "/api/msps/" +msp_id +"/organizations/summary", headers=headers, method="GET")
    response = response.json()
    print("orgs ", response)
    return response

def get_site(url, org_id):
    response = requestAPI(url + "/api/organizations/" +org_id +"/summary", headers=headers, method="GET")
    response = response.json()
    return response

def get_device_by_org(url, org_id):
    response = requestAPI(url + "/api/organizations/" +org_id +"/sites/devices", headers=headers, method="GET")
    response = response.json()
    return response

def get_device_by_site(url, org_id, site_id):
    response = requestAPI(url + "/api/organizations/" +org_id +"/sites/" + site_id + "/devices", headers=headers, method="GET")
    response = response.json()
    return response

def handle_msp(url, msp_id, msp_name, detail = False):
    orgs = get_org(url, msp_id)
    org_params = [(url, msp_id, msp_name, org['id'], org['name'], detail) for org in orgs['data']]

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        for tmp in executor.map(lambda p: handle_org(*p), org_params):
            pass

    return True
def handle_org(url, msp_id, msp_name, org_id, org_name, detail = False):
    sites = get_site(url, org_id)

    site_params = [(url, msp_id, msp_name, org_id, org_name, site['id'], site['name'], detail) for site in sites['data']['sites']]
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        for o in executor.map(lambda p: handle_site(*p), site_params):
            if o:
                output.append(o)

    return True

def handle_site(url, msp_id, msp_name, org_id, org_name, site_id, site_name, detail = False):
    site_devices = get_device_by_site(url, org_id, site_id)
    if not 'data' in site_devices:
        print(site_devices)
    site_devices_data = site_devices['data']

    if not site_devices_data:
        return None

    for device in site_devices_data:
        print(device)
        device_states.add(device['deviceStatus'] if 'deviceStatus' in device else 'UNKNOWN')

    o = {
        "msp_id": msp_id,
        "msp_name": msp_name,
        "org_id": org_id,
        "org_name": org_name,
        "site_id": site_id,
        "site_name": site_name,
    }
    log = "- Msp id {} - msp name {} - org id {} - org name {} - site id {} - site name: {}:".format(msp_id, msp_name, org_id, org_name, site_id, site_name)

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

def write_to_file(output_filename, detail = False):
    print('Writing to {}...'.format(output_filename))

    with open(output_filename, 'w') as file_object:
        if not detail:
            output_writer = csv.writer(file_object)
            output_writer.writerow([
                'MSP ID',
                'MSP Name',
                'Org ID',
                'Org Name',
                'Site ID',
                'Site Name'
            ] + list(device_states)
            )

            for o in output:
                number_devices = []
                for state in device_states:
                    number_device = o[state]['number'] if state in o else 0
                    number_devices.append(number_device)

                output_writer.writerow(
                    [
                        o['msp_id'],
                        o['msp_name'],
                        o['org_id'],
                        o['org_name'],
                        o['site_id'],
                        o['site_name']
                    ] + list(number_devices)
                )
        else:
            output_writer = csv.writer(file_object)
            output_writer.writerow([
                'MSP ID',
                'MSP Name',
                'Org ID',
                'Org Name',
                'Site ID',
                'Site Name',
                'Serial Number',
                'Status',
                'Number with same status'
            ]
            )
            for o in output:
                for state in device_states:
                    if not state in o:
                        continue

                    for device in o[state]['data']:
                        output_writer.writerow(
                        [
                            o['msp_id'],
                            o['msp_name'],
                            o['org_id'],
                            o['org_name'],
                            o['site_id'],
                            o['site_name'],
                            device,
                            state,
                             o[state]['number']
                        ]
                    )
        print("done!")

def print_total_device():
    print("- Device by state: ")
    sum = 0
    for state in device_states:
        sum_state = 0
        for o in output:
            sum_state += o[state]['number'] if state in o else 0
        print("     + {}: {}".format(state, sum_state))
        sum += sum_state
    print("- Sum: {}".format(sum))

def print_checklist(output_filename):
    print('*********'*5)
    df = pd.read_csv(output_filename)

    df = df.sort_values('OV Managed',ascending=False)
    df = df[['MSP Name','Org Name','Site Name','OV Managed']]

    count_numberOrgDevice = (df['OV Managed'] != 0).sum()
    print(f"Number of Org have Device: {count_numberOrgDevice}\n")

    print("Top 5 Org has most devices")
    print(df.head())

def print_msg_org_site(url):
    print("MSP: ")
    msp_data = get_msp(url)
    for msp in msp_data:
        print(f"- MSP ID: {msp['id']}, MSP Name: {msp['name']}")

    #print("\nOrganizations: ")
    #for msp in msp_data:
    #    org_data = get_org

def main():
    args = parse_argument()
    cluster_name = args.cluster
    url = [cluster["url"] for cluster in clusters if cluster["cluster"] == cluster_name][0]
    print("url :", url)
    now_str = "{}{:02d}{:02d}_{:02d}{:02d}{:02d}".format(now.year, now.month, now.day, now.hour, now.minute, now.second)
    output_filename = f"./output/number_devices_{cluster_name}_{now_str}.csv"

    print(f"You are connecting {url}!")

    if args.username is None:
        username = input("Please provide username: ")
    else:
        username = args.username

    password = input("Please provide password: ")

    msp = args.msp
    org = args.org
    site  = args.site
    detail = args.detail

    print("msp: ", msp)
    if not login(url, username, password):
        print("Can not login")
        return
    # sleep(2000)
    print("trigger")
    msp_data = get_msp(url)['data']
    print("msp_data = ", msp_data)
    # msp_data = msp_data

    if not msp and not org and not site:
        msp_params =[]
        for msp in msp_data:
            print("msp: ", msp)
            url = url
            id = msp['id']
            name = msp['name']
            detail = detail
            msp_params.apeend((url, id, name, detail))
        # msp_params = [(url, msp['id'], msp['name'], detail) for msp in msp_data]
        print("msp_params ", msp_params)
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            for tmp in executor.map(lambda p: handle_msp(*p), msp_params):
                pass

    elif msp and not org and not site:
        msp_name = [ m['name'] for m in msp_data if m['id'] == msp][0]
        handle_msp(url, msp, msp_name, detail)

    elif msp and org and not site:
        msp_name = [ m['name'] for m in msp_data if m['id'] == msp][0]
        orgs_data = get_org(url, msp)['data']
        org_name =  [ o['name'] for o in orgs_data if o['id'] == org][0]
        handle_org(url, msp, msp_name, org, org_name, detail)
    elif msp and org and site:
        msp_name = [ m['name'] for m in msp_data if m['id'] == msp][0]
        orgs_data = get_org(url, msp)['data']
        org_name =  [ o['name'] for o in orgs_data if o['id'] == org][0]
        sites = get_site(url, org)
        site_name = [ s['name'] for s in sites['data']['sites']][0]
        o = handle_site(url, msp, msp_name, org, org_name, site, site_name, detail)
        output.append(o)

    write_to_file(output_filename, detail)
    print_total_device()

    print_checklist(output_filename)

if __name__ == "__main__":
    main()
