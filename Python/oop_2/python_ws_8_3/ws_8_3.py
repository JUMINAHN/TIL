# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0 #클래스 속성 --> instancer가 생성될 때 animal의 num값이 증가되도록 

    def __init__(self) :
        Animal.num_of_animal += 1 #클래스 변수 접근

class Cat(Animal):
    def __init__(self, sound):
        super().__init__()
        self.sound = sound
    
    def meow(slef) :
        print(f'{slef.sound} !')

 

cat1 = Cat("야옹")
cat1.meow()


# class Cat:
#     pass


# cat1 = Cat("야옹")
# cat1.meow()
