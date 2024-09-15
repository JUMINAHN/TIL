import requests
from pprint import pprint as print

#총 1부터 10까지 10명의 데이터를 요청한다 range(1, 11) -> name을 dummy_data에 추가한다
dummy_data = []
for i in range(1, 11):
    API_URL = 'https://jsonplaceholder.typicode.com/users/'+str(i)
    response = requests.get(API_URL)
    parsed_data = response.json()
    #dictionary를 만들어야 함
    inner_info = {}
    if (float(parsed_data['address']['geo']['lat']) > -80 and float(parsed_data['address']['geo']['lat']) < 80) and (float(parsed_data['address']['geo']['lng']) > -80 and float(parsed_data['address']['geo']['lng']) < 80):
        dummy_data.append(inner_info)
        inner_info['company'] = parsed_data['company']['name']
        inner_info['lat'] = parsed_data['address']['geo']['lat']
        inner_info['lng'] = parsed_data['address']['geo']['lng']
        inner_info['name'] = parsed_data['name'] 

for data in dummy_data:
    print(data)


# dummy_data.append(inner_info)
# inner_info['company'] = parsed_data['company']['name']
# if float(parsed_data['address']['geo']['lat']) > -80 and float(parsed_data['address']['geo']['lat']) < 80:
#     inner_info['lat'] = parsed_data['address']['geo']['lat']
# if float(parsed_data['address']['geo']['lng']) > -80 and float(parsed_data['address']['geo']['lng']) < 80:
#     inner_info['lng'] = parsed_data['address']['geo']['lng'] 
# inner_info['name'] = parsed_data['name']    