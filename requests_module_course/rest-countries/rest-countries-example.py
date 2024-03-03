import requests
from pprint import pprint
base_url = 'https://restcountries.com/v3.1/'
print('What information do you want about a country? Choose one.')
print('1. Population')
print('2. Languages')
print('3. Timezone')
option = input('')
country = input('What country do you want that information for? ')

params = {'fields' : 'population,languages,timezones', 'fullText': 'true'}
r = requests.get(base_url + 'name/{}'.format(country))

json_response = r.json()
country = None

try:
    country = json_response[0]
except KeyError:
    print('Country Not Found')

# pprint(country)
if country:
    if option == '1':
        population = country['population']
        print("Population is {}. ".format(population))

    elif option == '2':
        for key, value in country['languages'].items():
            print(f"The language are {key}: {value}")
    else:
        print('The timezones are: {}.'.format(', '.join(country['timezones'])))