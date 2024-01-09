import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

import base64
import json
import os, sys, time

class St2ApiRequest(object):
    
    def __init__(self,env="test",cafile="",verbose=False):
        # Inital fields
        self.username = "None"
        self.password = "None"
        self.environment = env
        self.verbose = verbose
        self.hostname = str("https://st2.%s.myovcloud.com/" % (self.environment))
        
        #Processing fields
        self.token = "None"
        self.execution_id = ""
        self.session = requests.Session()
        
        #Preconfig
        adapter = HTTPAdapter(max_retries=Retry(connect=5, backoff_factor=1))
        self.session.mount('https://', adapter)
        
        if cafile == "":
            self.session.verify = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/certs/ca_bundle.pem"
        else:
            self.session.verify = cafile
    
    def check_connection(self):
        try:
            r = self.session.get(self.hostname,verify=True)
            if r.status_code != 200:
                print("Non-200 status !")
                return False
            return True
        except Exception, e:
            print(str(e))
            return False
    
    def authenticate(self,user,pwd):
        "Obtain authorization token"
        
        self.username = user
        self.password = pwd
        
        auth_str = 'Basic ' + St2ApiRequest.base64_encode(self.username,self.password)
        headers = {'Connection':'keep-alive',
                   'Accept-Encoding':'gzip, deflate',
                   'Content-Type':'application/json',
                   'Content-Length':'2',
                   'Authorization': auth_str
                  }
        data = '{}'
        
        url =  self.hostname + 'auth/v1/tokens'
        
        r = self.session.post(url,headers=headers,data=data,verify=True)
        
        if r.status_code != 201:
            print str("%s: %s"%(r.status_code,r.content))
            return None
        
        if self.verbose: print r.content
        self.token = str(json.loads(r.content)["token"])
        return self.token
        
        
    def action_check(self,action_str):
        "Get action info"
        
        if self.token == "None":
            print("Please authenticate first !")
            return {}
        
        headers = {'Connection':'keep-alive',
                   'Accept-Encoding':'gzip, deflate',
                   'Accept':'*/*',
                   'X-Auth-Token': self.token
                  }
        url = self.hostname + 'api/v1/actions/' + action_str
        
        r = self.session.get(url,headers=headers,verify=True)
        
        if r.status_code != 200:
            print str("%s: %s"%(r.status_code,r.content))
            return {}
        
        if self.verbose: print r.content
        return json.loads(r.content)
        
        
    def action_checkrun(self):
        "Trackback action status"
        
        if self.token == "None":
            print("Please authenticate first !")
            return {}
        
        headers = {'Connection':'keep-alive',
                   'Accept-Encoding':'gzip, deflate',
                   'Accept':'*/*',
                   'X-Auth-Token': self.token
                  }
        url = self.hostname + 'api/v1/executions/' + self.execution_id
        
        timer = 0
        while(1):
            # run it after action_execute
            r = json.loads(self.session.get(url,headers=headers,verify=True).content)
            
            if r["status"] == "running" or r["status"] == "scheduled" or r["status"] == "requested":
                pass
            elif r["status"] == "succeeded":
                print "ST2-checkrun: Succeeded"
                break
            elif r["status"] == "failed":
                print "ST2-checkrun: Failed"
                break
            else:
                print str("ST2-checkrun: Unknown status (%s)" % (r["status"]))
                break

            time.sleep(2)
            if timer > 10:
                break
            else:
                if self.verbose: print("ST2-checkrun: waiting for result...")
                timer=+1
        
        return r
    
    
    def action_execute(self,action_str,params,isString=False):
        "Execute action"
        
        if self.token == "None":
            print("Please authenticate first !")
            return {}
        #print("Before: \n", params)
        headers = {'Connection':'keep-alive',
                   'Accept-Encoding':'gzip, deflate',
                   'Accept':'*/*',
                   'Content-Type':'application/json',
                   'Content-Length':'70',
                   'X-Auth-Token': self.token
                  }
        if isString:
            data = '{"action": "'+action_str+'", "user": null, "parameters": '+ params +'}'
        else:
            data = '{"action": "'+action_str+'", "user": null, "parameters": '+str(params).replace("'","\"")+'}'
        #data = '{"action": "'+action_str+'", "user": null, "parameters": '+ '"' + str(params).replace("'","\"").replace("\"","\\\"")+'"}' 
        url = self.hostname + 'api/v1/executions'
        
        r = self.session.post(url,headers=headers,data=data,verify=True)
        
        if r.status_code != 201:
            print str("%s: %s \n%s"%(r.status_code,r.content,data))
            return {}
        
        self.execution_id = str(json.loads(r.content)["id"])
        
        if self.verbose: print r.content
        return json.loads(r.content)
        
    
    
    @staticmethod
    def base64_encode(username,password):
        return base64.b64encode(str("%s:%s" % (username,password)))