# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0 #클래스 속성 --> instancer가 생성될 때 animal의 num값이 증가되도록 

    def __init__(self) :
        Animal.num_of_animal += 1 #클래스 변수 접근

class Dog(Animal):
    def __init__(self):
        super().__init__()

    def bark(self) :
        print('멍멍!')

dog1 = Dog()
dog1.bark()


# 아래 클래스를 수정하시오.
# class Dog:
#     pass

# dog1 = Dog()
# dog1.bark()