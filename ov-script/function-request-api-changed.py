import requests
import json
from time import sleep

def requestAPI(url, headers, data=None, method='GET'):
    max_retries = 3
    retry_interval = 5
    timeout = 15

    for retry_count in range(max_retries):
        try:
            response = requests.request(method, url, headers=headers, data=data, timeout=timeout)
            if response.status_code == 200:
                return response
            else:
                raise Exception(response)
        except Exception as e:
            if retry_count == max_retries - 1:
                raise e
            print(f"Retrying Request API ... Attempt {retry_count+1}/{max_retries}")
            sleep(retry_interval)


def main():
    url = 'https://sqa-sca.manage.ovcirrus.com/api/user/signin'
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({
        'email': 'abc',
        'password': 'xyz'
        })
    try:
        response = requestAPI(url, headers, data, "POST")
        print("Response: ", response.text)
    except Exception as e:
        print("Error: ", e)

if __name__ == "__main__":
    main()
