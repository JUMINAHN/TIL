#디코딩
#json을 파이썬의 기본 자료형으로 변환
import json 

user = {
    'id' : 'gildong',
    'pw' : '192837',
    'age' : 30,
    'hobby' : ['football, programming'] #동일하게
}

#인코딩 : 파이썬 변수를 json으로 변환
json_data = json.dumps(user) #장애가 발생했을 떄, 프로그램의 오류 수정이나 데이터 검사를 위해. 그 상태

#디코딩 : json을 파이썬 변수로 변환
data = json.loads(json_data) #json data로드
print(data)