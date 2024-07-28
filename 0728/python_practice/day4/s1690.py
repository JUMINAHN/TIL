import requests
from pprint import pprint as print

black_list = [ #얘네는 추가 하지 않고 제외한다.
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]

dummy_data = []
for i in range(1, 11):
    API_URL = 'https://jsonplaceholder.typicode.com/users/'+f'{i}'
    url = requests.get(API_URL)
    result = url.json()
    #dict로 
    new_dict = {'company': result['company']['name'], 'lat': result['address']['geo']['lat'], 'lng': result['address']['geo']['lng'], 'name': result['name']}
    if float(new_dict['lng']) < 80 and float(new_dict['lng']) > -80 and float(new_dict['lat']) < 80 and float(new_dict ['lat']) > -80:
        dummy_data.append(new_dict)


def censorship() : #이게 blacklist에 있는지 확인한다.
    pass     

def create_user(dummy_data): #사용자 목록을 인자로 넘겨 순회하는 코드
    censored_user_list = {dummy_data['company'] : list(dummy_data['name'])} #company이름을 key로 사용자 이름을 value는 list로 구성한다.
    pass

result = create_user(dummy_data)
print(result)






# black_list = [
#     'Hoeger LLC',
#     'Keebler LLC',
#     'Yost and Sons',
#     'Johns Group',
#     'Romaguera-Crona',
# ]

# dummy_data = [] #사용자 목록 --> dictionary 여러개 company ~ name
# for i in range(1, 11):
#     API_URL = 'https://jsonplaceholder.typicode.com/users/'+str(i)
#     #응답 ㅂ다기

# def censorship() : #이게 blacklist에 있는지 확인한다.
#     pass     

# def create_user():
#     pass



# result = create_user(dummy_data)
# print(result)