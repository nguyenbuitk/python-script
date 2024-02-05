import requests

try:
    r = requests.get('https://httpbin.org/delay/10', timeout=3)
except requests.exceptions.ReadTimeout:
    print('TIME OUT!!!')