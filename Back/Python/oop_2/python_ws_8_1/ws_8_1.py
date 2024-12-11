# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0 #클래스 속성 --> instancer가 생성될 때 animal의 num값이 증가되도록 

    def __init__(self) :
        Animal.num_of_animal += 1 #클래스 변수 접근

class Dog(Animal):
    def __init__(self):
        super().__init__()


class Cat(Animal):
    def __init__(self):
        super().__init__()


class Pet(Dog, Cat):
    def __init__(self):
        super().__init__()

    @classmethod
    def access_num_of_animal(cls): #classmethod -> cls
        return f'동물의 수는 {cls.num_of_animal}마리 입니다.'

dog = Dog()
print(Pet.access_num_of_animal())
cat = Cat()
print(Pet.access_num_of_animal())
