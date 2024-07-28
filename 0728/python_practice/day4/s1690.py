import requests
from pprint import pprint as print

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]

dummy_data = [] #사용자 목록 --> dictionary 여러개 company ~ name
for i in range(1, 11):
    API_URL = 'https://jsonplaceholder.typicode.com/users/'+str(i)
    #응답 ㅂ다기

def censorship() : #이게 blacklist에 있는지 확인한다.
    pass     

def create_user():
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