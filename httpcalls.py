import requests
import config
import pprint

pp = pprint.PrettyPrinter(indent=2)

baseUrl = config.get('weatherbit#url')
accessKey = config.get('weatherbit#accesskey')

currentWeaterResponse = requests.get(
    url=baseUrl + '/current?postal_code=08043&key=' + accessKey)
#pp.pprint(currentWeaterResponse.json())

currentWeater = currentWeaterResponse.json()

print('Current weather in', currentWeater['data'][0]['city_name'], 'is',
      currentWeater['data'][0]['weather']['description'])

x = requests.get(url=baseUrl +
                 '/forecast/daily?postal_code=08043&days=1&key=' + accessKey)

#pp.pprint(x.json())