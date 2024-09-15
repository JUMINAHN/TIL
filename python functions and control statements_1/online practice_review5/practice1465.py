class Dog:
    sound = "멍멍" #클래스 속성
    def __init__(self) :
        pass
        

class Cat:
    sound = "야옹" #클래스 속성
    def __init__(self) :
        pass


class Pet(Dog,Cat): #str 매직 메서드 추가
    def __init__(self):
        super().__init__()

    def __str__(self) -> str: #인스턴스 생성 자체 --> 그 인스턴스 생성의 속성을 내려받은 것
        return f'애완동물은 {self.sound} 소리를 냅니다.'

pet = Pet()
print(pet)