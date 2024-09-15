
#Myth 클래스의 type_of_myth 출력
#description 스태틱 메서드 호출

class Myth():
    type_of_myth = 0

    def __init__(self, name) :
        self.name = name #내 자신에게 할당
        Myth.type_of_myth += 1 #클래스 변수에 접근하기 위해선 클래스 이름만을 사용해서 접근해야 함
    
    @staticmethod #static 메서드는 -> 스스로 staticmethod임을 나타내는 @을 사용함
    def description():
        print('신화는 한 나라 혹은 한 민족으로부터 전승되어 오는 예로부터 섬기는 신을 둘러싼 이야기를 뜻한다.')


dagun = Myth('dagun')
print(dagun.name) #dagun은 객체 그자체고, 그 인스턴스가 가진 값을 확인하기 위해선 dagun의 이름에 접근해야 함
greek_rome = Myth('greek & rome')
print(greek_rome.name)
print(f'현재까지 생성된 신화 수 : {Myth.type_of_myth}') #클래스 변수에 접근 
Myth.description()#class 자체에 접근해서 메서드 호출
