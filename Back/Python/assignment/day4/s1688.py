import requests
from pprint import pprint as print

dummy_data = []
for i in range(1, 11):
    API_URL = 'https://jsonplaceholder.typicode.com/users/'+f'{i}'
    url = requests.get(API_URL)
    result = url.json()
    dummy_data.append(result['name'])

print(dummy_data)