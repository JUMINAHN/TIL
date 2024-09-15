#set자료형 기본
my_set = {'가', '나', (0, 0)} 

#dict 자료형
my_dict = {
        '가': 1, 
        (0, 0): '튜플도 키값으로 사용가능'
    }

for my in my_set:
    print(my_dict.get(my)) #자체적으로 get은 반환할 값이 없으면 None 만듬

var = (1,2,3,'A')
my_dict.setdefault(var, '변수로도 키 설정 가능')
print(my_dict) #dict자체가 순서가 정함이 있는게 아니라 해시를 기반으로 이루어지기 때문에 내용물이 바뀜
# 나중에 update도 활용해볼 것