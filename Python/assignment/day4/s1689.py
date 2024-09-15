import requests
from pprint import pprint as print

dummy_data = []
for i in range(1, 11):
    API_URL = 'https://jsonplaceholder.typicode.com/users/'+f'{i}'
    url = requests.get(API_URL)
    result = url.json()
    #dict로 
    new_dict = {'company': result['company']['name'], 'lat': result['address']['geo']['lat'], 'lng': result['address']['geo']['lng'], 'name': result['name']}
    if float(new_dict['lng']) < 80 and float(new_dict['lng']) > -80 and float(new_dict['lat']) < 80 and float(new_dict ['lat']) > -80:
        dummy_data.append(new_dict)

print(dummy_data)