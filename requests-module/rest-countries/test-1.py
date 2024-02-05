import requests
base_url = 'https://restcountries.com/v3.1/'
r = requests.get(base_url + 'all')

json_result = r.json()
print(json_result)