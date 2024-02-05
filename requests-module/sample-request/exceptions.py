import requests
r = requests.get('https://httpbin.org/status/404')

try:
    r.raise_for_status()
except requests.exceptions.HTTPError:
    print('ERROR!')
print(r)