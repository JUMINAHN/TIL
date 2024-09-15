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

many_user = list(map(create_user, name, age, address)) #list 중 dictionary 여러개

number_of_book = 100
def decrease_book(number): 
    global number_of_book
    number_of_book -= number
    print(f'남은 책의 수 : {number_of_book}')

def rental_book(info): #info인자 하나만 할당 받을 수 있다(신규고객 이름, 나이 딕셔너리)
    decrease_book(number) #나이를 10으로 나눈 몫을 대여할 책의 수로 활용
    print(f'{name}님이 {number}권의 책을 대여하였습니다.')

print(many_user)
#many_user에서 address 제거 -> 키값을 제거하는 것,,
#remove는 요소 제거에요..
#name이랑 age만 뽑아올래요 -> 함수가 매개변수를 모두 받게 되었는데,, copy해야하나?
#pop메서드


# many_user
# def user_remove(many_user):
#     del many_user[address]
#     return many_user

# result = list(map(user_remove, many_user))
# print(result)

# #address key type 모두 제거해야함
# result = list(map(lambda many_user : many_user[address], many_user))
# #람다는 단일 표현식만 되기 떄문에 안됨 (del)




def default_arg_func(default='기본값'):
    return default

print(default_arg_func())
print(default_arg_func('다른 값'))