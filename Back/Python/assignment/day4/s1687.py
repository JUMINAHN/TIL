import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users/1'
# API 요청
url = requests.get(API_URL)
# JSON -> dict 데이터 변환
result = url.json()

# 응답 데이터 출력
print(result)

# 변환 데이터 출력
print(type(result))
# 변환 데이터의 타입

print(result['name'])
print(result['username'])
print(result['company']['name'])
