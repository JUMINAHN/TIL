# 아래 클래스를 수정하시오.
class Person:
    number_of_people = 0

    #인스턴스를 만들때마다 number_of_people이 증가해야하기 떄문에 -> 초기값, 생성자에 넣는다.
    def __init__(self, name, age) : #self는 생성자를 만들때 무조건 있어야 하는 키워드 -> 인스턴스를 만들기 위함
        self.name = name
        self.age = age
        Person.number_of_people += 1 #class 변수이기 때문에 class 자체에 접근해야 한다.
       
    def introduce(self): #instance method 사용을 위해서는 self 키워드를 기능에도 넣어줘야 함
        print(f'제 이름은 {self.name} 이고, 저는 {self.age} 살 입니다.')
        #인스턴스 메서드를 호출했기 때문에, 인스턴스 변수 자체에 접근하는 키워드를 만든다.

person1 = Person("Alice", 25)
person1.introduce()
print(Person.number_of_people)