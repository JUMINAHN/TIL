# 아래 클래스를 수정하시오.
class Shape:
    
    def __init__(self, width, height) :
        self.width = width
        self.height = height

    def __str__(self) :
        return f'Shape: width={self.width}, height={self.height}'


shape1 = Shape(5, 3)
print(shape1)
