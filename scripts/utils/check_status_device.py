#!/usr/bin/env python

import csv
from datetime import datetime
import sys
import os
import argparse
import concurrent.futures
from os import path
from pprint import pprint

# Get the absolute path of script
absolute_path = path.abspath(__file__) # Output: /home/ubuntu/python-script/scripts/check_status_device.py
# Get directory of script
module_dir = path.dirname(absolute_path) # Output: /home/ubuntu/python-script/scripts
# The sys.path.append() method is used to add a specific directory to this list, meaning Python will also look in this directory when importing modules.
sys.path.append(path.dirname(module_dir))

from lib.datapond import  DataPond
from lib.libtenant import Tenant
from lib.util import setup_logger
from dao.utility import UtilityDAO as dao

script_file_name = (os.path.basename(__file__)).split('.')[0].strip()
log_file = script_file_name + '.log'

if os.path.exists(log_file):
    os.remove(log_file)
else:
    print("The log file doesn't exists")

now = datetime.now()
now_str = "{}{:02d}{:02d}_{:02d}{:02d}{:02d}".format(now.year, now.month, now.day, now.hour, now.minute, now.second)

status_devices_tenant_file_name = "managed_devices_per_tenant_{}.csv".format(now_str)
status_devices_tenant_with_serial_number_file_name = "managed_devices_per_tenant_with_serial_number_{}.csv".format(now_str)
status_devices_tenant_response_file_name = "managed_devices_all_{}.log".format(now_str)
print('*** Data is written to {} and {}. ***'.format(status_devices_tenant_file_name, status_devices_tenant_response_file_name))

logger = setup_logger(script_file_name, is_verbose=False)
now = datetime.utcnow()
query_time = 600000

def main():
    description_message = '''
    Description: Get all devices with ovManaged and assigned status and last callhome time less than or equal to 10 minutes.\n\n\r \
    Example: python %(prog)s -e dev \n
    '''

    parser = argparse.ArgumentParser(description=description_message, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-e', '--environment', help='environment: dev, prod, etc.', required=True)

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-r', 
        dest='data_center_region',
        action='store', 
        choices=['ap-southeast-1', 'ap-south-1', 'ca-central-1', 'eu-central-1'],
        metavar='data_central_region_name',
        help='(Optional) The data center region name'
    )

    group.add_argument('-o',
        dest='ov_ids',
        action='append',
        metavar='ov_instance',
        help='(Optional) OV instance ID')
    
    args = parser.parse_args()
    env = args.environment

    credentials = dao.getConfig(env)
    datapond_username = credentials["DataPond"]["Username"]
    datapond_password = credentials["DataPond"]["Password"]

    name_space = '.' + env
    datapond_url = "https://datapond" + name_space + ".myovcloud.com:1337"
    dp = DataPond(datapond_url, "dataPond", datapond_username, datapond_password)
    dp.login()

    # Query testing
    get_tenant = dp.find_all("Tenant", {"ovInstanceId":"725477ab-b88c-4c54-8ec5-83a405488308"})
    
    stackstorm_settings = dp.find_one("Global", {"name": "StackstormSettings"})["value"]
    pprint(stackstorm_settings)
    tenant_configs = {
        "environment": env,
        "system_support": credentials["Tov"]["system-support"], # username and password of user support
        "stackstorm_settings": stackstorm_settings
    }

    Tenant.init_class(tenant_configs)
    # query data (e.g. the whole Device table) from datapond may take long time,
    # you may want to write the data from DP to a file to use later

    print('Querying data from {}.'.format(datapond_url))
if __name__ == "__main__":
    main()