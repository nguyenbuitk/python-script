
import requests
import time
import json
import os
from lib.datapond import DataPond

#from pprint import pprint


class Tenant():
    
    environment = None
    system_support = None
    stackstorm_settings = None
    verbose = None
    is_using_ale_cert = None
    timeout = None
    
    verify_ssl = True
    ###    
    
    login_api = '/api/login'
    ham_agconfig_api = '/api/ham/agconfig'
    device_status_api = "/api/devices?fieldSetName=discovery"
    scheduler_api = '/api/scheduler'
    device_catalogue_api = '/api/inventory/devices/filter'
    managed_devices_api = '/api/devices?fieldSetName=discovery'
    mesh_aps_api = '/api/wma/accessPoint/getAPList/normal'
    upam_authen_record_api = '/api/ham/radius/authRecord/getPageAuthRecordList'
    upam_authen_strategy_api = '/api/ham/authentication/strategy/getStrategylist'
    upam_captive_portal_record_api = '/api/ham/accessRecord/getPageAccessRecord'
    request_header = {'Content-Type': 'application/json'}
    
    @classmethod    
    def init_class(cls, configs):
        cls.environment = configs['environment']
        cls.system_support = configs['system_support']
        cls.stackstorm_settings = configs['stackstorm_settings']
        cls.verbose = cls.stackstorm_settings["monitoring"]["verbose"]
        cls.is_using_ale_cert = cls.stackstorm_settings["monitoring"]["tenant"]["is_using_ale_cert"]
        cls.timeout = 10
        cls.timeout = cls.stackstorm_settings["monitoring"]["tenant"]["timeout"]
    
    def __init__(self, vanity_subdomain, user_credentials=system_support, verbose=verbose):        
        
        self.verbose = verbose
        self.is_logged_in = False
        self.timestamp = int(time.time())
        self.vanity_subdomain = vanity_subdomain
        self.conn = requests.Session()
        if Tenant.environment == "prod":
            self.ov_fqdn = ".".join([vanity_subdomain, "ov", "ovcirrus", "com"])
        else:
            self.ov_fqdn = ".".join([vanity_subdomain, "ov", Tenant.environment, "ovcirrus", "com"])
        
        if Tenant.is_using_ale_cert is True:
            self.conn.verify = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/certs/ale-bundle.crt"
            
        self.login_url = self.get_api_url(Tenant.login_api)
        self.ham_agconfig_url = self.get_api_url(Tenant.ham_agconfig_api)
        self.device_status_url = self.get_api_url(Tenant.device_status_api)
    
    
    def get_api_url(self, api_path):
        url = "https://" + self.ov_fqdn + api_path
        return url
        
    def login(self, user_credentials=system_support, verbose=None):
        if verbose is None:
            verbose = self.verbose
        
        login_request_body = {
            "userName": user_credentials["username"],
            "password": user_credentials["password"],
            "support": "true"
        }

        max_retry = 10
        retry = 0
        while retry < max_retry:
            try:
                response = self.conn.post(self.login_url, json=login_request_body, headers=Tenant.request_header, verify=Tenant.verify_ssl, timeout=Tenant.timeout)
                response_json = response.json()
                if response_json.get("accessToken", None) and response_json.get("message", None) == "login.success":
                    # check token returned by api/login
                    device_api_response = self.get_devices_status()
                    if device_api_response.json().get("status", None) == "SUCCESS":
                        self.is_logged_in = True
                        return response
            
            except requests.exceptions.ConnectTimeout as e:
                print("[ERROR-login - {}] ConnectTimeout".format(self.vanity_subdomain))               
            except requests.exceptions.ReadTimeout as e:
                print("[ERROR-login - {}] ReadTimeout".format(self.vanity_subdomain))
            except requests.exceptions.ConnectionError as e:
                print("[ERROR-login - {}] ConnectionError".format(self.vanity_subdomain))         
            except requests.exceptions.RequestException as e:
                print("[ERROR-login - {}] RequestException".format(self.vanity_subdomain))          
            except Exception as e:
                print("[ERROR-login - {}]".format(self.vanity_subdomain), e)

            retry = retry + 1
            time.sleep(10)
        return None
         
    def login_as_support_user(self, verbose=None):
        if verbose is None:
            verbose = self.verbose
        response = self.login(Tenant.system_support, verbose)
        return response
    
    
    def get_x_status(self, api_path, verbose=None):
        if self.is_logged_in == False:
            self.login_as_support_user()

        if self.is_logged_in == True:
            if verbose is None:
                verbose = self.verbose
            try:
                api_url = self.get_api_url(api_path)
                response = self.conn.get(api_url, headers = Tenant.request_header, verify=Tenant.verify_ssl, timeout=Tenant.timeout)
                return response
            except Exception as e:
                print("[ERROR-get_x_status (x={}) - {}]".format(api_url, self.vanity_subdomain), e)
                return None
        else:
            print('Not logged in yet!')
            return None
            
    def get_devices_status(self, verbose=None):
        if verbose is None:
            verbose = self.verbose
        try:
            response = self.conn.get(self.device_status_url, headers = Tenant.request_header, verify=Tenant.verify_ssl, timeout=Tenant.timeout)
            return response
        except Exception as e:
            print("[ERROR-get_devices_status - {}]".format(self.vanity_subdomain), e)
            return None
    #'''
    def get_upam_status(self, verbose=None):
        return self.get_x_status(api_path=Tenant.ham_agconfig_api, verbose=verbose)
    
    def get_scheduler_status(self, verbose=None):
        return self.get_x_status(api_path=Tenant.scheduler_api, verbose=verbose)
        
    def get_managed_devices(self, verbose=None):
        max_retry = 10
        retry = 0
        while retry < max_retry:
            try:
                response = self.get_x_status(api_path=Tenant.managed_devices_api, verbose=verbose)
                if response != None:
                    return response
            except Exception as e:
                print("[ERROR-get_managed_devices - {}]".format(self.vanity_subdomain), e)
            retry = retry + 1
            time.sleep(10)
        return None
        
    def get_mesh_aps(self, verbose=None):
        max_retry = 5
        retry = 0
        while retry < max_retry:
            response = self.get_x_status(api_path=Tenant.mesh_aps_api, verbose=verbose)
            if response != None:
                return response
            else:
                retry = retry + 1
                time.sleep(3)
            if retry == max_retry:
                print(' ********* Could not access tenant {}!  ********* '.format(self.vanity_subdomain))
        return None
        
    def get_upam_authen_strategies(self, verbose=None):
        max_retry = 5
        retry = 0
        while retry < max_retry:
            response = self.get_x_status(api_path=Tenant.upam_authen_strategy_api, verbose=verbose)
            if response != None:
                return response
            else:
                retry = retry + 1
                time.sleep(3)
            if retry == max_retry:
                prin
    
    def get_upam_authen_records(self, verbose=None):
        max_retry = 5
        retry = 0
        request_body = {
            "start": "",
            "querySize": 1000
        }
        while retry < max_retry:
            api_url = self.get_api_url(Tenant.upam_authen_record_api)
            response = response = self.conn.post(api_url, json=request_body, headers=Tenant.request_header, verify=Tenant.verify_ssl, timeout=Tenant.timeout)
            if response != None:
                return response
            else:
                retry = retry + 1
                time.sleep(3)
            if retry == max_retry:
                print(' ********* Could not access tenant {}!  ********* '.format(self.vanity_subdomain))
        return None
    
    def get_upam_captive_portal_records(self, verbose=None):
        max_retry = 5
        retry = 0
        request_body = {
            "start": "",
            "querySize": 1000
        }
        while retry < max_retry:
            api_url = self.get_api_url(Tenant.upam_captive_portal_record_api)
            response = response = self.conn.post(api_url, json=request_body, headers=Tenant.request_header, verify=Tenant.verify_ssl, timeout=Tenant.timeout)
            if response != None:
                return response
            else:
                retry = retry + 1
                time.sleep(3)
            if retry == max_retry:
                print(' ********* Could not access tenant {}!  ********* '.format(self.vanity_subdomain))
        return None
