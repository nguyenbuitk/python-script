import json
import os.path
import requests
import logging
import functools
from urlparse import urljoin
from functools import wraps

#decorator for lazy login
def login_datapond(func):
    @wraps(func)
    def wrapper(*args):
        args[0].login()
        return func(*args)
    return wrapper

class DataPond(object):
    """Util class contain helpful function to operate with OV DataPond"""

    DATA_LIMIT = 10000

    def __init__(self, url="", appId="dataPond", username="", password="", verbose=False):
        self.logger = logging.getLogger(__name__)
        self.token = ""
        
        self.url = url
        self.appId = appId
        self.username = username
        self.password = password
        
        self.conn = requests.Session()
        self.conn.verify = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/certs/cacert.pem"
        self.conn.headers['X-Parse-Application-Id'] = self.appId

    def __del__(self):
        if(self.token != ""):
            self.__logout()

    def login(self):
        if(self.token != ""):
            self.logger.debug("Already logined to datapond")
            return

        self.logger.debug("Login to %s", self.url)

        result = self.conn.get(urljoin(self.url, '/parse/login'),
                                   params={
                                       "username": self.username,
                                       "password": self.password
                                   })
        
        if(result.status_code == 200):
            self.logger.debug("Result: %s", self.__dumpJson(result.json()))
        else:
            self.logger.debug("Result: %s", result.text)
        
        result = result.json()

        if "sessionToken" not in result:
            raise Exception("Cannot login DataPond {}".format(self.url)) 

        self.token = str(result['sessionToken'])
        # store session token to header of session
        self.conn.headers['X-Parse-Session-Token'] = self.token

    def __logout(self):
        self.logger.debug("Logout from %s", self.url)

        result = self.conn.post(urljoin(self.url, '/parse/logout'))

        self.logger.debug("Result: %s", result.text)

    def __dumpJson(self,data):
        return json.dumps(data, indent=4, sort_keys=True)

    @login_datapond
    def query(self, table, query=None, option=None):
        """query data
            refer to this page https://docs.parseplatform.org/rest/guide/#basic-queries

        """

        url = urljoin(self.url, '/parse/classes/{}'.format(table))

        params = {}
        if(query is not None):
            params = {'where': json.dumps(query)}

        if option:
            params.update(option)
        else:
            params.update({"order":"objectId","limit":DataPond.DATA_LIMIT})

        result = self.conn.get(url, params=params)
        self.logger.debug("Query Result: %s", result.text)

        result = result.json()
        return result['results'] if "results" in result else {}

    def find_all(self, table, query=None, option=None):
        return query(table, query, option)

    def find_one(self, table, query=None):
        result = self.find_all(table, query, {"limit": 1})

        if not result:
            return {}

        return result[0] if result[0] else {}

    def get_id(self, table, query=None):
        result = self.find_one(table, query)

        return str(result['objectId']) if "objectId" in result else ""

    @login_datapond
    def create(self, payload, table):
        url = urljoin(self.url, '/parse/classes/{}'.format(table))

        result = self.conn.post(url, json=payload, headers={"Content-Type": "application/json"})
        self.logger.debug("Result: %s", result.text)

        result = result.json()
        return result["objectId"] if "objectId" in result else ""

    @login_datapond
    def update(self, objectId, payload, table):
        url = urljoin(self.url, '/parse/classes/{}/{}'.format(table, objectId))

        result = self.conn.put(url, json=payload, headers={"Content-Type": "application/json"})
        self.logger.debug("Result: %s", result.text)

        result = result.json()
        return True if "updatedAt" in result else False

    @login_datapond
    def delete(self, objectId, table):
        url = urljoin(self.url, '/parse/classes/{}/{}'.format(table, objectId))

        result = self.conn.delete(url)
        self.logger.debug("Result: %s", result.text)
        
        return True if result.text == "{}" else False