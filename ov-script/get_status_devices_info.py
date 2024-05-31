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

def login(url, usernmae, password):
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

def main():

    parse_argument()
    cluster_name="prod-us"

    url = None
    for cluster in clusters:
        if cluster['cluster'] == cluster_name:
            url = cluster["url"]
            print("url: ", url)
            break

if __name__ == "__main__":
    main()
