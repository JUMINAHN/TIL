number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people += 1
    return number_of_people

def create_user(**kwargs):
    result = kwargs['name']
    print(f'{result}님 환영합니다!') #대괄호를 사용하려면 {}을 한번 더 처리해야함
    print(kwargs)
    return print(f'현재 가입된 유저 수 : {number_of_people}')

print(f'현재 가입 된 유저 수 : {number_of_people}')
increase_user()
create_user(name = '홍길동', age = 30, address = '서울')

# number_of_people = 0


# # number_of_people이 증가해야한다.
# # name age address를 인자로받아서 user_ifo에 적절한 키값을 할당한다
# # 완성된 user_info dictionary를 반환한다
# def increase_user():
#     global number_of_people
#     number_of_people += 1
#     return number_of_people
    
# #호출되면 {name님} 환영합니다가 출력되어야 한다.
# # 결과를 출력하면 user_info 딕셔너리가 출력되어야 한다
# def create_user(**kwargs): #dictionary type이 되려면
#     #user_info 에 할당해라 
#     print(kwargs['name'])
#     #print(f'{kwargs[]}님 환영합니다!') #user에서 어떻게 가져오지 --> 매개변수의 키값을 어떻게 가져옴
#     return print(f'현재 가입된 유저 수 : {kwargs}')

# #인자로 전달함

# #키워드 인자값 -> dictionary
# create_user(name = '홍길동', age = 30, address = '서울') #user_info에 키값에 값을 할당한다
# #이거 자체가 dictionary이고

# #user info 딕셔너리 반환s