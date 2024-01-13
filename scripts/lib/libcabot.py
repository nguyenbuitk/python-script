import os, sys, time
import json
import requests
from requests.adapters import HTTPAdapter
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.util.retry import Retry


class Cabot(object):
    
    # mode=st2: run on stackstorm; mode=manual: run manually on local VM
    def __init__(self,env=None, mode="st2"):
        print "> Create Cabot-Request object ..."
        
        if env is None:
            raise ValueError("> ERR: \'Environment\' parameter is missing ! ")
        
        #Get configs
        self.environment = env
        
        
        if mode == "manual":
            try:
                from dao.utility import UtilityDAO as dao
                configs = dao.getConfig(env)                
                self.uri = configs["Cabot"]["Protocol"]+'://'+configs["Cabot"]["Hostname"].replace("{Env}",self.environment)+':'+str(configs["Cabot"]["Port"])
                print "    -- Get requests URI: "+self.uri
                self.user = configs["Cabot"]["Username"]
                self.pwd = configs["Cabot"]["Password"]
                '''
                self.tov_metric_prefix = ""
                self.tenant_metric_prefix = ""    
                self.alerts = []    
                self.users_to_notify = []    
                self.tenant_checks = []
                '''                

            except ImportError:
                pass
        elif mode == "st2":
            try:
                from lib import OvConfig
                configs = OvConfig()
                cabot_configs = configs.get("monitoring")["cabot"]
                self.uri =  cabot_configs["protocol"] + "://" + cabot_configs["address"] + ":" + cabot_configs["port"]
                self.user = cabot_configs["username"]
                self.pwd = cabot_configs["password"]
                self.tov_metric_prefix = cabot_configs["tov_metric_prefix"]
                self.tenant_metric_prefix = cabot_configs["tenant_metric_prefix"]
                self.alerts = [cabot_configs["alerts"]["email"], cabot_configs["alerts"]["slack"]]
                self.users_to_notify = [cabot_configs["users_to_notify"]["admin"]]
                self.tenant_checks =  configs.get("monitoring")["tenant_checks"]
                
            except Exception as e:
                print("[ERROR-cabot.init] {}".format(e))
        
        self.cabot_check_template = {
            "name": None,
            "active": True,
            "importance": "ERROR",
            "frequency": 6,
            "debounce": 0,
            "calculated_status": "passing",
            "metric": None,
            "check_type": "<",
            "value": "1",
            "expected_num_hosts": 1,
            "allowed_num_failures": 0
        }
        self.cabot_service_template = {
            "name": None,
            "users_to_notify": self.users_to_notify,
            "alerts_enabled": True,
            "status_checks": [],
            "alerts": self.alerts,
            "hackpad_id": "",
            "url": "",
            "instances": [],
            "overall_status": "PASSING"
        }
        #Prepare session
        self.session = requests.Session()
        adapter = HTTPAdapter(max_retries=Retry(connect=2, backoff_factor=1))
        self.session.mount('http://', adapter)
        
        #Authenticate
        try:            
            self.session.auth = HTTPBasicAuth(self.user, self.pwd)
            print "    -- Authenticated "
            
        except:
            print "    -- No credential defination, please authenticate late..."
        
        #Token-Authenticate
        self.csrf_token = ''
        self.login_url = self.uri+'/accounts/login/'
        
        #Check connection
        print ( "> [OK] " if self.check_connection() else "> [FAIL] " ) + "Check connection"
    
    def authenticate(self,usr,pwd):
        # Use other credentials
        self.user = usr
        self.pwd = pwd
        self.session.auth = HTTPBasicAuth(self.user, self.pwd)
        
        if self.find_all_objs('services').status_code == 200:
            print "> Login success"
        else:
            print "> Login failed - Invalid username/password !"
    
    def token_authenticate(self):
        # Use other credentials
        r = self.session.get(self.login_url,headers=dict(Referer=self.login_url))
        r_token = r.cookies['csrftoken']
        r2 = self.session.post(self.login_url,headers=dict(Referer=self.login_url),data={"username":self.user,"password":self.pwd,"csrfmiddlewaretoken": r_token})
        self.csrf_token = self.session.cookies['csrftoken']
        
        if self.csrf_token:
            print "> Token-auth success"
        else:
            print "> Token-auth failed !"
            return None
        return self.csrf_token
    
    def check_connection(self):
        # return <Boolean>
        try:
            r = self.session.get(self.uri)
            if r.status_code != 200:
                print("Non-200 status !")
                return False
            return True
        except Exception, e:
            print("[ERROR-cabot.check_connection] {}".format(e))
            return False
    
    def _collect(self,url,headers={},data={}):
        r = self.session.get(url,headers=headers,data=data)
        return r
    
    def _create(self,url,headers,data):
        r = self.session.post(url,headers=headers,json=data)
        return r
    
    def _update(self,url,headers,data):
        r = self.session.put(url,headers=headers,json=data)
        return r
    
    def _delete(self,url):
        r = self.session.delete(url)
        return r
    
    """
    CHECKS
    """
    def run_check(self,id):
        # return <Object>
        # done when status code is 200
        print "> Execute check immediately"
        if self.csrf_token == '': self.token_authenticate()
        
        return self.session.get(self.uri+'/check/run/'+str(id)+'/',headers=dict(Referer=self.login_url))
    
    """
    === GRAPHITE CHECKS
    """
    def create_graphite_check(self,data):
        # return <Object>
        print "> Create graphite check"
        return self._create(self.uri+'/api/graphite_checks/',{'Content-Type':'application/json'},data)
    
    def update_graphite_check(self,data,id):
        # return <Object>
        print "> Update graphite check"
        return self._update(self.uri+'/api/graphite_checks/'+str(id)+'/',{'Content-Type':'application/json'},data)
    
    def delete_graphite_check(self,id):
        # return <Object>
        print "> Delete graphite check"
        return self._delete(self.uri+'/api/graphite_checks/'+str(id)+'/')
    
    def find_graphite_check(self,keyname):
        # return <List>
        obj_list = json.loads(self.find_all_objs('graphite_checks').content)
        return_list = []
        for obj in obj_list:
            if keyname in obj["name"]:
                return_list.append(obj)
        return return_list
    
    def find_exact_graphite_check(self,keyname):
        # return <List>
        obj_list = json.loads(self.find_all_objs('graphite_checks').content)
        return_list = []
        for obj in obj_list:
            if keyname == obj["name"]:
                return_list.append(obj)
        if len(return_list) > 1:
            print("There are duplicated checks with the name '{}'".format(keyname))
        return return_list        
        
    def check_and_create_graphite_check(self,data):
        if self.find_exact_graphite_check(data["name"]):
            print("Already exist a '{}' check. Exit without creating one.".format(data["name"]))
            return None
        else:
            return self.create_graphite_check(data)
    
    
    """
    === PING CHECKS
    """
    def create_ping_check(self,data):
        # return <Object>
        print "> Create ping check"
        return self._create(self.uri+'/api/icmp_checks/',{'Content-Type':'application/json'},data)
    
    def update_ping_check(self,data,id):
        # return <Object>
        print "> Update ping check"
        return self._update(self.uri+'/api/icmp_checks/'+str(id)+'/',{'Content-Type':'application/json'},data)
    
    def delete_ping_check(self,id):
        # return <Object>
        print "> Delete ping check"
        return self._delete(self.uri+'/api/icmp_checks/'+str(id)+'/')
    
    def find_ping_check(self,keyname):
        # return <List>
        obj_list = json.loads(self.find_all_objs('icmp_checks').content)
        return_list = []
        for obj in obj_list:
            if keyname in obj["name"]:
                return_list.append(obj)
        return return_list
    
    """
    INSTANCES
    """
    def create_instance(self,data):
        # return <Object>
        print "> Create monitor instance"
        return self._create(self.uri+'/api/instances/',{'Content-Type':'application/json'},data)
    
    def update_instance(self,data,id):
        # return <Object>
        print "> Update monitor instance"
        return self._update(self.uri+'/api/instances/'+str(id)+'/',{'Content-Type':'application/json'},data)
    
    def delete_instance(self,id):
        # return <Object>
        print "> Delete monitor instance"
        return self._delete(self.uri+'/api/instances/'+str(id)+'/')
    
    def find_instance(self,keyname):
        # return <List>
        obj_list = json.loads(self.find_all_objs('instances').content)
        return_list = []
        for obj in obj_list:
            if keyname in obj["name"]:
                return_list.append(obj)
        return return_list
    
    """
    SERIVCES
    """
    def create_service(self,data):
        # return <Object>
        print "> Create alert service"
        return self._create(self.uri+'/api/services/',{'Content-Type':'application/json'},data)
    
    def update_service(self,data,id):
        # return <Object>
        print "> Update alert service"
        return self._update(self.uri+'/api/services/'+str(id)+'/',{'Content-Type':'application/json'},data)
    
    def delete_service(self,id):
        # return <Object>
        print "> Delete alert service"
        return self._delete(self.uri+'/api/services/'+str(id)+'/')
    
    def find_service(self,keyname):
        # return <List>
        obj_list = json.loads(self.find_all_objs('services').content)
        return_list = []
        for obj in obj_list:
            if keyname in obj["name"]:
                return_list.append(obj)
        return return_list    
    
    def find_exact_service(self,keyname):
        obj_list = json.loads(self.find_all_objs('services').content)
        return_list = []
        for obj in obj_list:
            if keyname == obj["name"]:
                return_list.append(obj)
        if len(return_list) > 1:
            print("There are duplicated services with the name '{}'".format(keyname))
            return None
        
        return return_list
    
    def check_and_create_service(self,data):
        if self.find_exact_service(data["name"]):
            print("Already exist a '{}' service. Exit without creating one.".format(data["name"]))
            return None
        else:
            return self.create_service(data)
    """
    UTILITY
    """
    def find_all_objs(self,tag):
        # return <Object>
        return self._collect(self.uri+'/api/'+tag+'/')

    def create_tenant_check(self, tenant_vanity_subdomain, check_name, data_in=None, verbose=False):
        tenant_check = self.cabot_check_template
        name = ".".join([self.environment, self.tenant_metric_prefix, tenant_vanity_subdomain, check_name])
        
        data = {
            "name": name,
            "metric": name,
            "frequency": 70
        }
        
        if data_in is not None:
            data.update(data_in)
        tenant_check.update(data)
        
        response = self.check_and_create_graphite_check(tenant_check)
        if response:        
            return response.json()
        else:
            return None
        
    # Create checks and return a list of check ids
    def create_all_tenant_checks(self, tenant_vanity_subdomain, data_in=None, verbose=False):
        ids = []
        for check_name in self.tenant_checks:
            # Create devices check but disable it.
            # We only need devices check for TOVs, not for tenants
            if check_name == 'devices':
                response = self.create_tenant_check(tenant_vanity_subdomain, check_name, data_in={"active": False}, verbose=verbose)
            else:
                response = self.create_tenant_check(tenant_vanity_subdomain, check_name, data_in=data_in, verbose=verbose)
            
            if response:
                ids.append(response["id"])
        # return ids of checks in order to add them to the tenant service
        return ids
    
    # find all checks of a specific tenant
    def find_all_tenant_checks(self, tenant_vanity_subdomain, verbose=False):
        tenant_checks = self.find_graphite_check(self.tenant_metric_prefix + "." + tenant_vanity_subdomain + ".")
        return tenant_checks
    
    def find_one_tenant_check(self, tenant_vanity_subdomain, check_name, verbose=False):
        tenant_checks = self.find_graphite_check(".".join([self.tenant_metric_prefix, tenant_vanity_subdomain, check_name]))
        if tenant_checks:
            return tenant_checks[0]
        else:
            return None
        
    # find all services of a specific tenant
    def find_tenant_service(self, tenant_vanity_subdomain, verbose=False):
        tenant_services = self.find_exact_service("[" + self.environment + "]" + " " + self.tenant_metric_prefix + "." + tenant_vanity_subdomain)
        if tenant_services:
            return tenant_services[0]
        else:
            print("Found 0 service.")
            return None
    
    def create_tenant_service(self, tenant_vanity_subdomain, status_checks, verbose=False): 
        tenant_service = self.cabot_service_template
        name = "[" + self.environment + "]" + " " + self.tenant_metric_prefix + "." + tenant_vanity_subdomain
        tenant_service.update({
            "name": name,
            "status_checks": status_checks
        })
        response = self.check_and_create_service(tenant_service)
        if response:
            return response.json()
        else:
            return None
        
    def delete_all_tenant_checks(self, tenant_vanity_subdomain, verbose=False):
        tenant_checks = self.find_all_tenant_checks(tenant_vanity_subdomain)
        for check in tenant_checks:
            response = self.delete_graphite_check(check["id"])
            if verbose:
                print(str("> Request-object: %s\n> Status-code: %s\n" % (check,response.status_code)))
    
    
    def delete_tenant_service(self, tenant_vanity_subdomain, verbose=False):
        service = self.find_tenant_service(tenant_vanity_subdomain)
        if service:
            response = self.delete_service(service["id"])
            if verbose:
                print(str("> Request-object: %s\n> Status-code: %s\n" % (service,response.status_code)))
    
    def create_tov_check(self, ov_instance_id, check_name, data_in=None, verbose=False):
        tov_check = self.cabot_check_template
        name = ".".join([self.environment, self.tov_metric_prefix, ov_instance_id, check_name])
        print(name)
        
        data = {
            "name": name,
            "metric": name,
            "frequency": 6
        }
        
        if data_in is not None:
            data.update(data_in)
        tov_check.update(data)
        
        response = self.check_and_create_graphite_check(tov_check)
        if response:
            return response.json()
        else:
            return None
    
    def find_all_tov_checks(self, ov_instance_id, verbose=False):
        tov_checks = self.find_graphite_check(self.tov_metric_prefix + "." + ov_instance_id)
        return tov_checks
    
    def find_one_tov_check(self, ov_instance_id, check_name, verbose=False):
        tov_checks = self.find_graphite_check(".".join([self.tov_metric_prefix, ov_instance_id, check_name]))
        return tov_checks[0]
        
    def delete_tov_check(self, ov_instance_id, check_name, verbose=False):
        try:
            tov_check = self.find_one_tov_check(ov_instance_id, check_name)
            response = self.delete_graphite_check(tov_check["id"])
            return response
        except Exception as e:
            print("[ERROR-cabot.delete_tov_check] {}".format(e))
    
    #add a list of check ids to a service
    def add_checks_to_service(self, check_ids, service_name):
        service = self.find_service(service_name)[0]
        data = {
            "name": str(service["name"]),
            "status_checks": check_ids + service["status_checks"]
        }
        response = self.update_service(data,service["id"])
        return response.json()
        
    def tov_check(self,keyname):
        # return <Boolean>, <String>
        # This method is used for checking existed TOV records
        # ------------------------------------------------------
        
        obj_list = self.find_graphite_check(keyname)
        if obj_list != []: 
            return False, "> Graphite Checks record found !"
        
        obj_list = self.find_ping_check(keyname)
        if obj_list != []:
            return False, "> IMCP Checks record found !"

        obj_list = self.find_service(keyname)
        if obj_list != []:
            return False, "> Services record found !"
        
        obj_list = self.find_instance(keyname)
        if obj_list != []: 
            return False, "> Instances records found !"
        
        return True, "No record for this TOV on Cabot"
        
    
    
    
        
    def tov_cleanup(self,keyname):
        # return <Boolean>
        # This method is used for cleaning all related Cabot opponents of specific TOV 
        # ------------------------------------------------------
        if keyname == "":
            raise ValueError("> Blank keyname is not allowed !")
        
        try:
            obj_list = self.find_graphite_check(keyname)
            if obj_list != []:
                for obj in obj_list:
                    del_req = self.delete_graphite_check(obj["id"])
                    print str("> Request-object: %s\n> Status-code: %s\n" % (obj,del_req.status_code))
            
            obj_list = self.find_ping_check(keyname)
            if obj_list != []:
                for obj in obj_list:
                    del_req = self.delete_ping_check(obj["id"])
                    print str("> Request-object: %s\n> Status-code: %s\n" % (obj,del_req.status_code))
            
            obj_list = self.find_service(keyname)
            if obj_list != []:
                for obj in obj_list:
                    del_req = self.delete_service(obj["id"])
                    print str("> Request-object: %s\n> Status-code: %s\n" % (obj,del_req.status_code))
            
            obj_list = self.find_instance(keyname)
            if obj_list != []:
                for obj in obj_list:
                    del_req = self.delete_instance(obj["id"])
                    print str("> Request-object: %s\n> Status-code: %s\n" % (obj,del_req.status_code))
            
            return True
            
        except Exception, e:
            print str(e)
            return False
    
    
    def tov_update(self,ov_id,domain=""):
        # return <Boolean>
        # This method is used for concurrent updating Cabot opponents which owned by specific TOV
        # ------------------------------------------------------
        if ov_id == "":
            raise ValueError("> Blank keyname is not allowed !")
        
        try:
            obj_list = self.find_graphite_check(ov_id)
            if obj_list != []:
                for obj in obj_list:
                    data = {"name":str(obj["name"]),"active":True}
                    req = self.update_graphite_check(data,obj["id"])
                    print str("> Request-object: %s\n> Status-code: %s\n> Response: %s\n" % (obj,req.status_code,req.content))
            
            obj_list = self.find_service(ov_id)
            if obj_list != []:
                for obj in obj_list:
                    data = {"name":str(obj["name"]),"alerts_enabled":True}
                    req = self.update_service(data,obj["id"])
                    print str("> Request-object: %s\n> Status-code: %s\n> Response: %s\n" % (obj,req.status_code,req.content))
            
            
            if domain != "":
                obj_list = self.find_instance(ov_id)
                if obj_list != []:
                    for obj in obj_list:
                        data = {"name":str(obj["name"]),"address":domain}
                        req = self.update_instance(data,obj["id"])
                        print str("> Request-object: %s\n> Status-code: %s\n> Response: %s\n" % (obj,req.status_code,req.content))
            
            
            
            obj_list = self.find_ping_check(ov_id)
            if obj_list != []:
                for obj in obj_list:
                    if self.run_check(obj["id"]).status_code == 200:  # Re-run check after updating Instance, else it will send alert email.
                        time.sleep(1.5)
                        data = {"name":str(obj["name"]),"active":True}
                        req = self.update_ping_check(data,obj["id"])
                        print str("> Request-object: %s\n> Status-code: %s\n> Response: %s\n" % (obj,req.status_code,req.content))
                    else:
                        print str("> [FAILED] \n    - Status-code: %s \nFailed to execute IMCP Check !" % (runchk.status_code))
            
            
            return True
        
        except Exception, e:
            print str(e)
            return False
        