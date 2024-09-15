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

class Cat(Animal):
    def __init__(self, sound):
        super().__init__()
        self.sound = sound
    
    def meow(self) :
        print('야옹 !')

class Pet(Cat, Dog):
    def __init__(self, sound):
        super().__init__(sound)

    def make_sound(self) :
        print(self.sound)

    def play(self):
        print('애완동물과 놀기')

pet1 = Pet("그르르")
pet1.make_sound()
pet1.bark()
pet1.meow()
pet1.play()


# 아래 클래스를 수정하시오.
# class Pet:
#     pass

# pet1 = Pet("그르르")
# pet1.make_sound()
# pet1.bark()
# pet1.meow()
# pet1.play()
