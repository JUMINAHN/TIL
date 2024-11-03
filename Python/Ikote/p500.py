#rest_api와 json 체험
#목킹 : 어떠한 기능이 있는것처럼 흉내내어 구현
#api중에서 가짜 회원 게시물에 대한 가짜 api기능을 제공해준다.

import requests
URL = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url=URL)
print(response) #현재는 응답코드만 나타난다.  #<Response [200]>

#response.을 찍으면 다양한 데이터 확인 가능
print(response.connection) #<requests.adapters.HTTPAdapter object at 0x000001C8D45D4BB0>
print(response.cookies) #<RequestsCookieJar[]>
print(response.request) #<PreparedRequest [GET]>
print(response.url) #https://jsonplaceholder.typicode.com/
print(response.history) #[]
print(response.json) #json ()호출 에러 ! => <bound method Response.json of <Response [200]>>

#디코드 에러 발생
# json() 메서드에 값이 없으면 ==> requests.exceptions.JSONDecodeError: Expecting value: line 2 column 1 (char 1)

#응답 data가 json형식이기 때문에 파이썬 객체로 변환
data = response.json() #python 형태로 바꿈
print(data)

#이름 정보만 삽입하기
#dictionary type 정보에 접근 => list내부에 하나하나의 객체
ex1 = data[0]['name'] #가져오기 => dictionary로
ex2 = data[0].get('name') #가져오기 => 객체로 
#상기값을 봤을떄 무엇이라도 가져오든 상관이 없다 => 방법 무관
print('---------')
print(ex1, ex2)

#따라서 모든 사용자의 객체 정보를 가져온다면?
user_list = []
for d in data: #data정보를 모두 돌면서
    name = d.get('name') #name 정보
    user_list.append(name)
print(user_list) #현재 api의 데이터 정보를 가져오는 방법