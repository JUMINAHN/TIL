number_of_people = 0

def increase_user(): 
    global number_of_people
    number_of_people +=1

def create_user(name, age, address): #값 할당 방법
    #user_info = {'name':name, 'age':age, 'address':address}  #키 값에 값을 할당
    user_info = {}
    user_info['name'] = name
    user_info['age'] = age
    user_info['address'] = address
    print(f'{name}님 환영합니다!')
    increase_user()
    return user_info

print(f'현재 가입 된 유저 수 : {number_of_people}')
result = create_user('홍길동', 30, '서울') #호출되면 메세지가 출력되어야 함
print(result) #dictionary 출력
print(f'현재 가입 된 유저 수 : {number_of_people}')





# number_of_people = 0

# def increase_user(): 
#     pass

# def create_user(): 
#     pass


# print()
# print(create_user('홍길동', 30, '서울'))
# print()
