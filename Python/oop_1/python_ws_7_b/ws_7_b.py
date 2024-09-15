# 아래에 코드를 작성하시오.
class Myth():
    type_of_myth = 0

    def __init__(self, name) :
        self.name = name
        Myth.type_of_myth += 1
    
    @staticmethod #static 메서드는 static 메서드 설정해야 함
    def description(): #신화에 대한 설명 -> static
        print('신화는 한 나라 혹은 한 민족으로부터 전승되어 오는 예로부터 섬기는 신을 둘러싼 이야기를 뜻한다.')

dangun = Myth('dangun')
print(dangun.name) #인스턴스 변수에 접근해야 함
greek_rome = Myth('greek & rome')
print(greek_rome.name)
print(f'현재까지 생성된 신화 수 : {Myth.type_of_myth}')
Myth.description() #description 스태틱 메서드 호출 -> 여기서 오류 터지는 듯






# 아래에 코드를 작성하시오. (끝)