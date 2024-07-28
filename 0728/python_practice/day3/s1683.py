number_of_people = 0

def increase_user(): 
    global number_of_people
    number_of_people +=1

def create_user(name, age, address):
    user_info = {'name':name, 'age':age, 'address':address} 
    print(f'{name}님 환영합니다!')
    increase_user()
    return user_info

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

new_dict = {}
users = list(map(create_user, name, age, address)) #map 매개변수로 3개'
print(users)





# number_of_people = 0

# def increase_user(): 
#     global number_of_people
#     number_of_people +=1

# def create_user(name, age, address): #값 할당 방법
#     user_info = {'name':name, 'age':age, 'address':address}  #키 값에 값을 할당
#     #user_info = {}
#     #user_info['name'] = name
#     #user_info['age'] = age
#     #user_info['address'] = address
#     print(f'{name}님 환영합니다!')
#     increase_user()
#     return user_info

# name = ['김시습', '허균', '남영로', '임제', '박지원']
# age = [20, 16, 52, 36, 60]
# address = ['서울', '강릉', '조선', '나주', '한성부']


# users = 1 #수정
# print(users)

