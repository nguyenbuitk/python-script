import os, sys
import socket
from subprocess import call, check_output
from dao.utility import UtilityDAO as dao

class Graphite(object):
    
    # mode=st2: run on stackstorm; mode=manual: run manually on local VM; mode=lambda: run on AWS Lambda
    def __init__(self, env=None, mode="st2", verbose=False):
        
        self.verbose = verbose
        if env is None:
            raise ValueError("> ERR: \'Environment\' parameter is missing ! ")
        
        self.environment = env
        if mode == "manual":
            #Get configs
            try:
               
                self.configs = dao.getConfig(env)                        
                self.ssh_key = self.configs["Cabot"]["SSH_Key"]
                self.ssh_user = self.configs["Cabot"]["SSH_User"]
                self.ssh_address = dao.fillEnv(self.environment,self.configs["Cabot"]["Hostname"])
                self.graphite_port = self.configs["Cabot"]["Port"]
                '''
                self.graphite_port = graphite_configs["port"]
                self.tov_metric_prefix = graphite_configs["tov_metric_prefix"]
                self.tenant_metric_prefix = graphite_configs["tenant_metric_prefix"]
                self.whisper_dir = graphite_configs["whisper_dir"]
                self.tenant_checks = configs.get("monitoring")["tenant_checks"]
                '''
            except ImportError:
                pass
        elif mode == "st2" or mode == "lambda":
            try:
                from lib import OvConfig
                configs = OvConfig(mode=mode)
                graphite_configs = configs.get("monitoring")["graphite"]
                #self.ssh_key = graphite_configs["ssh_key_path"]
                #self.ssh_user = graphite_configs["ssh_user"]
                self.ssh_address = graphite_configs["address"]
                self.graphite_port = graphite_configs["port"]
                self.tov_metric_prefix = graphite_configs["tov_metric_prefix"]
                self.tenant_metric_prefix = graphite_configs["tenant_metric_prefix"]
                self.whisper_dir = graphite_configs["whisper_dir"]          
            except Exception as e:
                print("[ERROR-graphite-init] {}".format(e))
                print(mode)
        elif mode == "default":
            try:
                self.configs = dao.getConfig(env)   
                self.ssh_address = dao.fillEnv(self.environment,self.configs["Gaphite"]["Url"])
                self.graphite_port = self.configs["Gaphite"]["Port"]
            except Exception as e:
                print("[ERROR-graphite-init] {}".format(e))
                print(mode)
        self.graphite_address = self.ssh_address
        
        #self.docker_container_name = self.getContainerName()
    '''   
    def getContainerName(self):
        self.docker_container_name = check_output("ssh -o StrictHostKeyChecking=no -i "+self.ssh_key+" "+self.ssh_user+"@"+self.ssh_address+" docker ps | grep r-graphite-m-graphite | awk '{print $NF}'",shell=True).decode().strip('\n')
        if self.verbose:
            print("> Get container: %s" % self.docker_container_name)
        return self.docker_container_name
    
    def removeMetric(self,tov_id,container=""):
        if container == "":
            container = self.docker_container_name
        
        output = str(check_output("ssh -o StrictHostKeyChecking=no -i "+self.ssh_key+" "+self.ssh_user+"@"+self.ssh_address+" \'docker exec -i "+container+" sh -c \"rm -rf /opt/graphite/storage/whisper/"+self.environment+"/infra/tov/"+tov_id+" \" && echo \"> Executing...\" \' ",shell=True).decode().strip('\n'))
        checker = str("\nError-status: %s (expected: 0)" % check_output("ssh -o StrictHostKeyChecking=no -i "+self.ssh_key+" "+self.ssh_user+"@"+self.ssh_address+" \'docker exec -i "+container+" sh -c \"ls -la /opt/graphite/storage/whisper/"+self.environment+"/infra/tov/ \"\'",shell=True))
        
        if tov_id in checker:
            output+="[Error] This record still not be removed in Graphite!"
        else:
            output+=str("[OK] Remove Graphite-metric for %s successfully!" % tov_id)
        return output
    
    # The removeMetric function only supports tov metrics. Now we also need to monitor tenants and VPNs
    # metric_path could be: 
    #   "infra/tov/ov_instance_id"
    def remove_metric(self, metric_prefix, metric_id, verbose=False):
    
        metric_absolute_path = "/".join([self.whisper_dir ,self.environment, metric_prefix, metric_id])
        #print(metric_absolute_path)
        metric_parent_dir = os.path.dirname(metric_absolute_path)
        container = self.docker_container_name
        
        output = str(check_output(
            "ssh -o StrictHostKeyChecking=no -i " + self.ssh_key + " " + self.ssh_user + "@" + self.ssh_address +
            " \'docker exec -i " + container +
            " sh -c \"rm -rf " + metric_absolute_path +
            " \" && echo \"> Executing...\" \' "
            ,shell=True
        ).decode().strip('\n'))
        
        checker = str("\nError-status: %s (expected: 0)" % check_output(
            "ssh -o StrictHostKeyChecking=no -i " + self.ssh_key + " " + self.ssh_user + "@" + self.ssh_address +
            " \'docker exec -i " + container + " sh -c \"ls -la " + metric_parent_dir
            + " \"\'",shell=True
        ))
        
        if metric_id in checker:
            output += "[Error] This record still not be removed in Graphite!"
        else:
            output += str("[OK] Remove Graphite-metric for %s successfully!" % metric_id)
        return output
    
    def remove_tov_metric(self, ov_instance_id, verbose=False):
        output = self.remove_metric(self.tov_metric_prefix, ov_instance_id)
        return output
        
    def remove_tenant_metric(self, tenant_vanity_subdomain, verbose=False):    
        output = self.remove_metric( self.tenant_metric_prefix, tenant_vanity_subdomain)
        return output
    '''
    
    def netcat(self, hostname, port, content):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((hostname, port))
        s.sendall(content.encode())
        s.shutdown(socket.SHUT_WR)
        s.setblocking(False)
        s.close()
       
    # data = {"metric_path": "dir/id", "value": 123456, "timestamp": 123123123}
    def send_data(self, data, verbose=False):
        path = self.environment + "/" + data["metric_path"]
        output= self.netcat(self.graphite_address, int(self.graphite_port), '{} {} {}\n'.format(path, data["value"], data["timestamp"]))
        '''
        cmd = "echo \"{} {} {}\" | nc {} {}".format(
            path, data["value"], data["timestamp"], self.graphite_address, self.graphite_port
        )                
        output = check_output(cmd, shell=True)
        '''
        return output
        
    def send_tov_data(self, data, verbose=False):
        data["metric_path"] = self.tov_metric_prefix + "/" + data["id"]
        output = self.send_data(data)
        return output
        
    # data = {"id": tenant_vanity_subdomain/check_name, "value": 123456, "timestamp": 123123123}
    def send_tenant_data(self, data, verbose=False):
        data["metric_path"] = self.tenant_metric_prefix + "/" + data["id"]
        output = self.send_data(data)
        return output
        
    def listTov(self,container=""):
        """
        Return type: list()
        """
        if container == "":
            container = self.docker_container_name
        
        output = check_output("ssh -o StrictHostKeyChecking=no -i "+self.ssh_key+" "+self.ssh_user+"@"+self.ssh_address+" \'docker exec -i "+container+" sh -c \"ls /opt/graphite/storage/whisper/"+self.environment+"/infra/tov/\"\' ",shell=True).decode().strip()
        return output.split("\n")
     