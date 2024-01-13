import collections
import os.path
import fileinput

class AgentDAO:
    def __init__(self, path="/opt/ovcloud/ov_data"):
        self.__config = collections.OrderedDict()
        self.path = path
        #self.__config["dp_host_data"] = "https://datapond.dev.myovcloud.com:1337"
        #self.__config["fixed_ip"] = "143.209.0.2"
        
        if os.path.isfile(path):
            with open(path) as myfile:
                for line in myfile:
                    name, var = line.partition("=")[::2]
                    self.__config[name.strip()] = str(var).strip()
    
    def get(self, key):
        if key not in self.__config:
            return None
        return self.__config[key]
    
    def set(self,key,value):
        f = fileinput.input(files=(self.path),inplace=True, backup='.bak')  #Backup
        for line in f:
            if line.startswith(key+"="):
                old_value = line
                new_value = key+'='+value
                print(line.replace(old_value,new_value).strip())
            else:
                print(line.strip())
        f.close()
