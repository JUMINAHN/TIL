import requests
from pprint import pprint as print

#총 1부터 10까지 10명의 데이터를 요청한다 range(1, 11) -> name을 dummy_data에 추가한다
dummy_data = []
for i in range(1, 11):
    API_URL = 'https://jsonplaceholder.typicode.com/users/'+str(i)
    response = requests.get(API_URL)
    parsed_data = response.json()
    dummy_data.append(parsed_data['name'])

for i in dummy_data:
    print(i)


