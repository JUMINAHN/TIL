class Dog:
    def __init__(self, sound) : #멍멍
        self.sound = sound

class Cat:
    def __init__(self, sound) :
        self.sound = sound # 야옹
    

class Pet(Dog, Cat):
    def __init__(self, sound):
        super().__init__(sound)

    def __str__(self) :
        return f'애완동물은 {self.sound} 소리를 냅니다.'
    

pet_1 = Pet("멍멍")
print(pet_1)
pet_2 = Pet("야옹")
print(pet_2)