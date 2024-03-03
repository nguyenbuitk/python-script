import requests
payload = {'name' : 'Anthony', 'location' : 'Las Vegas'}
#r = requests.post('https://requestb.in/wpo4xjwp', data=payload)
#r = requests.post('https://enolzi8ie53r.x.pipedream.net/post', data=payload)
r = requests.post('https://httpbin.org/post',data=payload)
print(r.text)


'''
r = requests.get('https://httpbin.org/image/jpeg')
print(r.headers)

with open('image.jpg', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=500):
        fd.write(chunk)
'''

'''
r = requests.get('https://httpbin.org/status/501')

try:
    r.raise_for_status()
except requests.exceptions.HTTPError:
    print('ERROR! ERROR! ERROR!')

print(r)
'''

'''
try:
    r = requests.get('https://dsklfjdslfudsfdsj.com')
except requests.exceptions.ConnectionError:
    print('CONNECTION ERROR!')
'''

'''
try:
    r = requests.get('https://httpbin.org/delay/10', timeout=5)
except requests.exceptions.ReadTimeout:
    print('TIMED OUT!!!')
'''

from requests.auth import HTTPBasicAuth

r = requests.get('https://httpbin.org/basic-auth/anthony/secret', auth=HTTPBasicAuth('anthony', 'secret'))
print(r)