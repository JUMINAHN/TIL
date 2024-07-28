number_of_book = 100

#global 사용
def decrease_book(number): #한번에 대여하는 책의 수를 정수로 넘겨받음
    #넘겨받은 값만큼 number_of_book의 수를 감소시키고, 현재 남은 책의 수를 출력
    global number_of_book
    number_of_book -= number
    print(f'남은 책의 수 : {number_of_book}')

#대여자의 이름과 대여하는 책의 수를 인자로#
def rental_book(name, number) :
    decrease_book(number)
    print(f'{name}님이 {number}권의 책을 대여하였습니다.')


#return 사용
# def decrease_book(number_of_book, number):
#     number_of_book -= number
#     print(f'남은 책의 수 : {number_of_book}')
#     return number_of_book

# def rental_book(number_of_book, name, number) :
#     decrease_book(number_of_book, number)
#     print(f'{name}님이 {number}권의 책을 대여하였습니다.')

# rental_book(number_of_book, '홍길동', 3)





# number_of_book = 100
# def decrease_book():
#     pass

# def rental_book() :
#     pass

# rental_book('홍길동', 3)