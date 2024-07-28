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


def censorship(dummy) :#blacklist 유무 확인하기 -> 전달받은 company, name 기반
    if dummy['company'] in black_list:
        print(f'{dummy["company"]} 소속의 {dummy["name"]} 은/는 등록할 수 없습니다.')
        return False
    else:
        print('이상 없습니다.')
        return True
    
        

def create_user(dummy_data): 
    #순회하여 company 이름을 key로, 사용자이름을 value(리스트)로 가지는 dict 생성
    #순회하면서 각 사용자 정보를 censorship함수에 넘겨서 balcklist에 포함되어있는지 확인
    censored_user_list = {}
    for dummy in dummy_data: #dummy안에 한가지 리스트가 있을 것
        result = censorship(dummy)
        if result :
            censored_user_list.setdefault(dummy['company'], [dummy['name']])
    return censored_user_list


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