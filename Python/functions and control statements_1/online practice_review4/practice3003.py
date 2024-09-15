class Car:
    wheels = 4
    def __init__(self, engine, driving_system, sound) :
        self.engine = engine
        self.driving_system = driving_system
        self.sound = sound
    
    def drive(self) : #인스턴스 메서드
        print(self.sound)
        return self.engine

    def introduce(self):
        print(f'제 차의 엔진은 {self.engine} 방식이고, {self.driving_system} (으)로 동작합니다.')
    
    @classmethod
    def increase_wheels(cls): #cls 메서드는 -> cls 선언 및 `classmethod` 표기
        cls.wheels += 1 #cls를 통해 클래스 변수에 접근
        print('법이 개정되어 모든 자동차의 필요 바퀴 수가 1증가 하였습니다')
    
    @staticmethod
    def description() :
        print('자동차는 엔진에서 만든 동력을 바퀴에 전달하여 지상에서 승객이나 화물을 운반하는 교통 수단')


car1 = Car('gasoline', '후륜구동', '부릉부릉')
car2 = Car('diesel', '전륜구동', '달달달달')
car3 = Car('hybrid', '4wd', '슈웅')

car1.drive()
print(car2.drive())

print('===')
car1.introduce()
car3.introduce()

print('===')
print(f'이 세상의 자동차는 {Car.wheels}개의 바퀴를 가집니다.')
Car.increase_wheels()
print(f'이 세상의 자동차는 {Car.wheels}개의 바퀴를 가집니다.')
Car.description()