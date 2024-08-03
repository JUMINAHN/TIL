number_of_people = 0

def increase_user(): 
    global number_of_people
    number_of_people += 1
    return number_of_people 

def create_user(name, age, address):
    increase_user()
    user_info = {}
    user_info['name'] = name 
    user_info['age'] = age
    user_info['address'] = address
    print(f'{name}님 환영합니다!')
    return user_info


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


# create_user(name[0], age[0], address[0])
# create_user(name[1], age[1], address[1])
# create_user(name[2], age[2], address[2])
# create_user(name[3], age[3], address[3])
# create_user(name[4], age[4], address[4])
users = list(map(create_user, name, age, address))
print(users)
