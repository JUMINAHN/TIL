# main.py


# 아래 클래스를 수정하시오. -> 초기화 메서드를 가지고 가로 x 세로 길이를 인자로 받아 속성으로 저장
class Shape():
    def __init__(self, width, height) :
        self.width = width
        self.height = height   


shape1 = Shape(5, 3)
print(shape1.width, shape1.height)
