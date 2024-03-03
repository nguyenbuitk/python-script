import requests 


base_url = 'https://restcountries.com/v3.1/'

'''
r = requests.get(base_url + 'all')
json_result = r.json()
print(json_result[84]['subregion'])
'''
'''
# filter resources
fields = {'fields' : 'altSpellings,name'}
r = requests.get(base_url + 'name/can', params=fields)
print(r.json())
'''

fields = {'fields': 'name,currencies'}
r = requests.get(base_url + 'capital/tokyo', params=fields)
print(r.json())