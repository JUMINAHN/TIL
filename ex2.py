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

result = list(map(create_user, name, age, address)) #얘네가 다 있으면 되겠네
print(result)
#print(create_user(name[0], age[0], address[0]))
#{'name': '김시습', 'age': 20, 'address': '서울'} -> 구조 --> 반복되면 됨 --> 리스트로