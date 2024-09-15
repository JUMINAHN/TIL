# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self, width, height) :
        self.width = width
        self.height = height

    def print_info(self): #가로, 세로, 넓이, 둘레 출력 --> 인스턴스 생성
        print(f'Width: {self.width}\nHeight: {self.height}\nArea: {self.height * self.width}\nPerimeter: {(self.height+self.width)*2}')


shape1 = Shape(5, 3)
shape1.print_info()
