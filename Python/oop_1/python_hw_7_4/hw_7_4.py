# 아래 클래스를 수정하시오.
class Person: 
    number_of_people = 0 #클래스변수 증가

    def __init__(self, name, age) :
        self.name = name
        self.age = age
        Person.number_of_people += 1 #새로 만들 때 한 번 더 증가하느 것이니까 클래스 변수 증가(클래스에 접근)를 이곳에 한다

    def introduce(self) : #인스턴스 함수 사용할 때 self 까먹지 말기
        print(f'제 이름은 {self.name} 이고, 저는 {self.age} 살 입니다.')  #insatnce 메서드 내 변수 접근 --> 나의 변수
        


person1 = Person("Alice", 25)
person1.introduce() #instance 메서드 포함
print(Person.number_of_people) #인스턴스가 생성될때마다 증가하는 클래스 변수



# # 아래 클래스를 수정하시오.
# class Person:
#     pass


# person1 = Person("Alice", 25)
# person1.introduce()
# print(Person.number_of_people)