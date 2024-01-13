'''
CHANGELOG:
2.1
 - add method convert_path_to_url
 - add method get_key_and_value_of_record
'''
import base64
import json
import validators
import requests
import re
import ast
from dao.utility import UtilityDAO as dao

class OvDns:
    """OV ETCD dns manage"""
    def __init__(self, env=None, url="", username="", password=""):
        if url != "":
            self.url = url
            self.credential = base64.b64encode(username + ":" + password) if username else ""
        else:
            if not env or env is None:
                raise ValueError("> ERR: \'Environment\' parameter is missing ! ")
            
            self.config = dao.getConfig(env)

            self.environment = env
            self.url = dao.fillEnv(self.environment,self.config["Dns"]["Url"])
            self.credential = base64.b64encode(self.config["Dns"]["Username"] + ":" + self.config["Dns"]["Password"]) if self.config["Dns"]["Username"] else ""

        self.conn = requests.session()

    def __generate_url(self, cname):
        return self.url + '/' + '/'.join(reversed(cname.split('.')))
    
    # convert /skydns/com/myovcloud/abc to 'abc.myovcloud.com'
    def convert_path_to_url(self, path):
        path_elements = filter(None, path.split('/'))
        # delete 'skydns' from the path
        del path_elements[0]
        
        url_elements = reversed(path_elements)
        url = '.'.join(url_elements)
        return url
        
    def is_exist(self, domain):
        """
        Check record is exist

        :param domain:
        :return:
        """
        url = self.__generate_url(domain)
        result = self.conn.get(url).json()

        return False if 'errorCode' in result else True
    
    def get_record(self, source):
        source = source.lower()
        
        if not validators.domain(source):
            raise ValueError('Invalid source domain name')
        
        url = self.__generate_url(source)
        
        result = self.conn.request('GET', url)

        return result.json()    
    
    def is_dir_record(self, source, raw=True):
        """
        Dir records occur when we add record with POST method instead of PUT (use case: acquire LetsEncrypt certifications with DNS verification)
        Dir_record:
            {
              "node": {
                "key": "/skydns/com/myovcloud/dev/activation",
                "dir": true,
                "nodes": [
                  {
                    "key": "/skydns/com/myovcloud/dev/activation/00000000000000014285",
                    "value": "{\"host\": \"18.221.2.70\"}"
                  }
                ]
              }
            }
        Normal record:
            {
              "node": {
                "key": "/skydns/com/myovcloud/dev/datapond",
                "value": "{\"host\": \"18.221.2.70\"}"
              }
            }
        Normal directory:
            {
              "node": {
                "key": "/skydns/com/myovcloud/dev/test2",
                "dir": true,
                "nodes": [
                  {
                    "key": "/skydns/com/myovcloud/dev/test2/ov",
                    "value": "{\"host\": \"1.1.1.1\"}"
                  }
                ]
              }
            }
        """
        if raw:
            record = source
        else:
            record = self.get_record(source)
        
        if (
            not 'value' in record['node'].keys()
            and 'nodes' in record['node'].keys()
            and record['node'].get('dir', None)
            and len(record['node']['nodes']) == 1
            and not record['node']['nodes'][0].get('dir', False)
            and re.search('^' + re.escape(str(record['node']['key'])) + '/' + r'(\d){20}$', str(record['node']['nodes'][0]['key']))):
            
            return True
        else:
            return False
    
    def get_key_and_value_of_record(self, source):
        raw_record = self.get_record(source)
        key = self.convert_path_to_url(raw_record['node']['key'])
        if self.is_dir_record(raw_record):
            value = ast.literal_eval(raw_record['node']['nodes'][0]['value'])['host']
        else:
            value = ast.literal_eval(raw_record['node']['value'])['host']
        return {'key': key, 'value': value}    
    
    def get_value(self, source):
        raw_record = self.get_record(source)
        if self.is_dir_record(raw_record):
            value = str(ast.literal_eval(raw_record['node']['nodes'][0]['value'])['host']).strip()
        else:
            value = str(ast.literal_eval(raw_record['node']['value'])['host']).strip()
        return value
        
    def add_record(self, source, dest):
        """
        Add or Update DNS record

        :param source:
        :param dest:
        :return:
        """
        # Convert to lowercase
        source = source.lower()
        dest = dest.lower()
        # Validation domain
        '''
        if not validators.domain(source):
            raise ValueError('Invalid source domain name')
        if not validators.ipv4(dest) and not validators.domain(dest):
            raise ValueError('Invalid destination domain name or IP address')
        '''
        url = self.__generate_url(source)

        params = {'value': json.dumps({"host": dest})}

        result = self.conn.request('PUT', url, params, headers={
            "Content-type": "application/x-www-form-urlencoded",
            'Authorization': 'Basic %s' % self.credential
        })

        return result.json()
    
    
    def add_record_v2(self, source, dest):
        
        record = self.get_record(source)
        if self.is_dir_record(record):
            params = {'value': json.dumps({"host": dest})}
            url = self.url + str(record['node']['nodes'][0]['key'])[7:]     # [0-6] = '/skydns'
            result = self.conn.request('PUT', url, params, headers={
                "Content-type": "application/x-www-form-urlencoded",
                'Authorization': 'Basic %s' % self.credential
            })
            return result.json()
        else:
            result = self.add_record(source, dest)
            return result
        
    def delete_record(self, domain, raw=False):
        """
        Delete DNS record

        :param domain:
        :return:
        """
        # Convert to lowercase
        domain = domain.lower()
        # Validation domain
        if not validators.domain(domain):
            raise ValueError('Invalid destination domain name')
        
        if raw is True:
            url = self.url + '/' +domain
        else:
            url = self.__generate_url(domain)
        print url
        
        result = self.conn.request("DELETE", url, headers={
            'Authorization': 'Basic %s' % self.credential
        })
        
        return result.json()

    @staticmethod
    def get_tov_env(fqdn):
        m = re.search('ovc\.(.*?)\.myovcloud', fqdn)

        return m.group(1) if m else ""

    @staticmethod
    def get_vpn_env(fqdn):
        m = re.search('vpn\.(.*?)\.myovcloud', fqdn)

        return m.group(1) if m else ""
