import requests

payload = {'name' : 'Anthony', 'job' : 'Programmer'}
r = requests.post('https://enolzi8ie53r.x.pipedream.net/api/users', json=payload)
print(r)
print(r.text)
print(r.json())