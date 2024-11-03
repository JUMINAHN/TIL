import json 

user = {
    'id' : 'gildong',
    'pw' : '192837',
    'age' : 30,
    'hobby' : ['football, programming'] #list 가능 
}

#python 변수를 json으로 변환
#인코딩  : 파이썬을 json으로 변환 
json_Data = json.dumps(user, indent=4) #띄어쓰기 4칸
print(json_Data) #user를 자체적인 json파일로 만드는 것 