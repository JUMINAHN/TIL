#set자료형 기본
my_set = {'가', '나', (0, 0)} 

#dict 자료형
my_dict = {
        '가': 1, 
        (0, 0): '튜플도 키값으로 사용가능'
    }

#my_set을 순회하여 얻은 값을 key로 하는 my dict의 value를 출력한다.
for ms in my_set:
    print(my_dict.get(ms)) #get은 값이 없을경우 None을 출력한다.

var = (1,2,3,'A')
#new_dict = {var : '변수로도 키 설정 가능'}
#my_dict.update(new_dict)
my_dict.setdefault(var, '변수로도 키 설정 가능')
print(my_dict)