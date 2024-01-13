import json
import os.path
import requests


class DataPond(object):
    """Util class contain helpful function operate with OV DataPond"""

    def __init__(self, url="", appId="", username="", password="", verbose=False):
        
        self.token = ""
        self.verbose = verbose
        
        self.url = url + "/parse"
        self.appId = appId
        self.username = username
        self.password = password
        
        self.conn = requests.Session()
        self.conn.verify = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/certs/cacert.pem"

    def login(self,authMethod='basic'):
        
        if authMethod == 'basic':
            result = self.conn.request('GET', self.url + '/login',
                headers={
                    "X-Parse-Application-Id": self.appId,
                    "X-Parse-Revocable-Session": "1"
                },
                params={
                    "username": self.username,
                    "password": self.password
            })
        elif authMethod == 'ldap':
            authData = {
                "authData":{
                  "ldap":{
                    "id": self.username,
                    "password": self.password
                }}}
            
            result = self.conn.request('POST', self.url + '/users',
                headers={
                    "X-Parse-Application-Id": self.appId,
                    "X-Parse-Revocable-Session": "1",
                    "Content-Type": "application/json"
                },
                json=authData)
        else:
            raise ValueError("> This auth method is not supported !")
        
        if self.verbose:
            print ("Login to %s. Result: %s" % (self.url, result.text))
        result = result.json()

        if "sessionToken" not in result:
            return False
        self.token = str(result['sessionToken'])
        return True

    def logout(self):
        result = self.conn.request('POST', self.url + '/logout',
                                   headers={
                                       "X-Parse-Application-Id": self.appId,
                                       "X-Parse-Session-Token": self.token
                                   })

        if self.verbose:
            print ("Logout Result: " + result.text)
        return True if result.text == "{}" else False

    def find_all(self, table, query=None, option=None):
        params = {'where': json.dumps(query)}

        uri = self.url + '/classes/' + table

        if option:
            params.update(option)
        else:
            params.update({"order":"objectId","limit":100000})

        result = self.conn.request('GET', uri,
                                   headers={
                                       "X-Parse-Application-Id": self.appId,
                                       "X-Parse-Session-Token": self.token
                                   },
                                   params=params)
        if self.verbose:
            print ("Query Result: " + result.text)
        result = result.json()
        return result['results'] if "results" in result else {}

    def find_one(self, table, query=None):
        result = self.find_all(table, query, {"limit": 1})

        if not result:
            return {}

        return result[0] if result[0] else {}

    def get_id(self, table, query=None):
        result = self.find_one(table, query)

        return str(result['objectId']) if "objectId" in result else ""

    def create(self, payload, table):
        uri = self.url + '/classes/' + table

        result = self.conn.request('POST', uri, json=payload, headers={
            "X-Parse-Application-Id": self.appId,
            "X-Parse-Session-Token": self.token,
            "Content-Type": "application/json",
        })

        if self.verbose:
            print ("Create: " + result.text)
        result = result.json()

        return result["objectId"] if "objectId" in result else ""

    def update(self, objectId, payload, table):
        uri = self.url + '/classes/' + table + '/' + objectId

        result = self.conn.request('PUT', uri, json=payload, headers={
            "X-Parse-Application-Id": self.appId,
            "X-Parse-Session-Token": self.token,
            "Content-Type": "application/json",
        })

        if self.verbose:
            print ("Update: " + result.text)
        result = result.json()

        return True if "updatedAt" in result else False

    def delete(self, objectId, table):
        uri = self.url + '/classes/' + table + '/' + objectId

        result = self.conn.request('DELETE', uri, headers={
            "X-Parse-Application-Id": self.appId,
            "X-Parse-Session-Token": self.token,
            "Content-Type": "application/json",
        })

        if self.verbose:
            print ("Delete: " + result.text)
        return True if result.text == "{}" else False
