def rental_book(name, number): #대여자의 이름과 대여하는 책의 수를 인자
    decrease_book(number)
    print(f'{name}님이 {number}권의 책을 대여하였습니다.')

number_of_book = 100

def decrease_book(number): 
    global number_of_book
    number_of_book -= number
    print(f'남은 책의 수 : {number_of_book}')


rental_book('홍길동', 3)