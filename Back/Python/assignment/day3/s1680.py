number_of_people = 0

def increase_user(): #함수 호출시 마다 +1 증가시키기
    global number_of_people
    number_of_people +=1
    print(f'현재 가입 된 유저 수 : {number_of_people}')
increase_user()





# number_of_people = 0

# def increase_user():
#     pass

# increase_user()