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
    parser.add_argument('-c', "--cluster", dest='cluster', action='store', metavar=('cluster'), choices=[cluster['cluster'] for cluster in clusters], help='The cluster name', required=True)=<

def main():
    arg = parse_argument()
    cluster_name="prod-us"

    url = None
    for cluster in clusters:
        if cluster['cluster'] == cluster_name:
            url = cluster["url"]
            print("url: ", url)
            break

if __name__ == "__main__":
    main()
