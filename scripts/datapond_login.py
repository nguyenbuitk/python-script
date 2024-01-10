import requests
import json

# Parse server URL and login endpoint
parse_server_url = 'https://datapond.dev.myovcloud.com:1337/parse/'
login_endpoint = parse_server_url + 'login'  # Adjust if the login endpoint differs

# Credentials
username = 'OV'
password = 'Bugaboo-Tecta-Fraud-Atom'

# Headers
headers = {
    'X-Parse-Application-Id': 'dataPond',  # Replace with your Parse Application ID
    'Content-Type': 'application/json'
}
print(login_endpoint)
# Login request
response = requests.get(login_endpoint, headers=headers, params={'username': username, 'password': password}, verify=False)
# Warn about insecure request
print(response.text)
if response.status_code == 200:
    print("Login successful")
else:
    print("Login failed")