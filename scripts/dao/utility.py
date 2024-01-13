import collections
import os
import fileinput
import json

class UtilityDAO:
      
    @staticmethod
    def getConfig(env,path=""):
        if path == "":
            # DEFAULT: ../cfg/config.<env>.json
            path = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))),"cfg","config."+env+".json")
            print ("    -- Get configs from: "+ path)
        
        try:
            formatCheck = path.split(".")
            if formatCheck[-1] == "json":
                configs = UtilityDAO.readJSON(path)
            else:
                configs = UtilityDAO.readOvData(path)
            
        except IOError:
            raise ValueError("> Configuration file not found ! ("+path+")")
        #except Exception, e:
        #    raise ValueError(str("%s \n%s") % ("> Something goes wrong in Configuration file !",str(e)))
        
        return configs
    
    @staticmethod
    def readJSON(_path):
        config = {}
        with open(_path,"r+") as file:
            config=json.loads(file.read())
        return config
    
    @staticmethod
    def readOvData(_path):
        config = {}
        file = open(_path, 'r+')
        file.seek(0)
        for line in file.readlines():
            if '=' not in line:
                continue
            val = line.split("=")
            config.update({val[0].rstrip():val[1].rstrip()})
        file.close()
        return config
    
    @staticmethod
    def fillEnv(env,url):
        return url.replace("{Env}",env)

    @staticmethod
    def get_secret(filename):
        config = UtilityDAO.getConfig("prod")
        secret_path = config['secret_path']
        return open(secret_path + '/' + filename,'rb').read().strip()
