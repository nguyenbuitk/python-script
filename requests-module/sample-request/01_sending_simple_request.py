import requests
r = requests.get('https://reqres.in/api/users/2')
print(r.text) # ouput is string with double qoute ("")
json_data = r.json() # output is json
print(json_data['data']['first_name'])